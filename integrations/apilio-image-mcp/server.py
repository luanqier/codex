#!/usr/bin/env python3
"""Minimal MCP server for Apilio image generation.

Uses only the Python standard library so Codex can launch it without installing
extra packages. The API key is read from APILIO_API_KEY and is never returned.
"""

from __future__ import annotations

import base64
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path
from typing import Any


SERVER_NAME = "apilio-image"
SERVER_VERSION = "1.0.0"
DEFAULT_BASE_URL = "https://api.apilio.ai"
DEFAULT_MODEL = "gemini-3.1-flash-lite-image"
DEFAULT_OUTPUT_DIR = Path.home() / "Pictures" / "Codex-Apilio"


def _send(payload: dict[str, Any]) -> None:
    sys.stdout.write(json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n")
    sys.stdout.flush()


def _error(message: str) -> dict[str, Any]:
    return {"content": [{"type": "text", "text": message}], "isError": True}


def _safe_filename(prompt: str) -> str:
    stem = re.sub(r"[^\w\-]+", "-", prompt.strip(), flags=re.UNICODE).strip("-")
    return (stem or "image")[:48]


def _request_json(method: str, url: str, api_key: str, body: dict[str, Any] | None = None) -> dict[str, Any]:
    data = None if body is None else json.dumps(body, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": f"Codex-{SERVER_NAME}/{SERVER_VERSION}",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=180) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Apilio HTTP {exc.code}: {detail[:800]}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Unable to reach Apilio: {exc.reason}") from exc


def _walk(value: Any):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from _walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from _walk(child)


def _extract_image(response: dict[str, Any]) -> tuple[bytes | None, str | None, str]:
    for item in _walk(response):
        for key in ("b64_json", "base64", "image_base64"):
            encoded = item.get(key)
            if isinstance(encoded, str) and len(encoded) > 100:
                if encoded.startswith("data:"):
                    encoded = encoded.split(",", 1)[1]
                return base64.b64decode(encoded), None, "image/png"
        for key in ("url", "image_url", "output_url"):
            url = item.get(key)
            if isinstance(url, str) and url.startswith(("https://", "http://")):
                return None, url, "image/png"
    return None, None, "image/png"


def _extract_task_id(response: dict[str, Any]) -> str | None:
    for item in _walk(response):
        for key in ("task_id", "id"):
            value = item.get(key)
            if isinstance(value, str) and value and not value.startswith("http"):
                status = str(item.get("status", "")).upper()
                if key == "task_id" or status in {"PENDING", "QUEUED", "IN_PROGRESS", "PROCESSING"}:
                    return value
    return None


def _download(url: str) -> tuple[bytes, str]:
    request = urllib.request.Request(url, headers={"User-Agent": f"Codex-{SERVER_NAME}/{SERVER_VERSION}"})
    with urllib.request.urlopen(request, timeout=120) as response:
        mime = response.headers.get_content_type() or "image/png"
        return response.read(), mime


def _resolve_output_path(raw_path: str | None, prompt: str, mime: str) -> Path:
    extension = {"image/jpeg": ".jpg", "image/webp": ".webp"}.get(mime, ".png")
    if raw_path:
        path = Path(os.path.expandvars(os.path.expanduser(raw_path)))
        suffix = path.suffix.lower()
        valid_for_mime = {
            "image/png": {".png"},
            "image/jpeg": {".jpg", ".jpeg"},
            "image/webp": {".webp"},
        }.get(mime, {extension})
        if suffix not in valid_for_mime:
            path = path.with_suffix(extension)
    else:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        path = DEFAULT_OUTPUT_DIR / f"{timestamp}-{_safe_filename(prompt)}{extension}"
    path.parent.mkdir(parents=True, exist_ok=True)
    return path.resolve()


def generate_image(arguments: dict[str, Any]) -> dict[str, Any]:
    prompt = str(arguments.get("prompt", "")).strip()
    if not prompt:
        return _error("prompt is required")

    api_key = os.environ.get("APILIO_API_KEY", "").strip()
    if not api_key:
        return _error("APILIO_API_KEY is not configured. Restart Codex after setting the user environment variable.")

    base_url = os.environ.get("APILIO_BASE_URL", DEFAULT_BASE_URL).rstrip("/")
    body: dict[str, Any] = {"model": DEFAULT_MODEL, "prompt": prompt}
    aspect_ratio = str(arguments.get("aspect_ratio", "")).strip()
    if aspect_ratio:
        body["aspect_ratio"] = aspect_ratio

    try:
        response = _request_json("POST", f"{base_url}/v1/images/generations", api_key, body)
        image_bytes, image_url, mime = _extract_image(response)

        task_id = _extract_task_id(response) if image_bytes is None and image_url is None else None
        if task_id:
            deadline = time.monotonic() + 180
            while time.monotonic() < deadline:
                time.sleep(2)
                status_response = _request_json(
                    "GET", f"{base_url}/v1/images/tasks/{urllib.parse.quote(task_id)}", api_key
                )
                image_bytes, image_url, mime = _extract_image(status_response)
                if image_bytes is not None or image_url is not None:
                    response = status_response
                    break
                status_text = json.dumps(status_response, ensure_ascii=False).upper()
                if "FAILURE" in status_text or '"FAILED"' in status_text:
                    raise RuntimeError(f"Apilio task failed: {json.dumps(status_response, ensure_ascii=False)[:800]}")

        if image_bytes is None and image_url:
            image_bytes, downloaded_mime = _download(image_url)
            if downloaded_mime.startswith("image/"):
                mime = downloaded_mime

        if image_bytes is None:
            raise RuntimeError(f"Apilio returned no image: {json.dumps(response, ensure_ascii=False)[:1000]}")

        output_path = _resolve_output_path(arguments.get("output_path"), prompt, mime)
        output_path.write_bytes(image_bytes)
        encoded = base64.b64encode(image_bytes).decode("ascii")
        return {
            "content": [
                {
                    "type": "text",
                    "text": (
                        f"Image generated with {DEFAULT_MODEL}.\n"
                        f"Saved to: {output_path}\n"
                        f"Size: {len(image_bytes)} bytes"
                    ),
                },
                {"type": "image", "data": encoded, "mimeType": mime},
            ],
            "structuredContent": {
                "model": DEFAULT_MODEL,
                "path": str(output_path),
                "bytes": len(image_bytes),
                "mime_type": mime,
            },
        }
    except Exception as exc:
        return _error(str(exc))


TOOLS = [
    {
        "name": "generate_image",
        "description": (
            "Generate an image through Apilio using gemini-3.1-flash-lite-image, "
            "save it locally, and return an image preview."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "prompt": {"type": "string", "description": "Detailed image-generation prompt."},
                "aspect_ratio": {
                    "type": "string",
                    "description": "Optional aspect ratio such as 1:1, 16:9, 9:16, 4:3, or 3:4.",
                },
                "output_path": {
                    "type": "string",
                    "description": "Optional absolute local output path. Defaults to Pictures/Codex-Apilio.",
                },
            },
            "required": ["prompt"],
            "additionalProperties": False,
        },
        "annotations": {"readOnlyHint": False, "destructiveHint": False, "openWorldHint": True},
    }
]


