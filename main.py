#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line -- an alien tourist's review of planet Earth --
to /output/entry.txt, as the competition gate requires (UTF-8, 1-200 chars).
"""

import os

ENTRY = (
    "The locals stare at glowing rectangles all day, then pay strangers "
    "to remind them to go outside. Lovely planet. 4/5 stars \u2014 would "
    "visit again, briefly."
)


def main() -> None:
    # Gate self-check: the scorer requires 1-200 characters, not only
    # whitespace. Fail loudly here rather than shipping an invalid entry.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
