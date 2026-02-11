# Q7 - Wikipedia scrape

import requests
from bs4 import BeautifulSoup

def main():
    url = "https://en.wikipedia.org/wiki/Data_science"
    resp = requests.get(url, timeout=20, headers={"User-Agent": "Mozilla/5.0"})
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")

    title = soup.title.get_text(strip=True) if soup.title else ""
    print(title)

    content = soup.find("div", id="mw-content-text")
    if content is None:
        raise RuntimeError("Could not find div#mw-content-text")

    for p in content.find_all("p"):
        txt = p.get_text(" ", strip=True)
        if len(txt) >= 50:
            print("\n" + txt)
            break

if __name__ == "__main__":
    main()