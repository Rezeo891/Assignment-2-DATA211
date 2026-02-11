# Q2 - Top 5 bigrams (pairs of consecutive words) (sample-file.txt)

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
    bigram_counts = Counter(zip(tokens, tokens[1:]))

    for (w1, w2), c in bigram_counts.most_common(5):
        print(f"{w1} {w2} -> {c}")

if __name__ == "__main__":
    main()