import pdfplumber, json
from heading_detector import classify_heading

def extract_outline(pdf_path):
    outline, title = [], None
    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            for char in page.extract_words(extra_attrs=["size"]):
                level = classify_heading(char['size'])
                if level:
                    outline.append({
                        "level": level,
                        "text": char['text'],
                        "page": page_number
                    })
                    if not title and level == "H1":
                        title = char['text']
    return {"title": title or "Untitled", "outline": outline}

if __name__ == "__main__":
    import sys
    result = extract_outline("input.pdf")
    with open("outline.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print("✅ Outline written to outline .json")
    
