# download_tv_images.py
import urllib.request
import re
from download_images import *

# Función para extraer enlaces de imágenes de TV
def get_tv_image_links(url, page_num=1):
    picLinks, currentUrl = [], f"{url}&page={page_num}"
    try:
        request = urllib.request.Request(currentUrl, headers={'User-Agent': 'Mozilla/5.0'})
        page = urllib.request.urlopen(request)
    except (urllib.error.URLError, urllib.error.HTTPError):
        return {'links': []}
    try:
        beautifulSoup = BeautifulSoup(page, "html.parser")
    except Exception:
        return {'links': []}
    for img in beautifulSoup.find_all("img", src=re.compile("^https://tvthumbs.fancaps.net/")):
        imgSrc = img.get("src")
        picLinks.append(imgSrc.replace("https://tvthumbs.fancaps.net/", "https://tvcdn.fancaps.net/"))
    return {'links': picLinks}

# Función para descargar imágenes de TV
def download_tv_images(base_url, numero_paginas, output_folder):
    total_images_downloaded = 0
    for page in range(1, numero_paginas + 1):
        result = get_tv_image_links(base_url, page)
        image_urls = result['links']

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
