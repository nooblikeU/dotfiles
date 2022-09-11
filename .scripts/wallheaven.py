#!/usr/bin/python

import requests
import os
from requests import ReadTimeout
from concurrent.futures import ThreadPoolExecutor

API_KEY = ""


def init():
    keyword = search()
    res = resolution()
    ratio = ratios()
    category_code = get_category_code()
    purity_code = get_purity_code()
    #topRange = toprange()
    sorting = sort()
    global path
    path = "/home/john/Pictures"
    global BASE_URL
    BASE_URL = f"https://wallhaven.cc/api/v1/search?apikey={API_KEY}"+f"&q={keyword}"+f"&purity={category_code}"+f"&purity={purity_code}"+f"&atleast={res}"+f"&ratios={ratio}"+f"&sorting={sorting}"+f"&page=1"
def search():
    query = input("Put the keyword you want search: ")
    return query


def resolution():
    res = input("Enter resolution: ").lower()
    while res not in ('720', '1080', '2160'):
        print("Wrong resolution input")
        res = input("Enter resolution: ").lower()

    resolution_tags = {'720': '1280x720', '1080': '1920x1080', '2160': '3840x2160'}
    resolution_code = resolution_tags[res]
    return resolution_code

def ratios():
    ratio = input("Enter ratio: ").lower()
    while ratio not in ('16x9', '21x9', 'all'):
        print('Wrong ratio input')
        ratio = input("Enter ratio: ").lower()
    ratio_tags = {'16x9': '16x9', '21x9': '21x9', 'all': 'landscape'}
    ratio_code = ratio_tags[ratio]
    return ratio_code

def get_category_code():
    category = input("Enter category name (all, anime, general, people, ga, gp): ").lower()
    while category not in ('all', 'anime', 'general', 'people', 'ga', 'gp'):
        print('Wrong category input')
        category = input("Enter category name (all, anime, general, people, ga, gp): ").lower()
    category_tags = {'all': '111', 'anime': '010', 'general': '100', 'people': '001', 'ga': '110', 'gp': '101'}

    category_code = category_tags[category]

    return category_code

def get_purity_code():
    purity = input("Enter purity name (sfw, sketchy, nsfw, ws, wn, sn, all): ")
    while purity not in ('sfw', 'sketchy', 'nsfw', 'ws', 'wn', 'sn', 'all'):
        print("Wrong purity input")
        purity_tags = {'sfw': '100', 'sketchy': '010', 'nsfw': '001', 'ws': '110', 'wn': '101', 'sn': '011', 'all': '111'}

    purity_tags = {'sfw': '100', 'sketchy': '010', 'nsfw': '001', 'ws': '110', 'wn': '101', 'sn': '011', 'all': '111'}

    purity_code = purity_tags[purity]

    return purity_code

def sort():
    sort = input("Sort: (tp:toplist dt:data_added ho:hot vi:views ra:random re:relevance): ").lower()

    while sort not in ('tp', 'dt', 'ho', 'vi', 'ra', 're'):
        print("Wrong sort input")
        sort = input("Sort: (tp:toplist dt:data_added ho:hot vi:views ra:random re:relevance): ").lower

    sort_tags = {'tp': 'toplist', 'dt': 'data_added', 'ho': 'hot', 'vi': 'views', 'ra': 'random', 're': 'relevance'}
    sort_code = sort_tags[sort]
    return sort_code

def toprange():
    toprange = input("Enter toprange (1d, 3d, 1w, 1M, 3M, 6M, 1y): ").lower()

    while toprange not in ('1d', '3d', '1w', '1M', '3M', '6M', '1y'):
        print("Wrong toprange input")
        toprange = input("Enter toprange (1d, 3d, 1w, 1M, 3M, 6M, 1y): ").lower()

    toprange_tags = {'1d': '1d', '3d': '3d', '1w': '1w', '1M': '1m', '3M': '3m', '6M': '6m', '1y': '1y'}

    toprange_code = toprange_tags[toprange]
    return toprange_code

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
            if not os.path.isfile(savefile):
                with open(savefile, 'wb') as f:
                    f.write(content)
                print("Downloading: "+ filename)
            else:
                print(filename, 'is already exists skipping download')
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
        
        with ThreadPoolExecutor(max_workers=5) as t:
            for i in range(len(wall)):
                img = wall[i]["path"]
                t.submit(image_download, url=img)
                #image.append(wall["data"][i]["path"])
                #print(image)


         

    

    print(f"PAGE{page} IS OVER")
    print("All is done!")

if __name__ == "__main__":
    main()
