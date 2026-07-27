#!/usr/bin/env python3
"""Rebuild generated course artifacts from the canonical course sources.

Canonical inputs:
- data/course.config.json: shell, routes, version, progress, quiz extensions
- data/course_data.json: historical paper/model dataset
- data/source_index.json: source reader inventory

Generated outputs:
- vendor/course-config.js
- data/course_data.bundle.js (file:// fallback)
- data/papers_index.json (compatibility alias)
- manifest.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "data/course.config.json"
DATA_PATH = ROOT / "data/course_data.json"
SOURCE_INDEX_PATH = ROOT / "data/source_index.json"
GENERATED = {
    ROOT / "vendor/course-config.js",
    ROOT / "data/course_data.bundle.js",
    ROOT / "data/course_overview.json",
    ROOT / "data/course_overview.bundle.js",
    ROOT / "data/papers_index.json",
}
EXCLUDED_FROM_MANIFEST = {
    "manifest.json",
}
EXCLUDED_SUFFIXES = {".zip", ".sha256", ".pyc"}
EXCLUDED_PARTS = {".git", "__pycache__", ".pytest_cache"}


def load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def compact_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def pretty_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def overview_data(data: dict[str, Any], version: str) -> dict[str, Any]:
    """Build the small dataset needed for the initial map/list render."""
    paper_fields = (
        "id", "folder", "year", "authors", "titles", "module", "type",
        "historical_state_before", "new_step", "paper_id",
    )
    return {
        "schema_version": "1.0",
        "course_version": version,
        "title": data.get("title", {}),
        "modules": data.get("modules", []),
        "dependencies": data.get("dependencies", []),
        "papers": [
            {key: paper[key] for key in paper_fields if key in paper}
            for paper in data.get("papers", [])
        ],
    }


def generated_contents(config: dict[str, Any], data: dict[str, Any]) -> dict[Path, str]:
    version = str(config["courseVersion"])
    normalized = dict(data)
    normalized["schema_version"] = "1.0"
    normalized["course_version"] = version
    overview = overview_data(normalized, version)
    return {
        ROOT / "vendor/course-config.js": (
            "/* GENERATED from data/course.config.json — do not edit directly. */\n"
            f"window.QM_COURSE_CONFIG=Object.freeze({compact_json(config)});\n"
        ),
        ROOT / "data/course_data.bundle.js": (
            "/* GENERATED from data/course_data.json — lazy full-detail file:// fallback. */\n"
            f"window.QM_COURSE_DATA={compact_json(normalized)};\n"
        ),
        ROOT / "data/course_overview.json": pretty_json(overview),
        ROOT / "data/course_overview.bundle.js": (
            "/* GENERATED lightweight index dataset. */\n"
            f"window.QM_COURSE_OVERVIEW={compact_json(overview)};\n"
        ),
        ROOT / "data/papers_index.json": pretty_json(normalized),
    }


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def iter_manifest_files() -> list[Path]:
    paths: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT)
        if rel.as_posix() in EXCLUDED_FROM_MANIFEST:
            continue
        if any(part in EXCLUDED_PARTS for part in rel.parts):
            continue
        if path.suffix in EXCLUDED_SUFFIXES:
            continue
        paths.append(path)
    return sorted(paths, key=lambda p: p.relative_to(ROOT).as_posix())


def count_source_texts() -> int:
    return sum(1 for pattern in ("sources/**/*.md", "summaries/**/*.md") for _ in ROOT.glob(pattern))


def count_primary_images() -> int:
    image_suffixes = {".png", ".jpg", ".jpeg", ".webp", ".svg"}
    return sum(1 for p in (ROOT / "sources").rglob("*") if p.is_file() and p.suffix.lower() in image_suffixes)


def build_manifest(config: dict[str, Any], course_data: dict[str, Any], source_index: dict[str, Any]) -> dict[str, Any]:
    files = []
    for path in iter_manifest_files():
        rel = path.relative_to(ROOT).as_posix()
        files.append({"path": rel, "size": path.stat().st_size, "sha256": sha256(path)})
    papers = source_index.get("papers", [])
    experiments = course_data.get("experiments", [])
    return {
        "version": str(config["courseVersion"]),
        "product_name": config.get("title", {}).get("de", "Quantum course"),
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "status": "interaction-correction release candidate",
        "canonical_sources": [
            "data/course.config.json",
            "data/course_data.json",
            "data/source_index.json",
        ],
        "contents": {
            "paper_count": len(papers),
            "pdf_count": sum(bool(p.get("pdf_path")) for p in papers),
            "source_and_summary_markdown_files": count_source_texts(),
            "primary_source_images": count_primary_images(),
            "historical_model_sections": len(experiments),
            "guided_stages": len(config.get("stages", [])),
            "advanced_quiz_questions": len(config.get("advancedQuizQuestions", {})),
            "primer_units": 7,
        },
        "architecture": {
            "progress_key": config.get("progress", {}).get("key"),
            "legacy_progress_keys": config.get("progress", {}).get("legacyKeys", []),
            "iframe_protocol": "qm-course-v1",
            "math_modes": config.get("math", {}).get("modes", []),
            "default_math_mode": config.get("math", {}).get("defaultMode"),
            "initial_index_html_bytes": (ROOT / "index.html").stat().st_size,
            "plotly_loading": "lazy local loader",
            "css_entrypoint": "vendor/course-shell.css",
        },
        "package": {
            "file_count": len(files),
            "uncompressed_bytes": sum(item["size"] for item in files),
        },
        "files": files,
    }


def validate_architecture(config: dict[str, Any], data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    version = str(config.get("courseVersion", ""))
    progress = config.get("progress", {})
    if progress.get("key") != "qm_course_progress_v1":
        errors.append("canonical progress key must be qm_course_progress_v1")
    if len({s.get("id") for s in config.get("stages", [])}) != len(config.get("stages", [])):
        errors.append("stage IDs are not unique")
    if len({s.get("url") for s in config.get("stages", [])}) != len(config.get("stages", [])):
        errors.append("stage URLs are not unique")
    if data.get("course_version") != version:
        errors.append("data/course_data.json course_version differs from course config")

    required_shared = (
        "vendor/course-config.js?v=",
        "vendor/qm-state.js?v=",
        "vendor/page-api.js?v=",
        "vendor/course-shell.js?v=",
        "vendor/course-enhancements.js?v=",
    )
    html_pages = [p for p in sorted(ROOT.glob("*.html")) if p.name != "progress.html"]
    for page in html_pages:
        text = page.read_text(encoding="utf-8")
        for token in required_shared:
            if token not in text:
                errors.append(f"{page.name}: missing shared runtime {token.rstrip('=')}")
        if '<header aria-label="Course navigation" class="course-shell"></header>' not in text:
            errors.append(f"{page.name}: missing generated shell mount point")
        old_versions = set(re.findall(r"[?&]v=(0\.\d+)", text)) - {version}
        if old_versions:
            errors.append(f"{page.name}: stale cache-buster versions {sorted(old_versions)}")

    index_text = (ROOT / "index.html").read_text(encoding="utf-8")
    if "window.QM_COURSE_OVERVIEW" not in index_text:
        errors.append("index.html does not consume the lightweight overview bundle")
    if "vendor/course-data-loader.js" not in index_text:
        errors.append("index.html does not lazy-load full paper details")
    if "<script id=\"courseData\"" in index_text or "const DATA = JSON.parse" in index_text:
        errors.append("index.html still embeds the large course dataset")
    if (ROOT / "index.html").stat().st_size > 450_000:
        errors.append("index.html exceeds the 450 kB stabilization target")

    shell = (ROOT / "vendor/course-shell.js").read_text(encoding="utf-8")
    enhancements = (ROOT / "vendor/course-enhancements.js").read_text(encoding="utf-8")
    for name, text in (("course-shell.js", shell), ("course-enhancements.js", enhancements)):
        if re.search(r"\bconst\s+stages\s*=\s*\[", text, re.I):
            errors.append(f"{name}: duplicates stage definitions instead of reading the config")
    css_entry = (ROOT / "vendor/course-shell.css").read_text(encoding="utf-8")
    for stylesheet in ("tokens.css", "shell.css", "learning.css", "rail.css", "math.css"):
        if stylesheet not in css_entry:
            errors.append(f"course-shell.css does not import {stylesheet}")

    math_modes = set(config.get("math", {}).get("modes", []))
    if math_modes != {"explicit", "hybrid", "defensive"}:
        errors.append("math modes must be explicit, hybrid, and defensive")
    quiz_types = {q.get("type") for q in config.get("advancedQuizQuestions", {}).values()}
    if not {"number", "multi"}.issubset(quiz_types):
        errors.append("advanced quiz bank must include number and multi-select questions")
    return errors


def compare_generated(expected: dict[Path, str]) -> list[str]:
    errors: list[str] = []
    for path, content in expected.items():
        if not path.exists():
            errors.append(f"missing generated file: {path.relative_to(ROOT)}")
        elif path.read_text(encoding="utf-8") != content:
            errors.append(f"generated file is stale: {path.relative_to(ROOT)}")
    return errors


def validate_manifest(config: dict[str, Any], course_data: dict[str, Any], source_index: dict[str, Any]) -> list[str]:
    path = ROOT / "manifest.json"
    if not path.exists():
        return ["manifest.json is missing"]
    actual = load_json(path)
    expected = build_manifest(config, course_data, source_index)
    errors: list[str] = []
    for key in ("version", "product_name", "status", "canonical_sources", "contents", "architecture", "package", "files"):
        if actual.get(key) != expected.get(key):
            errors.append(f"manifest.json field is stale: {key}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="validate without writing generated files")
    parser.add_argument("--no-manifest", action="store_true", help="skip manifest generation/check")
    args = parser.parse_args()

    config = load_json(CONFIG_PATH)
    course_data = load_json(DATA_PATH)
    source_index = load_json(SOURCE_INDEX_PATH)
    expected = generated_contents(config, course_data)

    errors = validate_architecture(config, course_data)
    if args.check:
        errors.extend(compare_generated(expected))
        if not args.no_manifest:
            errors.extend(validate_manifest(config, course_data, source_index))
    else:
        for path, content in expected.items():
            path.write_text(content, encoding="utf-8")
        # Ensure canonical JSON itself carries the current version/schema.
        normalized = dict(course_data)
        normalized["schema_version"] = "1.0"
        normalized["course_version"] = str(config["courseVersion"])
        DATA_PATH.write_text(pretty_json(normalized), encoding="utf-8")
        if not args.no_manifest:
            manifest = build_manifest(config, normalized, source_index)
            (ROOT / "manifest.json").write_text(pretty_json(manifest), encoding="utf-8")

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    mode = "verified" if args.check else "rebuilt"
    print(f"OK: generated course artifacts {mode} from the canonical sources.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
