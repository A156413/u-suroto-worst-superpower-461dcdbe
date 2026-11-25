#!/usr/bin/env python3
"""Worst Superpower entry for make.fun competition
u-suroto-worst-superpower-461dcdbe.

Program contract (program/v1): write exactly one line, at most
140 characters, to /output/entry.txt. Pure stdlib.
Final entry verified locally: 121 chars, 1 line, no trailing newline.
"""

import os

# Candidate lines drafted for the judge's brief:
#   A: "I can stop time for exactly one second, once in my life - and I already wasted it on a sneeze."
#   B: "I can hear the thoughts of any pigeon, but only while it is asleep, and pigeons dream in static."
#   C: "I can predict yesterday's lottery numbers with 100% accuracy, every single time, without fail."
#
# A wins, revised for a tighter, more pictured payoff: the one second
# is spent mid-sneeze into breakfast, a concrete image the reader
# sees at once. "Freeze" is punchier than "stop", and "this morning"
# puts the waste in the immediate past.
ENTRY = "I can freeze time for exactly one second, once in my life - and I already spent it this morning, sneezing into my cereal."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 140, f"entry length {len(text)} out of range"
    assert text == text.strip() and "\n" not in text
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
