#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint — make.fun entry.

Writes one two-part micro-confession to /output/entry.txt: a To: line
naming who it was meant for, and the unsent message itself, one line
written exactly as it was typed.

Deterministic: the same text on every run. No network, no secrets,
no randomness, no input read from anywhere.
"""

import os

# The confession, in exactly two parts: the To: line naming who it was
# meant for, and the unsent message itself, one line as it was typed.
# Total 123 characters (gate: 1-260); message 106 characters (at most 200).
TO_LINE = "To: my neighbour"
MESSAGE = (
    "i was the one who broke your window in 2009. "
    "i've walked past your house for fifteen years rehearsing this"
)
ENTRY = TO_LINE + "\n" + MESSAGE + "\n"


def main() -> None:
    # Fail loudly instead of handing the gate a bad file.
    text = ENTRY
    assert text.strip(), "entry must not be only white space"
    assert 1 <= len(text) <= 260, "entry must be 1-260 characters"
    assert len(MESSAGE) <= 200, "message must be at most 200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
