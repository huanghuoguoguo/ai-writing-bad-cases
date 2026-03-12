from __future__ import annotations

import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent
DATA_ROOT = REPO_ROOT / "data" / "cases"
MANIFEST_PATH = DATA_ROOT / "manifest.json"
OUTPUT_ROOT = REPO_ROOT / "docs" / "cases"


def load_manifest() -> dict:
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def load_payload(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def format_matchers(matchers: list[dict]) -> list[str]:
    lines: list[str] = []
    for matcher in matchers:
        matcher_type = matcher["type"]
        pattern = matcher["pattern"]
        weight = matcher.get("weight", 1.0)
        lines.append(f"- `{matcher_type}`: `{pattern}` (weight={weight})")
    return lines


def render_record(record: dict, index: int) -> list[str]:
    lines = [
        f"## {index}. {record['label']}",
        "",
        f"- `id`: `{record['id']}`",
        f"- `severity`: `{record['severity']}`",
        f"- `diagnostic_dimensions`: {', '.join(record['diagnostic_dimensions'])}",
        f"- 描述：{record['description']}",
    ]

    if record.get("aliases"):
        lines.append(f"- 别名：{', '.join(record['aliases'])}")

    if record.get("why_it_sounds_ai"):
        lines.append(f"- 为什么像 AI：{record['why_it_sounds_ai']}")

    lines.extend(
        [
            "- 匹配规则：",
            *format_matchers(record["matchers"]),
        ]
    )

    if record.get("examples"):
        lines.append("- 示例：")
        lines.extend(f"  - {item}" for item in record["examples"])

    if record.get("counter_examples"):
        lines.append("- 更像人的写法：")
        lines.extend(f"  - {item}" for item in record["counter_examples"])

    lines.append(f"- 改写提示：{record['rewrite_hint']}")

    if record.get("prompt_rule"):
        lines.append(f"- Prompt 规则：{record['prompt_rule']}")

    lines.append("")
    return lines


def render_file(lang: str, genre: str, payload: dict) -> str:
    title = f"{lang.upper()} / {genre}"
    lines = [
        f"# {title}",
        "",
        "> This file is generated from `data/cases/*.json` by `python3 render_cases_md.py`.",
        "",
    ]

    records = payload.get("records", [])
    if not records:
        lines.append("暂无记录。")
        lines.append("")
        return "\n".join(lines)

    for index, record in enumerate(records, start=1):
        lines.extend(render_record(record, index))

    return "\n".join(lines)


def main() -> None:
    manifest = load_manifest()
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)

    for item in manifest["files"]:
        relative_path = Path(item["path"])
        payload = load_payload(REPO_ROOT / relative_path)
        lang = item["lang"]
        genre = item["genre"]

        output_dir = OUTPUT_ROOT / lang
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / f"{genre}.md"
        output_path.write_text(render_file(lang, genre, payload), encoding="utf-8")
        print(f"rendered {output_path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
