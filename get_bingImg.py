#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#使用selenium+PhantomJS爬取并下载bing每日图片，以当天时间命名，保存到系统图片文件夹
#使用selenium+PhantomJS的好处在于可以获取到加载完成后的脚本的信息

import os
import re
import datetime, time
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import urlretrieve

def get_bingImg(url):
    path = r'C:\Users\Wjw\Pictures\Saved Pictures'
    browser = webdriver.PhantomJS()
    browser.get(url)
    time.sleep(5)
    pg_sc_cd = browser.page_source
    page = BeautifulSoup(pg_sc_cd, 'html.parser')
    script = page.findAll('div', id= 'bgDiv')
    #print(script[0].get('style'))
    urlFmt = re.compile(r'http:.*\.jpg')
    imgUrl = re.findall(urlFmt, script[0].get('style'))
    imgName = datetime.datetime.today().strftime('%Y-%m-%d') + '.jpg'
    imgPath = os.path.join(path, imgName)
    for img in os.scandir(path):
        if img.is_file() and img.name != imgName:
            filename = os.path.join(path, img.name)
            os.remove(filename)
    urlretrieve(imgUrl[0], imgPath)
    browser.quit()
    
if __name__ == '__main__':
    url = 'http://cn.bing.com/'
    get_bingImg(url)
