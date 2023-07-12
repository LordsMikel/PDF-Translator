import cv2
from PIL import Image
import pytesseract
from googletrans import Translator
from fpdf import FPDF
from pdf2image import convert_from_path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors

def convert_pdf_to_image(file, start_page, end_page):
    images = convert_from_path(file, first_page=start_page, last_page=end_page)
    return images

def ocr_core(image):
    text = pytesseract.image_to_string(image, lang='por')
    return text

def translate_text(text, src_lang, dest_lang):
    translator = Translator()
    try:
        translation = translator.translate(text, src=src_lang, dest=dest_lang)
        return translation.text
    except Exception as e:
        print(f"Error al traducir el texto: {e}")
        return None

def save_to_pdf(pages, output_file):
    c = canvas.Canvas(output_file, pagesize=letter)
    c.setFont("Helvetica", 12)
    y = 750  
    for page in pages:
        for line in page:
            if y < 50:
                c.showPage()  
                y = 750  
            c.drawString(100, y, line)
            y -= 15  
        y -= 20 
    c.save()

# Solicitar al usuario que introduzca el nombre del archivo PDF a traducir
file_name = input('Por favor, introduce el nombre del archivo PDF a traducir (debe estar en la misma carpeta que este script): ')
start_page = int(input('Por favor, introduce la página de inicio: '))
end_page = int(input('Por favor, introduce la página de fin: '))

# Asumir que el archivo está en la misma carpeta que el script
file_path = f"./{file_name}"

# Convertir el PDF en una imagen
images = convert_pdf_to_image(file_path, start_page, end_page)

# Traducir el texto por página de portugués a español
translated_pages = []
for image in images:
    extracted_text = ocr_core(image)
    translated_text = translate_text(extracted_text, 'pt', 'es') 
    
    if translated_text is not None:
        translated_lines = translated_text.split('\n')
        translated_pages.append(translated_lines)
    else:
        print("No se pudo traducir el texto de la imagen")

# Solicitar al usuario que introduzca el nombre del archivo de salida
output_file = input('Por favor, introduce el nombre del archivo de salida: ')

# Guardar el texto traducido en un nuevo documento PDF
save_to_pdf(translated_pages, output_file)
