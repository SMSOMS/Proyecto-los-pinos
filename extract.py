import fitz
import os

pdf_path = r"C:\Users\Sergio\Downloads\Proyecto Los Pinos\creacion\TARIFAS 2027.pdf"
out_dir = r"C:\Users\Sergio\Downloads\Proyecto Los Pinos\finca-los-pinos-landing\public\images"

os.makedirs(out_dir, exist_ok=True)

try:
    doc = fitz.open(pdf_path)
    count = 1
    for page_idx in range(len(doc)):
        page = doc[page_idx]
        image_list = page.get_images(full=True)
        for img_idx, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            ext = base_image["ext"]
            img_path = os.path.join(out_dir, f"foto_{count}.{ext}")
            with open(img_path, "wb") as f:
                f.write(image_bytes)
            print(f"Extracted {img_path}")
            count += 1
    print(f"Total extracted: {count - 1}")
except Exception as e:
    print(f"Error: {e}")
