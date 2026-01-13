# download_anime_images.py
import urllib.request
from download_images import *
from bs4 import BeautifulSoup

# Función para extraer enlaces de imágenes de anime
def get_image_links(url):
    image_urls = []
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urllib.request.urlopen(req)
    soup = BeautifulSoup(page, "html.parser")
    for a in soup.find_all('a', href=True):
        if a['href'].startswith("https://fancaps.net/anime/picture.php?/"):
            image_urls.append(a['href'])
    return image_urls

# Función para descargar imágenes de anime
def download_anime_images(base_url, numero_paginas, output_folder):
    total_images_downloaded = 0
    for page in range(1, numero_paginas + 1):
        image_urls = get_image_links(base_url + f"&page={page}")
        
        if len(image_urls) < 5:
            break

        image_urls = image_urls[4:]
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        for url in image_urls:
            filename = os.path.join(output_folder, url.split('/')[-1])
            download_image(url, filename)
            total_images_downloaded += 1

    return total_images_downloaded
