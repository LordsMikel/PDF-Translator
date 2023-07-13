# PDF Translator

Este proyecto es un script en Python que permite traducir el texto de un archivo PDF (ESCANEADO) de portugués a español utilizando OCR (Reconocimiento Óptico de Caracteres) y la API de traducción de Google.

## Requisitos

- Python 3.x
- pytesseract
- googletrans
- pdf2image
- reportlab

Asegúrate de tener instalado Python 3.x en tu sistema. Puedes verificar la versión de Python instalada ejecutando el siguiente comando en tu terminal:

python --version

Si no tienes Python 3.x instalado, puedes descargarlo desde el sitio web oficial de Python: https://www.python.org/downloads/

Para instalar las bibliotecas requeridas, puedes utilizar el administrador de paquetes de Python llamado pip. Ejecuta los siguientes comandos en tu terminal para instalar las bibliotecas necesarias:

pip install pytesseract
pip install googletrans
pip install pdf2image
pip install reportlab

Además, asegúrate de tener el modelo de idioma adecuado para el OCR con Tesseract. Puedes seguir las instrucciones en la documentación oficial de Tesseract para descargar e instalar el modelo de idioma para portugués: https://github.com/tesseract-ocr/tesseract

## Uso

1. Coloca el archivo PDF que deseas traducir en la carpeta del proyecto.

2. Abre una terminal y navega al directorio del proyecto:

cd pdf-translator

3. Ejecuta el script y sigue las instrucciones en pantalla:
´´´bash
python traductor.py
´´´
4. Elige la página inicial y final del PDF que deseas traducir.

5. Espera a que se realice el proceso de OCR y traducción.

6. Introduce el nombre del archivo de salida para guardar el texto traducido en un nuevo documento PDF.

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún problema o tienes alguna mejora, no dudes en crear un issue o enviar un pull request.

## Licencia

Este proyecto se encuentra bajo la Licencia MIT.
