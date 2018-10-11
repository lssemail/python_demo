#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib3
import requests
import os
import re
from bs4 import BeautifulSoup


requests.packages.urllib3.disable_warnings()
folder_path = "G:\liusir\logs\\novel\\"

class NovelSpider(object):

    def __init__(self):
        self.baseUrl = "https://www.biquke.com"
        self.bookId = "/bq/0/990/"
        self.url = self.baseUrl + self.bookId
        self.method = "GET"
        self.folder = "G:\\liusir\\logs\\novel\\"

    def get_href_list(self):

        urls = []
        http = urllib3.PoolManager()
        request = http.request(self.method, self.url)
        soup = BeautifulSoup(request.data, 'html.parser')
        result = soup.select('div[id="list"] dl dd a')
        for item in result:
            self.get_page_info(item.get("href"))
            urls.append(item.get("href"))

        total = len(urls)

        return total, urls

    def get_page_info(self, url):

        http = urllib3.PoolManager()
        # url = 'https://www.biquke.com/bq/0/990/3703064.html'
        request = http.request(self.method, self.url + url)
        soup = BeautifulSoup(request.data, 'html.parser')
        titles = soup.select('div[class="bookname"] h1')
        contents = soup.select('div[id="content"]')
        title = titles[0]
        content = contents[0]
        str_title = title.string.replace(" ", "")
        section_text = re.sub('\s+', '\r\n\t', content.text).strip('\r\n')
        temp_folder_name = folder_path + str_title + ".txt"
        try:
            with open(temp_folder_name, 'w+') as item:
                item.write(section_text)
        except UnicodeEncodeError :
           pass

        print("download success")




if __name__ == '__main__':

    total, urls = NovelSpider().get_href_list()
    # print(total)
    # NovelSpider().get_page_info()

    # print(os.path.exists("num.db"))
    # with open("num.db") as num:
    #     print(num.readline())
