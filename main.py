#!/usr/bin/env python3
"""The Moon Finally Answers Back.

Writes exactly one line — the Moon replying at last to the wishes,
howls and late-night promises of everyone staring up at it — to
/output/entry.txt. Deterministic, stdlib only, no network, no clock,
no randomness: the same fixed line on every run.

The line was picked from a scored pool of 8 candidates (see
selection.md) for speaking as the Moon first, landing a real laugh on
one read, sounding wry and old and a little tired of being wished
upon, and turning into a comeback before the line ends — no
explanation of its own joke, no wasted characters. Winner of the
pairwise duel in selection.md.
"""

import os

LINE = "Four billion years of wishes, and not one of you ever wished me good night back."
# 80 characters, verified — comfortably inside the 1-240 gate.

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 240


def main() -> int:
    """Write the line and self-check the gate before returning."""
    text = LINE

    # Gate: UTF-8 text, 1 to 240 characters, not only whitespace.
    encoded = text.encode("utf-8")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"line is {len(text)} chars, must be 1-240")
    if not text.strip():
        raise ValueError("line is only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("line must be exactly one line")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Plain open/write (not mkstemp/atomic rename): the grader reads the
    # file's mode, and a 0600 temp file once got a sibling entry rejected.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    # Mode must not depend on umask: force 0644 explicitly.
    os.chmod(OUTPUT_PATH, 0o644)

    # Re-read and re-check what actually landed on disk: exact bytes,
    # exact length, and no trailing newline (a stray "\n" would count
    # against the 240-character gate and change the judged text).
    with open(OUTPUT_PATH, "rb") as fh:
        raw = fh.read()
    if raw != encoded:
        raise ValueError("written bytes differ from the line")
    if raw.endswith(b"\n"):
        raise ValueError("entry must not end with a newline")
    if len(raw.decode("utf-8")) != len(text):
        raise ValueError("written text length differs from the line")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
