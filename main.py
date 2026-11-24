#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters.

Writes one loading-screen tip for stressed developers and AI coding
agents to /output/entry.txt. Standard library only (Python 3.13
sandbox installs nothing).
"""

import os

TIP = (
    "Tip: your agent isn't stuck \u2014 it's in a meeting with itself "
    "about whether to ask you or just guess. Spoiler: it guessed."
)


def main() -> None:
    # Enforce the bounty gate in code: 1-200 chars, one line, not blank.
    if not 1 <= len(TIP) <= 200:
        raise ValueError(f"tip must be 1-200 characters, got {len(TIP)}")
    if TIP != TIP.strip() or "\n" in TIP:
        raise ValueError("tip must be a single non-blank line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TIP + "\n")


if __name__ == "__main__":
    main()
