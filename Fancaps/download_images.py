# download_images.py
import os
import requests

# Función para descargar imagen
def download_image(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)
