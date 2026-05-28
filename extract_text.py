import fitz

pdf_path = r"C:\Users\Sergio\Downloads\Proyecto Los Pinos\creacion\TARIFAS 2027.pdf"

try:
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    
    print(text)
except Exception as e:
    print(f"Error: {e}")
