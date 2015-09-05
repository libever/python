#!/usr/bin/env python
#coding=utf-8

import sys
import requests
import pyquery

def Handler():
    articles = []
    url = "http://istrone.com"
    print "get Content %s " % url
    response = requests.get(url)
    #response.encoding = "UTF-8"
    doc = pyquery.PyQuery(response.text)
    return articles

if __name__ == "__main__":
    argc = len(sys.argv)
    Handler()

