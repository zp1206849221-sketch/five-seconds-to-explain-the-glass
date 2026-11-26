#!/usr/bin/env python3
"""Write the house cat's one-sentence defence to /output/entry.txt."""

import os

LINE = (
    "I gave that glass three tail-flick warnings and one hard stare "
    "for squatting in my sunbeam, so by cat law its eviction was entirely lawful."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
