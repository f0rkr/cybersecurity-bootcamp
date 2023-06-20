<img src="/images/spider.jpg" />


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

The spider program allow you to extract all the images from a website, recursively, by
providing a url as a parameter.

You have to manage the following program options:
 - ./spider [-rlp] URL
 -  Option -r : recursively downloads the images in a URL received as a parameter.
 -  Option -r -l [N] : indicates the maximum depth level of the recursive download. If not indicated, it will be 5.
 - Option -p [PATH] : indicates the path where the downloaded files will be saved. If not specified, ./data/ will be used.

The program will download the following extensions by default:
 - .jpg/jpeg
 - .png
 - .gif
 - .bmp

# Usage
```bash
> python3.11 -m venv env
> source env/bin/activate
> pip install -r requirements.txt
> chmod +x spider.py
> ./spider [-h] [-r] [-l LEVEL] [-p PATH] URL
```
