#!/usr/bin/env python3
"""AIGC watermark cleanup v3 - handles repeated/multiple injections.

Patterns removed:
1. YAML frontmatter blocks containing AIGC: field (may appear multiple times)
2. Inline AIGC injection blocks (standalone ---\nAIGC:\n...\n---)
3. Isolated standalone --- lines (orphan delimiters from removed blocks)
4. Trailing "> AI生成" or "> AI鐢熣垚" lines
5. Garbled AIGC text inside JS arrays/objects (AI鐢熣垚 patterns)
"""

import re
import sys
import glob
import os


def strip_watermark(content: str) -> str:
    """Remove all AIGC watermark patterns from content."""

    # 1. Remove all AIGC YAML frontmatter blocks (may appear multiple times)
    #    Pattern: ---\nAIGC:\n  field: value\n...\n---
    #    Also handles cases where --- on same line as last field
    content = re.sub(
        r"---\s*\nAIGC:\s*\n(?:  \S+:\s*.*\n)*---\s*\n?",
        "",
        content,
        flags=re.MULTILINE,
    )

    # 2. Remove isolated standalone --- lines (orphan delimiters from removed blocks)
    #    Only if they appear at start of line with nothing else on that line
    #    Be careful not to remove valid markdown horizontal rules (--- with blank lines around them)
    #    or table delimiters (|---|---|)
    #    Target: lines that are just --- and are NOT part of a valid structure
    #    Remove leading consecutive --- lines (before any real content)
    content = re.sub(r"^(?:---\s*\n)+", "", content)

    # 3. Remove trailing "> AI生成" or garbled variants
    #    Variants: > AI生成, > AI鐢熣垚, > AI鐢熣
    content = re.sub(r"\n{0,3}>\s*AI[\u751f\u0fd0\u780f\u0f97\u0f7a\u0f58\u0f66\u0f90\u0f91\u0f44\u0f62\u0f5b\u0f5e\u0f53\u0f7c\u0f42\u0f49\u0f4b\u0f4d\u0f5d\u0f4c\u0f51\u0f54\u0f7a\u0f63\u0f5f]*[成\u0fd0\u780f\u0f97\u0f7a\u0f58\u0f66\u0f90\u0f91\u0f44\u0f62\u0f5b\u0f5e\u0f53\u0f7c\u0f42\u0f49\u0f4b\u0f4d\u0f5d\u0f4c\u0f51\u0f54\u0f7a\u0f63\u0f5f]*\s*\n?",
        "\n",
        content,
    )

    # 4. Remove garbled AIGC text inside JS/JSON content
    #    Pattern: strings containing "AI\u751f\u6210" or "AI鐢熣垚"
    content = re.sub(r'["\']?AI鐢熣垚["\']?', '', content)
    content = re.sub(r'AI\u751f\u6210', '', content)

    # 5. Clean up excessive blank lines at start of file (max 1)
    content = re.sub(r"^\n{2,}", "", content)
    
    # 6. Clean up excessive blank lines at end of file (ensure single trailing newline)
    content = re.sub(r"\n{3,}$", "\n", content)

    return content


def main():
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    files = glob.glob(os.path.join(target_dir, "**/*.md"), recursive=True)

    cleaned = 0
    for f in files:
        if ".git" in f:
            continue
        if ".fetch-cache" in f:
            continue
        if ".fetch-cache-new" in f:
            continue
        with open(f, "r", encoding="utf-8") as fh:
            original = fh.read()
        result = strip_watermark(original)
        if result != original:
            with open(f, "w", encoding="utf-8") as fh:
                fh.write(result)
            cleaned += 1
            print(f"  cleaned: {f}")

    print(f"Done. {cleaned} file(s) cleaned.")


if __name__ == "__main__":
    main()
