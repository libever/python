#!/bin/env python 
#coding=utf-8

import requests
from pyquery import PyQuery as PQ

"""
获取北京社保的定点医院!
希望你们永远用不到这个文件.
"""


def do_url(url):
    f_find = 0
    content = requests.get(url).text
    
    dom = PQ(content)
    
    rows = dom.find("table[bgcolor]").find("tr")
    
    for row in rows:
        cells = PQ(row).find("td")
        if len(cells) == 5 :
            if f_find == 0 :
                f_find = 1
            else :
                line = ""
                for cell in cells:
                    t = PQ(cell).text().strip()
                    line = line + t + ","
    
                print line
    
for sno in range(0,105):
    url = "http://www.bjrbj.gov.cn/LDJAPP/search/ddyy/ddyy_01_outline_new.jsp?sno=%d&spage=0&epage=105&leibie=&suoshu=&sword=" % (sno * 20)
    do_url(url)


