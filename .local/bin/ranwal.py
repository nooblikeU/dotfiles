#!/usr/bin/python

import requests
import os
import time
from requests import ReadTimeout
from concurrent.futures import ThreadPoolExecutor

API_KEY = "FmchmmLXApTNJc9OeelPtGQ9NLmUkoac"


def init():
    #res = resolution()
    #ratio = ratios()
    keyword = search()
    category_code = get_category_code()
    purity_code = get_purity_code()
    global path
    path = "/home/john/.scripts/image"
    global BASE_URL
    BASE_URL = f"https://wallhaven.cc/api/v1/search?apikey={API_KEY}"+f"&q={keyword}"+f"&purity={category_code}"+f"&purity={purity_code}"+f"&page=1"
def search():
    query = input("Put the keyword you want search: ")
    return query


def resolution():
    res = input("Enter resolution: ").lower()
    while res not in ('720p', '1080p', '2160p'):
        print("Wrong resolution input")
        res = input("enter resolution: ").lower()
        print("\n")

    resolution_tags = {'720p': '1280x720', '1080p': '1920x1080', '2160p': '3840x2160'}
    resolution_code = resolution_tags[res]
    return resolution_code

def ratios():
    ratio = input("Enter ratio: ").lower()
    while ratio not in ('16:9', '21:9', 'all'):
        print('Wrong ratio input')
        ratio = input("Enter ratio: ").lower()
        print('\n')
    ratio_tags = {'16:9': '16x9', '21:9': '21x9', 'all': 'landscape'}
    ratio_code = ratio_tags[ratio]
    return ratio_code

def get_category_code():
    category_tags = {'all': '111', 'anime': '010', 'general': '100', 'people': '001', 'ga': '110', 'gp': '101'}

    category_code = category_tags['anime']

    return category_code

def get_purity_code():
    purity_tags = {'sfw': '100', 'sketchy': '010', 'nsfw': '001', 'ws': '110', 'wn': '101', 'sn': '011', 'all': '111'}

    purity_code = purity_tags['nsfw']

    return purity_code

def image_download(url):
    r = requests.get(url)
    filename = url.split("/")[-1]
    global path
    savefile = os.path.join(path, filename)
    if not os.path.exists(path):
        os.makedirs(path)
    try:
        if r.status_code == 200:
            content = r.content
            with open(savefile, 'wb') as f:
                f.write(content)
            print("Downloading: "+ filename)
        else:
            print("Failed to download ",filename , r.status_code)
            return None
    except (ConnectionError, ReadTimeout):
        print("Crawling Failed", url)
        return None

def get_page():
    start, end = map(int, input("Please enter the page range ('1,1', '1,2'): ").split(","))
    return start, end+1


def main():
    init()
    image = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    start_page, end_page = get_page()
    for page in range(start_page, end_page):
        global BASE_URL
        BASE_URL = BASE_URL[:-1]+f"{page}"
        print(BASE_URL, "is crawing")
        wall = requests.get(BASE_URL, headers=headers).json()["data"]
   #     for i in range(len(wall)):
   #         img = wall[i]["path"]
   #         image.append(img)

   # for imgs in image:
   #     image_download(imgs)
        
        
        with ThreadPoolExecutor(50) as t:
            for i in range(len(wall)):
                img = wall[i]["path"]
                t.submit(image_download, url=img)
                time.sleep(1)
                #image.append(wall["data"][i]["path"])
                #print(image)


         

    

    print(f"PAGE{page} IS OVER")
    print("All is done!")

if __name__ == "__main__":
    main()
