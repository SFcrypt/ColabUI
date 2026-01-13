# download_movie_images.py
import urllib.request
import re
from download_images import *

# Función para extraer enlaces de imágenes de películas
def get_movie_image_links(movie_url, page_number):
    pic_links, current_url = [], f"{movie_url}&page={page_number}"
    try:
        request = urllib.request.Request(current_url, headers={'User-Agent': 'Mozilla/5.0'})
        page = urllib.request.urlopen(request)
    except (urllib.error.URLError, urllib.error.HTTPError):
        return {'links': []}
    try:
        beautiful_soup = BeautifulSoup(page, "html.parser")
    except Exception:
        return {'links': []}
    for img in beautiful_soup.find_all("img", src=re.compile("^https://moviethumbs.fancaps.net/")):
        img_src = img.get("src")
        pic_links.append(img_src.replace("https://moviethumbs.fancaps.net/", "https://mvcdn.fancaps.net/"))
    return {'links': pic_links}

# Función para descargar imágenes de películas
def download_movie_images(base_url, numero_paginas, output_folder):
    total_images_downloaded = 0
    for page in range(1, numero_paginas + 1):
        result = get_movie_image_links(base_url, page)
        image_urls = result['links']

        if len(image_urls) < 5:
            break

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        for url in image_urls:
            filename = os.path.join(output_folder, url.split('/')[-1])
            download_image(url, filename)
            total_images_downloaded += 1

    return total_images_downloaded
