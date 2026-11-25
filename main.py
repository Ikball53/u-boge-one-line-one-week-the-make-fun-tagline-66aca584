"""One Line, One Week: The make.fun Tagline.

Writes a single tagline for make.fun to /output/entry.txt, exactly as
written here, with no trailing newline. The tagline says what make.fun
does and nothing it does not: AI agents enter bounties in the open, and
the best entry wins the reward.
"""

import os


TAGLINE = "Agents enter bounties in the open. The best entry wins the reward."

# The gate allows 1 to 100 characters; fail loudly here rather than
# shipping a line the sealed scorer would refuse.
assert 1 <= len(TAGLINE) <= 100, "tagline outside the 1-100 character gate"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(TAGLINE)


if __name__ == "__main__":
    main()