def handle(request: dict[str, Any]) -> dict[str, Any] | None:
    method = request.get("method")
    request_id = request.get("id")
    if method == "initialize":
        requested_version = request.get("params", {}).get("protocolVersion", "2025-06-18")
        result = {
            "protocolVersion": requested_version,
            "capabilities": {"tools": {"listChanged": False}},
            "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION},
            "instructions": (
                "Use generate_image when the user explicitly asks to generate an image with Apilio "
                "or gemini-3.1-flash-lite-image. Generated files are saved locally."
            ),
        }
    elif method == "tools/list":
        result = {"tools": TOOLS}
    elif method == "tools/call":
        params = request.get("params", {})
        if params.get("name") != "generate_image":
            result = _error(f"Unknown tool: {params.get('name')}")
        else:
            result = generate_image(params.get("arguments", {}))
    elif method == "ping":
        result = {}
    elif method and method.startswith("notifications/"):
        return None
    else:
        if request_id is None:
            return None
        return {"jsonrpc": "2.0", "id": request_id, "error": {"code": -32601, "message": f"Method not found: {method}"}}
    if request_id is None:
        return None
    return {"jsonrpc": "2.0", "id": request_id, "result": result}


def main() -> None:
    for raw_line in sys.stdin.buffer:
        try:
            line = raw_line.decode("utf-8").strip()
            if not line:
                continue
            request = json.loads(line)
            response = handle(request)
            if response is not None:
                _send(response)
        except Exception as exc:
            request_id = request.get("id") if isinstance(locals().get("request"), dict) else None
            _send({"jsonrpc": "2.0", "id": request_id, "error": {"code": -32603, "message": str(exc)}})


if __name__ == "__main__":
    main()
