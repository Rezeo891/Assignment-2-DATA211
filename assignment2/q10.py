# Q10 - Reusable function to find lines containing a keyword (case-insensitive)

def find_lines_containing(filename, keyword):
    """
    Returns a list of (line_number, line_text) for lines that contain keyword
    (case-insensitive). Line numbers start at 1.
    """
    out = []
    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        for line_no, line in enumerate(f, start=1):
            if keyword.lower() in line.lower():
                out.append((line_no, line.rstrip("\n")))
    return out

def main():
    matches = find_lines_containing("sample-file.txt", "lorem")
    print(f"Matching lines found: {len(matches)}")
    for line_no, text in matches[:3]:
        print(f"{line_no}: {text}")

if __name__ == "__main__":
    main()
