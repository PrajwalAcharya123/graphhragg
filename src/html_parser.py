# src/html_parser.py
from bs4 import BeautifulSoup

def clean_and_structure_html(raw_html, output_path):
    soup = BeautifulSoup(raw_html, "html.parser")

    # ❌ Remove CSS
    for tag in soup(["style", "link"]):
        tag.decompose()

    for tag in soup.find_all(True):
        tag.attrs.pop("style", None)

    # 🔹 Structure conversion
    for div in soup.find_all("div"):
        text = div.get_text(strip=True)

        if not text:
            div.decompose()
            continue

        if len(text) < 60 and text.isupper():
            div.name = "h2"
        elif ":" in text:
            div.name = "p"
        else:
            div.name = "p"

    structured_html = str(soup)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(structured_html)

    print(f"✅ Structured HTML saved: {output_path}")

    return structured_html