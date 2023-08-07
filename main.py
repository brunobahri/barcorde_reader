import os
from pdf2image import convert_from_path
from pyzbar.pyzbar import decode

def extract_barcode_from_image(image):
    barcodes = decode(image)
    if barcodes:
        return barcodes[0].data.decode('utf-8')
    return None

def convert_from_path_with_custom_poppler(pdf_path, poppler_path):
    images = convert_from_path(pdf_path, poppler_path=poppler_path)
    return images

def extract_barcode_from_pdf(pdf_path):
    poppler_path = r"D:\\poppler\\Library\\bin"  # Substitua pelo caminho correto
    images = convert_from_path_with_custom_poppler(pdf_path, poppler_path)
    for image in images:
        barcode = extract_barcode_from_image(image)
        if barcode:
            return barcode
    return None

def process_pdfs_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.pdf'):
            pdf_path = os.path.join(folder_path, filename)
            barcode = extract_barcode_from_pdf(pdf_path)

            if barcode:
                print(f"Barcode found in '{filename}': {barcode}")
            else:
                print(f"No barcode found in '{filename}'.")

if __name__ == "__main__":
    folder_path = "pdf"
    process_pdfs_in_folder(folder_path)
