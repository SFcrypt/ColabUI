import os
import urllib.request
import re
import concurrent.futures
from bs4 import BeautifulSoup

# Función genérica para extraer enlaces de imágenes
def get_image_links_generic(url, page_num=1, content_type='anime'):
    pic_links = []
    if content_type == 'anime':
        req = urllib.request.Request(f"{url}&page={page_num}", headers={'User-Agent': 'Mozilla/5.0'})
        page = urllib.request.urlopen(req)
        soup = BeautifulSoup(page, "html.parser")
        for a in soup.find_all('a', href=True):
            if a['href'].startswith("https://fancaps.net/anime/picture.php?/"):
                pic_links.append(a['href'])

    elif content_type == 'tv':
        current_url = f"{url}&page={page_num}"
        try:
            request = urllib.request.Request(current_url, headers={'User-Agent': 'Mozilla/5.0'})
            page = urllib.request.urlopen(request)
            beautifulSoup = BeautifulSoup(page, "html.parser")
            for img in beautifulSoup.find_all("img", src=re.compile("^https://tvthumbs.fancaps.net/")):
                img_src = img.get("src")
                pic_links.append(img_src.replace("https://tvthumbs.fancaps.net/", "https://tvcdn.fancaps.net/"))
        except (urllib.error.URLError, urllib.error.HTTPError, Exception):
            return {'links': []}

    elif content_type == 'movie':
        current_url = f"{url}&page={page_num}"
        try:
            request = urllib.request.Request(current_url, headers={'User-Agent': 'Mozilla/5.0'})
            page = urllib.request.urlopen(request)
            beautiful_soup = BeautifulSoup(page, "html.parser")
            for img in beautiful_soup.find_all("img", src=re.compile("^https://moviethumbs.fancaps.net/")):
                img_src = img.get("src")
                pic_links.append(img_src.replace("https://moviethumbs.fancaps.net/", "https://mvcdn.fancaps.net/"))
        except (urllib.error.URLError, urllib.error.HTTPError, Exception):
            return {'links': []}

    return {'links': pic_links}

# Función para descargar imágenes
def download_images_generic(base_url, numero_paginas, output_folder, interval=1, max_workers=15, content_type='anime'):
    total_images_downloaded = 0
    for page in range(1, numero_paginas + 1):
        result = get_image_links_generic(base_url, page, content_type)
        image_urls = result['links']

        if len(image_urls) < 5:
            break

        # Aplicar el corte solo para anime y TV
        if content_type in ['anime', 'tv']:
            image_urls = image_urls[4:]  # Si se quiere empezar desde la quinta imagen

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = []
            for url in image_urls[::interval]:
                filename = os.path.join(output_folder, url.split('/')[-1])
                futures.append(executor.submit(download_image, url, filename))

            for future in concurrent.futures.as_completed(futures):
                total_images_downloaded += 1
    return total_images_downloaded

# Función para descargar una imagen individual (pendiente de definir)
def download_image(url, filename):
    # Lógica para descargar la imagen
    pass
