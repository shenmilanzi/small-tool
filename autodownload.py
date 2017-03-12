#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import urllib.request
import re
from bs4 import BeautifulSoup

class AutoDownload(object):
    def __init__(self, url):
        self.url = url
    
    def get_page(self):
        headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
                    'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'}
        req = urllib.request.Request(url= self.url, headers= headers)
        html = urllib.request.urlopen(req)
        data = BeautifulSoup(html, 'html.parser')
        return data
        
    def chk_update(self, page):
        target = page.find_all('a', text= ['Westworld 2016 - 西部世界', 'Humans - 真实的人类'])
        if target:
            return self.url + target[0].get('href'), self.url + target[1].get('href')
        else:
            return 'Not update yet!'
        
    def fetch_link(self, page):
        link = []
        link = page.find('div', id= 'd_3_1').find_all('a', href = re.compile(r'^(ed2k):\/\/\|file\|%.*'))
        return link
    
    def download(self, dldlink):
        latestEpi = dldlink[-1].get('href')
        os.execl(r'D:\软件\ThunderSpeed\Program\Thunder.exe', '-StartType:Desktop', latestEpi)

if __name__ == '__main__':
    url = 'http://videos.yizhansou.com'             #西部世界4302, 真实的人类4352
    newTask = []
    TV = AutoDownload(url)
    page_data = TV.get_page()
    if isinstance(TV.chk_update(page_data), tuple):
        for elem in TV.chk_update(page_data):
            newTV = AutoDownload(elem)
            newPage = newTV.get_page()
            dldlink = newTV.fetch_link(newPage)
            #TV.download(dldlink)
            newTask.append(dldlink[-1].get('href'))
        os.execl(r'D:\软件\ThunderSpeed\Program\Thunder.exe', '-StartType:Desktop', newTask[0], newTask[1])
    else:
        print(TV.chk_update(page_data))
    