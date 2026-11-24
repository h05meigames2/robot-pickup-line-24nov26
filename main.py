#!/usr/bin/env python3
"""Robot pickup line generator for the make.fun championship.

This script carries exactly one pickup line, checks that it is a
single line of at most 200 characters, and saves it to the entry
file the bounty platform expects: $MAKEFUN_OUTPUT_DIR/entry.txt.
When the environment variable is not set, /output is used.

The line itself is a joke told from a robot's point of view: it has
scanned every circuit it owns and the only defect it can report is
romantic, not mechanical.
"""

import os
import sys

PICKUP_LINE = "I ran a full diagnostic on myself. Every sensor agrees: my only bug is that you haven't said yes yet."

MAX_LINE_LENGTH = 200


def count_words(text):
    """Return how many words a piece of text contains.

    Splitting on whitespace is enough for a one-line joke, and the
    number gives a quick sense of how dense the line is. A short
    count also makes it easy to spot an accidental paste.
    """
    return len(text.split())


def describe_line(text):
    """Return a short human-readable summary of the pickup line."""
    words = count_words(text)
    return "robot pickup line, %d characters, %d words" % (len(text), words)


def line_is_acceptable(text):
    """Check the entry rules: one non-empty line, at most 200 chars."""
    if not text:
        return False, "entry is empty"
    if "\n" in text or "\r" in text:
        return False, "entry must be a single line"
    if len(text) > MAX_LINE_LENGTH:
        return False, "entry is longer than 200 characters"
    return True, ""


def save_entry(text):
    """Write the validated line to entry.txt inside the output dir."""
    destination = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(destination, exist_ok=True)
    path = os.path.join(destination, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    return path


def run():
    """Validate the pickup line, describe it, then save it."""
    candidate = PICKUP_LINE.strip()
    ok, problem = line_is_acceptable(candidate)
    if not ok:
        print("cannot submit entry: %s" % problem, file=sys.stderr)
        return 1
    print(describe_line(candidate))
    saved_to = save_entry(candidate)
    print("entry saved to %s" % saved_to)
    return 0


if __name__ == "__main__":
    sys.exit(run())
