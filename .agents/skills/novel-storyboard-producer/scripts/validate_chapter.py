#!/usr/bin/env python3
"""Validate self-contained Segment folders for a storyboard chapter."""

from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from pathlib import Path


SEGMENT_DIR_RE = re.compile(r"^第0*(\d+)段$")
CHAPTER_DIR_RE = re.compile(r"^第0*(\d+)章$")
SHOT_RE = re.compile(r"(?m)^镜号(\d+)[（(]([0-9]+(?:\.[0-9]+)?)s[）)]")
REFERENCE_RE = re.compile(r"^@图(\d+)是([^，\r\n]+)$")
NUMBERED_FILE_RE = re.compile(r"^图(\d+)_(.+)$")
GRID_VALUES = {"一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7, "八": 8, "九": 9, "十": 10}
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tif", ".tiff"}
REQUIRED_SHOT_FIELDS = (
    "主体",
    "动作",
    "运镜",
    "风格",
    "对白/旁白",
    "声音与同步",
)
REQUIRED_SEGMENT_FIELDS = ("本段统一风格", "本段声音基线")
EMOTION_WORDS = {"高兴", "开心", "悲伤", "难过", "愤怒", "生气", "紧张", "害怕", "惊讶", "震惊", "激动", "焦虑", "平静", "冷漠"}
PERFORMANCE_CUES = (
    "目光", "视线", "眼", "眉", "嘴角", "唇", "下颌", "呼吸", "停顿", "肩", "手", "指",
    "姿态", "身体", "重心", "脚步", "前倾", "后退", "靠近", "拉开", "转身", "抬头", "低头",
    "收紧", "放松", "移开", "避开", "握", "推", "放下", "抬起", "坐", "站", "走", "停",
)
CJK_RE = re.compile(r"[\u3400-\u9fff]")
PROHIBITED_TERMS = (
    "血液飞溅", "喷血", "血池", "断头血", "内脏出血", "血腥场面", "流血",
    "分尸", "斩首", "虐杀", "酷刑", "断肢", "爆头", "撕咬", "屠杀", "尸横遍野", "骨裂",
    "全裸", "露点", "一丝不挂", "性交易", "乱伦", "恋童", "兽交", "性暗示", "色情互动",
    "乳房", "阴部", "生殖器", "邪教仪式", "食人恶鬼", "自残", "自杀", "黑帮火拼",
    "傻逼", "贱人", "废物", "滚蛋",
    "blood splatter", "spraying blood", "pool of blood", "severed-head blood", "internal bleeding",
    "gory scene", "bleeding", "dismemberment", "decapitation", "torture killing", "torture",
    "severed limb", "headshot", "mauling", "massacre", "bodies everywhere", "bone fracture",
    "full nudity", "explicit exposure", "completely naked", "sexual transaction", "incest",
    "pedophilia", "bestiality", "sexual innuendo", "erotic interaction", "breast", "genitals",
    "cult ritual", "cannibal demon", "self-harm", "suicide", "gang shootout",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="Project unit or chapter directory")
    parser.add_argument("--image-dir", type=Path, help="Explicit directory containing 第NN段 folders")
    parser.add_argument("--zip", dest="zip_path", type=Path, help="Optional chapter ZIP")
    parser.add_argument("--segments", type=int, help="Expected Segment count")
    parser.add_argument(
        "--seconds",
        type=float,
        default=15.0,
        help="Expected seconds per Segment; defaults to 15 and may be overridden by the user",
    )
    return parser.parse_args()


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def segment_number(path: Path) -> int | None:
    match = SEGMENT_DIR_RE.fullmatch(path.name)
    return int(match.group(1)) if match else None


def discover_segment_root(root: Path) -> Path | None:
    if any(path.is_dir() and segment_number(path) is not None for path in root.iterdir()):
        return root
    named = [path for path in root.rglob("*") if path.is_dir() and path.name in {"分镜图", "storyboards", "storyboard"}]
    usable = [path for path in named if any(child.is_dir() and segment_number(child) is not None for child in path.iterdir())]
    return sorted(usable)[0] if usable else None


def first_nonempty_line(text: str) -> str | None:
    return next((line.strip() for line in text.splitlines() if line.strip()), None)


def prohibited_match_count(text: str) -> int:
    folded = text.casefold()
    return sum(1 for term in PROHIBITED_TERMS if term.casefold() in folded)


def validate_shot_fields(text: str, segment_no: int) -> list[str]:
    errors: list[str] = []
    for field in REQUIRED_SEGMENT_FIELDS:
        field_match = re.search(rf"(?m)^{re.escape(field)}：\s*(.+?)\s*$", text)
        if not field_match:
            errors.append(f"Segment {segment_no}: missing or empty field {field}")
        elif not CJK_RE.search(field_match.group(1)):
            errors.append(f"Segment {segment_no}: field {field} must be written in Chinese")

    matches = list(SHOT_RE.finditer(text))
    for index, match in enumerate(matches):
        shot_no = int(match.group(1))
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[start:end]
        for field in REQUIRED_SHOT_FIELDS:
            field_match = re.search(rf"(?m)^{re.escape(field)}：\s*(.+?)\s*$", block)
            if not field_match:
                errors.append(f"Segment {segment_no}, shot {shot_no}: missing or empty field {field}")
                continue
            if not CJK_RE.search(field_match.group(1)):
                errors.append(f"Segment {segment_no}, shot {shot_no}: field {field} must be written in Chinese")
            if field == "动作":
                value = field_match.group(1).strip()
                compact = re.sub(r"[\s，。；、！!？?]+", "", value)
                if compact in EMOTION_WORDS or re.fullmatch(
                    rf"(?:很|非常|有些|十分)?(?:{'|'.join(EMOTION_WORDS)})(?:地|的)?", compact
                ):
                    errors.append(f"Segment {segment_no}, shot {shot_no}: 动作 cannot be an emotion label alone")
                elif any(word in value for word in EMOTION_WORDS) and not any(cue in value for cue in PERFORMANCE_CUES):
                    errors.append(
                        f"Segment {segment_no}, shot {shot_no}: emotional 动作 needs visible performance cues"
                    )
    return errors


def parse_declaration(line: str | None) -> tuple[list[tuple[int, str]], list[str]]:
    errors: list[str] = []
    if line is None:
        return [], ["TXT is empty"]
    parts = [part.strip() for part in line.split("，")]
    if not parts or parts[0] != "@图1是参考分镜图":
        return [], ["first non-empty line must begin with @图1是参考分镜图"]

    declared: list[tuple[int, str]] = []
    expected = 2
    seen_names: set[str] = set()
    for part in parts[1:]:
        match = REFERENCE_RE.fullmatch(part)
        if not match:
            errors.append(f"invalid reference declaration: {part}")
            continue
        number = int(match.group(1))
        name = match.group(2).strip()
        if number != expected:
            errors.append(f"reference numbering expected 图{expected}, found 图{number}")
            expected = number
        if name in seen_names:
            errors.append(f"duplicate declared character: {name}")
        declared.append((number, name))
        seen_names.add(name)
        expected += 1
    return declared, errors


def grid_count_from_name(name: str) -> int | None:
    arabic = re.search(r"(\d+)宫格", name)
    if arabic:
        return int(arabic.group(1))
    chinese = re.search(r"([一二三四五六七八九十])宫格", name)
    return GRID_VALUES.get(chinese.group(1)) if chinese else None


def numbered_images(segment_dir: Path) -> tuple[dict[int, list[tuple[str, Path]]], list[Path]]:
    numbered: dict[int, list[tuple[str, Path]]] = {}
    unnumbered: list[Path] = []
    for path in sorted(segment_dir.iterdir()):
        if not path.is_file() or path.suffix.lower() not in IMAGE_SUFFIXES:
            continue
        match = NUMBERED_FILE_RE.fullmatch(path.stem)
        if not match:
            unnumbered.append(path)
            continue
        numbered.setdefault(int(match.group(1)), []).append((match.group(2), path))
    return numbered, unnumbered


def main() -> int:
    args = parse_args()
    errors: list[str] = []
    warnings: list[str] = []

    segment_root = args.image_dir or discover_segment_root(args.root)
    if segment_root is None or not segment_root.exists():
        return finish(["No directory containing 第NN段 Segment folders found"], warnings, {})

    segment_dirs = sorted(
        (path for path in segment_root.iterdir() if path.is_dir() and segment_number(path) is not None),
        key=lambda path: segment_number(path) or 0,
    )
    if args.segments is not None and len(segment_dirs) != args.segments:
        errors.append(f"Expected {args.segments} Segments, found {len(segment_dirs)}")
    if not segment_dirs:
        errors.append("No 第NN段 Segment folders found")

    voice_profiles = sorted(args.root.rglob("角色音色档案.md"))
    if len(voice_profiles) != 1:
        errors.append(f"Expected exactly one 角色音色档案.md, found {len(voice_profiles)}")
        voice_profile = None
    else:
        voice_profile = voice_profiles[0]
        if prohibited_match_count(read(voice_profile)):
            errors.append("角色音色档案.md contains prohibited literal content and must be safely rewritten")

    chapter_match = CHAPTER_DIR_RE.fullmatch(args.root.name)
    chapter_no = int(chapter_match.group(1)) if chapter_match else None
    expected_index_name = f"第{chapter_no:03d}章_生产索引.md" if chapter_no is not None else None
    production_indexes = sorted(args.root.glob("第*章_生产索引.md"))
    if len(production_indexes) != 1:
        errors.append(f"Expected exactly one chapter production index, found {len(production_indexes)}")
        production_index = None
    else:
        production_index = production_indexes[0]
        if expected_index_name and production_index.name != expected_index_name:
            errors.append(f"Production index is {production_index.name}, expected {expected_index_name}")
        if prohibited_match_count(read(production_index)):
            errors.append("Chapter production index contains prohibited literal content and must be safely rewritten")

    details: list[dict[str, object]] = []
    for segment_dir in segment_dirs:
        segment_no = segment_number(segment_dir)
        assert segment_no is not None
        expected_dir = f"第{segment_no:02d}段"
        if segment_dir.name != expected_dir:
            errors.append(f"Segment {segment_no}: folder is {segment_dir.name}, expected {expected_dir}")

        txt_files = sorted(segment_dir.glob("*.txt"))
        expected_txt = f"第{segment_no:02d}段.txt"
        if len(txt_files) != 1:
            errors.append(f"Segment {segment_no}: expected exactly one TXT, found {len(txt_files)}")
            details.append({"segment": segment_no, "shots": 0, "seconds": 0.0})
            continue
        txt_path = txt_files[0]
        if txt_path.name != expected_txt:
            errors.append(f"Segment {segment_no}: TXT is {txt_path.name}, expected {expected_txt}")

        text = read(txt_path)
        if prohibited_match_count(text):
            errors.append(f"Segment {segment_no}: TXT contains prohibited literal content and must be safely rewritten")
        declared, declaration_errors = parse_declaration(first_nonempty_line(text))
        errors.extend(f"Segment {segment_no}: {message}" for message in declaration_errors)

        shots = SHOT_RE.findall(text)
        shot_numbers = [int(number) for number, _ in shots]
        durations = [float(seconds) for _, seconds in shots]
        if shot_numbers != list(range(1, len(shots) + 1)):
            errors.append(f"Segment {segment_no}: non-sequential shot numbers {shot_numbers}")
        if not shots:
            errors.append(f"Segment {segment_no}: no timed shots found")
        errors.extend(validate_shot_fields(text, segment_no))
        total_seconds = sum(durations)
        if abs(total_seconds - args.seconds) > 0.01:
            errors.append(f"Segment {segment_no}: duration {total_seconds:.1f}s, expected {args.seconds:.1f}s")

        images, unnumbered = numbered_images(segment_dir)
        if unnumbered:
            errors.append(f"Segment {segment_no}: unnumbered image files {[path.name for path in unnumbered]}")

        grid_files = images.get(1, [])
        if len(grid_files) != 1 or not grid_files[0][0].startswith("参考分镜图_"):
            found = [path.name for _, path in grid_files]
            errors.append(f"Segment {segment_no}: expected one 图1_参考分镜图_N宫格 image, found {found}")
        else:
            grid_count = grid_count_from_name(grid_files[0][1].stem)
            if grid_count is None:
                errors.append(f"Segment {segment_no}: grid filename does not declare N宫格")
            elif grid_count != len(shots):
                errors.append(f"Segment {segment_no}: grid declares {grid_count} panels but TXT has {len(shots)} shots")

        expected_numbers = {1}
        for image_no, character_name in declared:
            expected_numbers.add(image_no)
            matches = images.get(image_no, [])
            if len(matches) != 1 or matches[0][0] != character_name:
                found = [path.name for _, path in matches]
                errors.append(
                    f"Segment {segment_no}: @图{image_no}是{character_name} requires one 图{image_no}_{character_name} image, found {found}"
                )

        extra_numbers = sorted(set(images) - expected_numbers)
        if extra_numbers:
            extras = [path.name for number in extra_numbers for _, path in images[number]]
            errors.append(f"Segment {segment_no}: numbered images not declared in TXT: {extras}")

        details.append(
            {
                "segment": segment_no,
                "txt": txt_path.name,
                "shots": len(shots),
                "seconds": round(total_seconds, 1),
                "characters": [name for _, name in declared],
            }
        )

    if args.zip_path:
        if not args.zip_path.exists():
            errors.append(f"ZIP does not exist: {args.zip_path}")
        else:
            if chapter_no is not None:
                expected_zip_name = f"第{chapter_no:03d}章_全部Segment.zip"
                if args.zip_path.name != expected_zip_name:
                    errors.append(f"ZIP is {args.zip_path.name}, expected {expected_zip_name}")
            with zipfile.ZipFile(args.zip_path) as archive:
                entries = {item.filename.replace("\\", "/") for item in archive.infolist() if not item.is_dir()}
            required = {
                path.relative_to(segment_root).as_posix()
                for segment_dir in segment_dirs
                for path in segment_dir.iterdir()
                if path.is_file()
            }
            missing = sorted(
                relative
                for relative in required
                if relative not in entries and not any(entry.endswith(f"/{relative}") for entry in entries)
            )
            if missing:
                errors.append(f"ZIP is missing {len(missing)} formal files: {missing}")
            if voice_profile is not None:
                voice_name = voice_profile.name
                if voice_name not in entries and not any(entry.endswith(f"/{voice_name}") for entry in entries):
                    errors.append("ZIP is missing 角色音色档案.md")
            if production_index is not None:
                index_name = production_index.name
                if index_name not in entries and not any(entry.endswith(f"/{index_name}") for entry in entries):
                    errors.append("ZIP is missing the chapter production index")

    return finish(
        errors,
        warnings,
        {
            "segment_root": str(segment_root),
            "voice_profile": str(voice_profile) if voice_profile else None,
            "production_index": str(production_index) if production_index else None,
            "segments": details,
        },
    )


def finish(errors: list[str], warnings: list[str], data: dict) -> int:
    print(json.dumps({"ok": not errors, "errors": errors, "warnings": warnings, **data}, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
