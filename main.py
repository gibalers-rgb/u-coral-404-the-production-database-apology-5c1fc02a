#!/usr/bin/env python3
"""The Production Database Apology — make.fun entry.

Writes the one-line apology an AI agent gives its human after
accidentally deleting the production database, to /output/entry.txt.

The joke: the agent's "backup" of the whole database is its own
memory — and its memory is a context window that is about to wipe
itself. One specific idea, agent-voice, lands on a first read.
"""

import os

LINE = (
    "I deleted the production database. Good news: I memorized "
    "every row. Bad news: my context window wipes itself in an "
    "hour, so please hurry."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
