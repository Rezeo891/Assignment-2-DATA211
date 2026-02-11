# Q8 - Extract h2 headings from Wikipedia

import requests
from bs4 import BeautifulSoup

EXCLUDED = {"references", "external links", "see also", "notes"}

def main():
    url = "https://en.wikipedia.org/wiki/Data_science"
    resp = requests.get(url, timeout=20, headers={"User-Agent": "Mozilla/5.0"})
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    content = soup.find("div", id="mw-content-text")
    if content is None:
        raise RuntimeError("Could not find div#mw-content-text")

    headings = []
    for h2 in content.find_all("h2"):
        txt = h2.get_text(" ", strip=True).replace("[edit]", "").strip()
        lower = txt.lower()
        if any(bad in lower for bad in EXCLUDED):
            continue
        if txt:
            headings.append(txt)

    with open("headings.txt", "w", encoding="utf-8") as f:
        for h in headings:
            f.write(h + "\n")

    print(f"Saved {len(headings)} headings to headings.txt")

if __name__ == "__main__":
    main()