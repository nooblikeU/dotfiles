#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import os
import sys
import io
from PIL import Image
from urllib.parse import urljoin, urlparse
from multiprocessing.pool import Pool
import multiprocessing as multi
from timer import timer

URL = sys.argv[1]
PATH = "/home/john/Pictures"

def s(URL, PATH):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

    r = requests.get(URL, headers=headers, stream=True)
    s = BeautifulSoup(r.content, 'html.parser')
    imgs = s.find_all("img")
    count = 0
    if r.status_code == 200:
        for img in imgs:
            img_url = img.attrs.get("src")
            if '_d' not in img_url:
                filename = img_url.split("/")[-1]
                if filename[-3:] == "png" or filename[-4:] == "jpeg":
                    img_url = urljoin(URL, img_url)
                   # print(img_url)
                    savefile = os.path.join(PATH, filename)
                    if not os.path.isfile(savefile):
                        r = requests.get(img_url, headers=headers, stream=True)
                        r.raw.decode_content = True
                        im = Image.open(io.BytesIO(r.content)).convert("RGB")
                        im.save(savefile)
                        count += 1 
                        print('Downloading:', filename)
                    else:
                        print(filename, 'is already exists skipping download')
    print(f"{count} Image downloaded!")
    print('Download Completed!')

@timer(1, 1)
def main():
    n_cores = multi.cpu_count()
    with Pool(n_cores) as pool:
        pool.starmap(s, [(URL, PATH)])
