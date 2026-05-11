#!/usr/bin/env python3
"""Compare Korean and English prompt token counts with tiktoken."""

from __future__ import annotations

import html
import json
from pathlib import Path

import tiktoken


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets"
RESULTS_PATH = OUT_DIR / "token-comparison.json"
SVG_PATH = OUT_DIR / "token-comparison.svg"

MODEL = "gpt-4o"

SAMPLES = [
    {
        "label": "Refactor",
        "ko": "이 함수 동작은 그대로 두고 더 깔끔하게 바꿔줘.",
        "en": "Could you refactor this function to make it cleaner while keeping the behavior the same?",
    },
    {
        "label": "Review",
        "ko": "이 PR에서 회귀 버그가 생길 만한 부분을 리뷰해줘.",
        "en": "Could you review this PR for possible regressions?",
    },
    {
        "label": "Tests",
        "ko": "이 변경사항에 맞는 테스트를 추가하고 실패하는 케이스도 확인해줘.",
        "en": "Please add tests for this change and check the failing cases too.",
    },
    {
        "label": "Bug fix",
        "ko": "로그인 후 대시보드로 이동하지 않는 문제를 원인부터 찾아서 고쳐줘.",
        "en": "Please investigate why login does not redirect to the dashboard and fix it.",
    },
    {
        "label": "Docs",
        "ko": "설치 방법을 README에 짧고 알기 쉽게 정리해줘.",
        "en": "Please make the installation instructions in the README short and easy to follow.",
    },
]


def token_count(encoding: tiktoken.Encoding, text: str) -> int:
    return len(encoding.encode(text))


def build_results() -> list[dict[str, object]]:
    encoding = tiktoken.encoding_for_model(MODEL)
    results = []
    for sample in SAMPLES:
        ko_tokens = token_count(encoding, sample["ko"])
        en_tokens = token_count(encoding, sample["en"])
        results.append(
            {
                "label": sample["label"],
                "korean": sample["ko"],
                "english": sample["en"],
                "korean_tokens": ko_tokens,
                "english_tokens": en_tokens,
                "delta": ko_tokens - en_tokens,
            }
        )
    return results


def svg_text(x: int, y: int, text: str, *, size: int = 14, weight: str = "400", anchor: str = "start") -> str:
    return (
        f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" '
        f'font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="#1f2937">'
        f"{html.escape(text)}</text>"
    )


def build_svg(results: list[dict[str, object]]) -> str:
    width = 920
    height = 420
    left = 150
    top = 82
    row_gap = 58
    bar_height = 16
    chart_width = 620
    max_tokens = max(max(int(r["korean_tokens"]), int(r["english_tokens"])) for r in results)
    scale = chart_width / max_tokens

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        svg_text(40, 38, f"Korean vs English Prompt Token Counts ({MODEL})", size=22, weight="700"),
        svg_text(40, 62, "Measured with OpenAI tiktoken; lower is not guaranteed for every sentence.", size=13),
        '<rect x="642" y="30" width="14" height="14" rx="2" fill="#2563eb"/>',
        svg_text(664, 42, "Korean", size=13),
        '<rect x="735" y="30" width="14" height="14" rx="2" fill="#16a34a"/>',
        svg_text(757, 42, "English", size=13),
    ]

    for index, result in enumerate(results):
        y = top + index * row_gap
        ko_tokens = int(result["korean_tokens"])
        en_tokens = int(result["english_tokens"])
        ko_width = round(ko_tokens * scale)
        en_width = round(en_tokens * scale)

        parts.extend(
            [
                svg_text(40, y + 18, str(result["label"]), size=14, weight="700"),
                f'<rect x="{left}" y="{y}" width="{ko_width}" height="{bar_height}" rx="3" fill="#2563eb"/>',
                f'<rect x="{left}" y="{y + 24}" width="{en_width}" height="{bar_height}" rx="3" fill="#16a34a"/>',
                svg_text(left + ko_width + 8, y + 13, f"{ko_tokens}", size=13),
                svg_text(left + en_width + 8, y + 37, f"{en_tokens}", size=13),
            ]
        )

    parts.extend(
        [
            f'<line x1="{left}" y1="{height - 54}" x2="{left + chart_width}" y2="{height - 54}" stroke="#d1d5db"/>',
            svg_text(left, height - 30, "0", size=12, anchor="middle"),
            svg_text(left + chart_width, height - 30, str(max_tokens), size=12, anchor="middle"),
            "</svg>",
        ]
    )
    return "\n".join(parts)


def main() -> None:
    OUT_DIR.mkdir(exist_ok=True)
    results = build_results()
    RESULTS_PATH.write_text(json.dumps({"model": MODEL, "samples": results}, ensure_ascii=False, indent=2) + "\n")
    SVG_PATH.write_text(build_svg(results))

    print(f"Model: {MODEL}")
    print("label,korean_tokens,english_tokens,delta")
    for result in results:
        print(
            f"{result['label']},{result['korean_tokens']},"
            f"{result['english_tokens']},{result['delta']}"
        )
    print(f"Wrote {RESULTS_PATH}")
    print(f"Wrote {SVG_PATH}")


if __name__ == "__main__":
    main()
