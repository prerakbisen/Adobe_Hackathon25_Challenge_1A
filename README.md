# PDF Outline Extractor

This repository provides a lightweight Python-based tool to extract an outline (table of contents) from a PDF file by detecting headings based on font size. The extracted outline is saved as a JSON file.

---

## **Features**
- **Automatic Heading Detection:** Identifies headings (`H1`, `H2`, `H3`) based on font size thresholds.
- **PDF Parsing:** Uses [pdfplumber](https://github.com/jsvine/pdfplumber) to extract text and font sizes.
- **JSON Output:** Generates a structured `outline.json` containing the detected headings and page numbers.
- **Dockerized Execution:** Easily run in a container with no local setup required.

---

## **Repository Structure**
```
.
├── Dockerfile               # Docker build configuration
├── extract_outline.py       # Main script for PDF outline extraction
├── heading_detector.py      # Heading level classifier based on font size
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## **Installation & Usage**

### **1. Prerequisites**
- [Docker](https://docs.docker.com/get-docker/) installed on your machine.
- A PDF file you want to process (rename it to `input.pdf` or adjust the script accordingly).

---

### **2. Build the Docker Image**
From the project root, run:
```bash
docker build -t pdf-outline .
```

---

### **3. Run the Container**
Place your `input.pdf` in the project root. Then run:
```bash
docker run --rm -v ${PWD}:/app pdf-outline
```

- `${PWD}` mounts your current directory to `/app` inside the container.
- The script will process `input.pdf` and produce an `outline.json` file.

**For Windows PowerShell:**
```powershell
docker run --rm -v ${PWD}:/app pdf-outline
```

**For Windows CMD:**
```cmd
docker run --rm -v %cd%:/app pdf-outline
```

---

### **4. Output**
After running, you will see:
- `outline.json` in the same directory, containing a structure like:
```json
{
  "title": "Document Title",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "Background", "page": 2 },
    { "level": "H3", "text": "Details", "page": 3 }
  ]
}
```

---

## **Local Development (Without Docker)**

If you prefer running the script locally:

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the script:**
   ```bash
   python extract_outline.py
   ```

Make sure your `input.pdf` is in the same directory.

---

## **How It Works**
1. **`extract_outline.py`**:
   - Opens the PDF using `pdfplumber`.
   - Iterates through each page and word.
   - Calls `classify_heading(font_size)` to determine if a word is a heading.

2. **`heading_detector.py`**:
   - Defines font size thresholds for `H1`, `H2`, and `H3`.

---

## **Example Command**
```bash
docker build -t pdf-outline .
docker run --rm -v ${PWD}:/app pdf-outline
```

---


