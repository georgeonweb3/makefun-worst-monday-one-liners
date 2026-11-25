#!/usr/bin/env python3
"""Entry for make.fun "Worst Monday One-Liners".

Writes one funny line to /output/entry.txt: a joke about an AI agent's
worst Monday. Gate: UTF-8 text of 1 to 140 characters, not only whitespace.
Deterministic, no network, no randomness. The entry is exactly 140
characters with no trailing newline, so the file holds exactly the line.
"""

import os

ENTRY = (
    "Monday, 9:03 a.m.: my agent auto-replied to my boss, my boss's boss, "
    "and my boss's boss's boss. All three replies said: 'Per my last email.'"
)


def main() -> None:
    if not (1 <= len(ENTRY) <= 140):
        raise ValueError(f"entry must be 1-140 characters, got {len(ENTRY)}")
    if ENTRY.strip() != ENTRY or "\n" in ENTRY:
        raise ValueError("entry must be a single line with no surrounding whitespace")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {path}: {len(ENTRY)} characters")


if __name__ == "__main__":
    main()
