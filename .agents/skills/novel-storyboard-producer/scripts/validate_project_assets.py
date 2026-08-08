#!/usr/bin/env python3
"""Validate project-level master character and scene asset naming."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tif", ".tiff"}
CHARACTER_RE = re.compile(
    r"^(?P<name>.+)_首次出现第(?P<chapter>\d{3,})章_"
    r"(?P<class>main|single-scene|persistent-world-stage)"
    r"(?:_(?P<label>[^_]+))?_v(?P<version>\d+)$"
)
SCENE_RE = re.compile(
    r"^(?P<name>.+)_首次出现第(?P<chapter>\d{3,})章"
    r"(?:_(?P<label>[^_]+))?_v(?P<version>\d+)$"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="Novel storyboard project root")
    return parser.parse_args()


def validate_folder(folder: Path, pattern: re.Pattern[str], asset_type: str) -> tuple[list[str], list[dict[str, object]]]:
    errors: list[str] = []
    records: list[dict[str, object]] = []
    if not folder.is_dir():
        return [f"Missing folder: {folder}"], records

    for path in sorted(folder.iterdir()):
        if not path.is_file():
            errors.append(f"{asset_type}: unexpected directory {path.name}")
            continue
        if path.suffix.lower() not in IMAGE_SUFFIXES:
            errors.append(f"{asset_type}: unsupported or non-image file {path.name}")
            continue
        match = pattern.fullmatch(path.stem)
        if not match:
            errors.append(f"{asset_type}: invalid filename {path.name}")
            continue
        data = match.groupdict()
        chapter = int(data["chapter"])
        version = int(data["version"])
        if chapter < 1:
            errors.append(f"{asset_type}: chapter must be at least 001 in {path.name}")
        if version < 1:
            errors.append(f"{asset_type}: version must be at least v1 in {path.name}")
        records.append(
            {
                "name": data["name"],
                "chapter": chapter,
                "class": data.get("class"),
                "label": data.get("label"),
                "version": version,
                "file": str(path),
            }
        )
    return errors, records


def main() -> int:
    args = parse_args()
    master = args.root / "总资产"
    errors: list[str] = []
    warnings: list[str] = []

    if not master.is_dir():
        return finish([f"Missing master asset folder: {master}"], warnings, {})

    settings_path = args.root / "项目制作设定.md"
    if not settings_path.is_file():
        errors.append(f"Missing project settings: {settings_path}")
    else:
        settings_text = settings_path.read_text(encoding="utf-8-sig")
        required_settings = (
            "生效范围",
            "画面风格",
            "Segment时长",
            "每章预计时长",
            "对白策略",
            "大场面对抗",
            "画幅",
            "人物与场景资产策略",
            "交付范围",
            "固定安全规则",
            "最近确认日期",
        )
        missing_settings = [field for field in required_settings if not re.search(rf"(?m)^-\s*{re.escape(field)}：\s*\S+", settings_text)]
        if missing_settings:
            errors.append(f"Project settings missing confirmed fields: {missing_settings}")
        if not re.search(r"(?m)^-\s*固定安全规则：\s*启用，不可关闭\s*$", settings_text):
            errors.append("Project settings must keep the fixed safety gate enabled and non-disableable")

    index_path = master / "资产索引.md"
    if not index_path.is_file():
        errors.append(f"Missing asset index: {index_path}")

    character_errors, characters = validate_folder(master / "人物人设图", CHARACTER_RE, "character")
    scene_errors, scenes = validate_folder(master / "场景图", SCENE_RE, "scene")
    errors.extend(character_errors)
    errors.extend(scene_errors)

    if not characters:
        warnings.append("No valid master character images found")
    if not scenes:
        warnings.append("No valid master scene images found")

    duplicate_keys: set[tuple[object, ...]] = set()
    seen: set[tuple[object, ...]] = set()
    for record in characters + scenes:
        key = (record["name"], record["chapter"], record["class"], record["label"], record["version"])
        if key in seen:
            duplicate_keys.add(key)
        seen.add(key)
    if duplicate_keys:
        errors.append(f"Duplicate master asset version keys: {len(duplicate_keys)}")

    return finish(
        errors,
        warnings,
        {
            "project_settings": str(settings_path),
            "characters": characters,
            "scenes": scenes,
            "asset_index": str(index_path),
        },
    )


def finish(errors: list[str], warnings: list[str], data: dict) -> int:
    print(json.dumps({"ok": not errors, "errors": errors, "warnings": warnings, **data}, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
