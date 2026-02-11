# Q1 - Top 10 word frequencies (sample-file.txt)

from collections import Counter

PUNCT_STRIP = ".,;:!?\"'`()[]{}<>/\\|-*_~"

def clean_tokens(filename: str) -> list[str]:
    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()

    tokens = []
    for raw in text.split():
        tok = raw.lower().strip(PUNCT_STRIP)
        if tok and sum(ch.isalpha() for ch in tok) >= 2:
            tokens.append(tok)
    return tokens

def main():
    tokens = clean_tokens("sample-file.txt")
    counts = Counter(tokens)
    for word, c in counts.most_common(10):
        print(f"{word} -> {c}")

if __name__ == "__main__":
    main()
