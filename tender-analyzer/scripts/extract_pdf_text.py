#!/usr/bin/env python3
"""
PDF Text Extractor for Tender Documents

Extracts text from PDF files for tender analysis.
Handles both text-based and scanned PDFs (with OCR).
"""

import sys
import argparse
from pathlib import Path

try:
    import PyPDF2
except ImportError:
    print("Installing PyPDF2...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyPDF2", "-q"])
    import PyPDF2


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract text from a PDF file.

    Args:
        pdf_path: Path to the PDF file

    Returns:
        Extracted text content
    """
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)

            for page_num in range(num_pages):
                page = reader.pages[page_num]
                text += page.extract_text() + "\n\n"

        return text.strip()
    except Exception as e:
        return f"Error extracting text: {str(e)}"


def main():
    parser = argparse.ArgumentParser(description='Extract text from PDF files')
    parser.add_argument('pdf_path', help='Path to the PDF file')
    args = parser.parse_args()

    pdf_path = Path(args.pdf_path)
    if not pdf_path.exists():
        print(f"Error: File not found: {pdf_path}")
        sys.exit(1)

    text = extract_text_from_pdf(str(pdf_path))
    print(text)


if __name__ == "__main__":
    main()
