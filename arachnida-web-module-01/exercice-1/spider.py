#!/usr/bin/env python
import os.path
import random
import string
from urllib.parse import urljoin

import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen, HTTPError
import argparse
import requests
import re
import sys


def print_banner():
    print('''
     ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄ ▄▄▄▄▄▄  ▄▄▄▄▄▄▄ ▄▄▄▄▄▄
    █       █       █   █      ██       █   ▄  █
    █  ▄▄▄▄▄█    ▄  █   █  ▄    █    ▄▄▄█  █ █ █
    █ █▄▄▄▄▄█   █▄█ █   █ █ █   █   █▄▄▄█   █▄▄█▄
    █▄▄▄▄▄  █    ▄▄▄█   █ █▄█   █    ▄▄▄█    ▄▄  █
     ▄▄▄▄▄█ █   █   █   █       █   █▄▄▄█   █  █ █
    █▄▄▄▄▄▄▄█▄▄▄█   █▄▄▄█▄▄▄▄▄▄██▄▄▄▄▄▄▄█▄▄▄█  █▄█

    Welcome to the Spider Program
    Author: f0rkr

    This program downloads all images recursively from a website,
    This program will only download images that have the following extensions: .jpg/jpeg, .png, .gif, and .bmp.
  ''')


def get_encoding(header):
    encoding = header['Content-Type'].split('charset=')[-1]
    return encoding

def get_base_url(url):
    match = re.match(r'(https?://[^/]+)/?', url)
    if match:
        return match.group(1)
    else:
        return None
def extracting_images(url, level, path, images, recursive=False):
    # Looping through all images and start extracting them
    for image in images:
        src = image['src']
        #filename = os.path.basename(''.join(random.choice(string.ascii_lowercase) for i in range(16)) + "." + src.split('.')[-1])
        filename = os.path.basename(src)
        filepath = os.path.join(path, filename)
        if not os.path.exists(filepath):
            if "//" in src:
                src = 'https:' + src
            elif 'https' not in src or 'http' not in src:
                # Get base url
                src = get_base_url(url) + src

            print("[+] Downloading image: {0}, url: {1}".format(filename, src))
            response = requests.get(src)
            with open(filepath, 'wb') as f:
                f.write(response.content)
            if level > 0 and recursive:
                next_url = urljoin(url, image['src'])
                run_spider(next_url, level - 1, path, recursive)


def run_spider(url, level, path, recursive=False):
    # Requesting the html of the website page
    hdr = {'User-Agent': 'Mozilla/5.0'}
    proxy_host = '158.69.53.98:9300'

    http_data = Request(url, headers=hdr, )


    # Parsing the html page with BeautifulSoup
    soup = BeautifulSoup(urlopen(http_data), features="html.parser")

    # Extracting all img tag in the html parsed data
    images = soup.find_all('img')

    
    extracting_images(url, level, path, images, recursive)


if __name__ == "__main__":
    # Display program banner
    print_banner()

    # TO-DO: Parsing arguments using argparse
    parser = argparse.ArgumentParser(
        prog='spider', description='The spider program allow you to extract all the images from a website, '
                                   'recursively, by providing a url as a parameter.')
    parser.add_argument('-r', '--recursive', action='store_true',
                        help='Recursively downloads the images in a URL received as a parameter.')
    parser.add_argument('-l', '--level', type=int, default=5, help='Indicates the maximum depth level of the '
                                                                   'recursive download. If not indicated, it will be '
                                                                   '5.')
    parser.add_argument('-p', '--path', type=str, default='./data/', help='Indicates the path where the downloaded '
                                                                          'files will be saved. If not specified, '
                                                                          './data/ will be used.')
    parser.add_argument('URL', type=str, help='URL to extract all the images recursively from.')
    args = parser.parse_args()

    if not os.path.exists(args.path):
        os.mkdir(args.path)

    print("[!] Running with the following arguments.")
    print("[+] url: {0}, level: {1}, path: {2}, recursive: {3}".format(args.URL, args.level, args.path, args.recursive))
    run_spider(args.URL, args.level, args.path, args.recursive)
# EOF
