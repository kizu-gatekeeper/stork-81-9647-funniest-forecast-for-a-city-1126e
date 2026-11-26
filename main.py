"""Write this entry's one-line weather forecast for a city that is not real to entry.txt."""

import os

ENTRY = "Glimmer Falls: sunny with a 90 percent chance of raining frogs, so bring an umbrella and a very small net."

# Guard: the bounty gate requires the entry line to be 1..120 chars.
if not 1 <= len(ENTRY) <= 120:
    raise ValueError("ENTRY must be 1-120 chars")

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/tmp/out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
