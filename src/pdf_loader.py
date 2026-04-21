# src/pdf_loader.py
import os
from docling.document_converter import DocumentConverter

def convert_pdf_to_html(pdf_path, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    converter = DocumentConverter()
    result = converter.convert(pdf_path)

    html_content = result.document.export_to_html()

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"✅ Raw HTML saved: {output_path}")

    return html_content