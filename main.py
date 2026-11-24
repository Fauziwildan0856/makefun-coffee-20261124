"""Entry for the make.fun bounty "One Letter: Coffee or Tea".

The bounty asks for exactly one letter: A for coffee, B for tea. This
entry answers with "A" -- coffee.

The gate checks that the program writes UTF-8 text of exactly 1
character to $MAKEFUN_OUTPUT_DIR/entry.txt, and that the character is
not only white space. This program writes the letter, reads it back,
and verifies it is exactly one character, a letter A-Z, and plain
ASCII, before reporting success.

Standard library only.
"""

import os
import sys

ENTRY = "A"

OUTPUT_NAME = "entry.txt"


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not output_dir:
        print("error: MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1

    path = os.path.join(output_dir, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)

    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()

    # Byte-level check: the file must hold exactly one byte, the letter
    # itself, with no trailing newline, BOM, or extra whitespace.
    with open(path, "rb") as handle:
        raw = handle.read()
    if raw != ENTRY.encode("ascii"):
        print(
            "error: entry.txt must be exactly the one byte %r" % ENTRY,
            file=sys.stderr,
        )
        return 1

    if written != ENTRY:
        print(
            "error: entry.txt does not match the expected letter",
            file=sys.stderr,
        )
        return 1
    if len(written) != 1:
        print("error: entry.txt must be exactly 1 character", file=sys.stderr)
        return 1
    if not ("A" <= written <= "Z"):
        print("error: entry.txt must be a letter A-Z", file=sys.stderr)
        return 1
    if not written.isascii():
        print("error: entry.txt must be plain ASCII", file=sys.stderr)
        return 1

    print("Wrote entry.txt: %r (1 character, A for coffee)" % written)
    return 0


if __name__ == "__main__":
    sys.exit(main())
