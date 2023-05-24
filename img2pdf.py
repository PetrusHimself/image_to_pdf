import img2pdf
from PyPDF2 import PdfFileWriter, PdfFileReader
from PIL import Image
import os

def image_to_pdf(image_path, output_path):
    with open(output_path, "wb") as pdf_file:
        image = Image.open(image_path)
        pdf_bytes = img2pdf.convert(image.filename)
        pdf_file.write(pdf_bytes)

def pdf_to_image(pdf_path, output_directory):
    with open(pdf_path, "rb") as pdf_file:
        pdf = PdfFileReader(pdf_file)
        for page_num in range(pdf.numPages):
            page = pdf.getPage(page_num)
            image = page.extract_images()[0]["image"]
            image_path = os.path.join(output_directory, f"page_{page_num+1}.png")
            with open(image_path, "wb") as image_file:
                image_file.write(image)

# Example usage
image_path = "input_image.jpg"
pdf_path = "output_pdf.pdf"
output_directory = "output_images"

# Convert image to PDF
image_to_pdf(image_path, pdf_path)
print("Image converted to PDF successfully!")

# Convert PDF to images
pdf_to_image(pdf_path, output_directory)
print("PDF converted to images successfully!")

