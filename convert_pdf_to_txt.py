from pypdf import PdfReader
import os

pdf_path = '/Users/shivam/Documents/GenAI/kundali/vedic_astro_textbook.pdf'
txt_path = '/Users/shivam/Documents/GenAI/kundali/vedic_astro_textbook.txt'

try:
    reader = PdfReader(pdf_path)
    print(f"Number of pages: {len(reader.pages)}")
    
    with open(txt_path, 'w', encoding='utf-8') as f:
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            f.write(f"--- Page {i+1} ---\n")
            f.write(text)
            f.write("\n\n")
            
    print(f"Successfully converted {pdf_path} to {txt_path}")

except Exception as e:
    print(f"Error converting PDF: {e}")
