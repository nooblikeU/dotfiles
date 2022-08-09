#import io
import requests
import shutil
from bs4 import BeautifulSoup
import os,sys
#from PIL import Image
from urllib.parse import urljoin, urlparse
from multiprocessing import Process
from timer import timer

def s():
    path = "/home/john/.scripts/thread/img"
    url = sys.argv[1]
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

    r = requests.get(url, headers=headers, stream=True)
    s = BeautifulSoup(r.content, 'html.parser')
    imgs = s.find_all("img")
    if r.status_code == 200:
        for img in imgs:
            img_url = img.attrs.get("src")
            if '_d' not in img_url:
                filename = img_url.split("/")[-1]
                if filename[-3:] == "png" or filename[-4:] == "jpeg":
                    img_url = urljoin(url, img_url)
                   # print(img_url)
                    savefile = os.path.join(path, filename)
                    if not os.path.isfile(savefile):
                        r = requests.get(img_url, headers=headers, stream=True)
                        r.raw.decode_content = True
                        with open(savefile, 'wb') as f:
                            shutil.copyfileobj(r.raw, f)
                            print('Downloading', filename)
                        #print("Failed to write image")
                    else:
                        print(filename, 'is already exists skipping download')
    else:
        print("ERROR")

    #print('Download Completed!')

@timer(1, 1)
def main():
    p = Process(target=s)
    p.start()
    p.join()
