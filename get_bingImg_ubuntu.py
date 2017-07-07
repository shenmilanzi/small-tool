#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import requests
import datetime
from urllib import urlretrieve


def get_bing_img(url):

    path = '/home/wangjw/图片/wallpaper'
    headers = {
        "Host": "cn.bing.com",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; \
                        Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0"
    }

    r = requests.get(url, headers=headers)
    img_link = re.findall(r'az/[a-z]+/[a-z]+/.+1920x1080\.jpg"', r.content)[0]
    imgName = datetime.datetime.today().strftime('%Y-%m-%d') + '.jpg'
    imgPath = os.path.join(path, imgName)
    for img in os.listdir(path):
        if img.is_file() and img.name != imgName:
            filename = os.path.join(path, img.name)
            os.remove(filename)
    urlretrieve(url + img_link[:-1], imgPath)


if __name__ == "__main__":
    url = "http://cn.bing.com/"
    get_bing_img(url)
