# Q3 - Near-duplicate line sets (sample-file.txt)

import re

def normalize_line(line: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", line.lower())

def main():
    groups: dict[str, list[tuple[int, str]]] = {}

    with open("sample-file.txt", "r", encoding="utf-8", errors="ignore") as f:
        for line_no, line in enumerate(f, start=1):
            original = line.rstrip("\n")
            key = normalize_line(original)
            if key:  # ignore lines that normalize to empty
                groups.setdefault(key, []).append((line_no, original))

    dup_sets = [v for v in groups.values() if len(v) >= 2]

    print(f"Number of near-duplicate sets: {len(dup_sets)}")

    for i, group in enumerate(dup_sets[:2], start=1):
        print(f"\nSet {i}:")
        for line_no, text in group:
            print(f"{line_no}: {text}")

if __name__ == "__main__":
    main()