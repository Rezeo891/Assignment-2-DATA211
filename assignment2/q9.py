# Q9 - Extract first Wikipedia table (Machine learning page) and save to wiki_table.csv

import requests
from bs4 import BeautifulSoup
import pandas as pd

def main():
    url = "https://en.wikipedia.org/wiki/Machine_learning"
    resp = requests.get(url, timeout=20, headers={"User-Agent": "Mozilla/5.0"})
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    content = soup.find("div", id="mw-content-text")
    if content is None:
        raise RuntimeError("Could not find div#mw-content-text")

    target = None
    for tbl in content.find_all("table"):
        rows = tbl.find_all("tr")
        data_rows = [r for r in rows if r.find("td")]
        if len(data_rows) >= 3:
            target = tbl
            break

    if target is None:
        raise RuntimeError("No table found with at least 3 data rows")

    rows = target.find_all("tr")

    # Headers
    header_cells = rows[0].find_all("th")
    if header_cells:
        headers = [c.get_text(" ", strip=True) for c in header_cells]
    else:
        first_data = next(r for r in rows if r.find("td"))
        ncols = len(first_data.find_all(["td", "th"]))
        headers = [f"col{i+1}" for i in range(ncols)]

    data = []
    for r in rows:
        cells = r.find_all(["td", "th"])
        if not cells:
            continue
        if r is rows[0] and header_cells:
            continue  # skip header row

        vals = [c.get_text(" ", strip=True) for c in cells]
        if len(vals) < len(headers):
            vals += [""] * (len(headers) - len(vals))
        else:
            vals = vals[:len(headers)]

        if r.find("td") or not header_cells:
            data.append(vals)

    pd.DataFrame(data, columns=headers).to_csv("wiki_table.csv", index=False)
    print(f"Saved table with {len(data)} rows to wiki_table.csv")

if __name__ == "__main__":
    main()
