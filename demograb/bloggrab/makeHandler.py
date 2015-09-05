#!/usr/bin/env python
#coding=utf-8

import sys
import os
import re

def delHandler(name):

    addcode = """
#AUTOCODE:%(name)s
import %(name)s
addHandler(%(name)s.Handler)
#AUTOCODE_END:%(name)s
""" % {"name":name}
    print addcode

    m = open("handlers/utils.py","r")
    c = m.read()
    m.close()
    newc = c.replace(addcode,"")

    m = open("handlers/utils.py","w")
    m.writelines(newc)
    m.close()

    os.remove("handlers/" + name + ".py")

    
def makeHandler(name,url): 

    if "-d" == url :
        return delHandler(name)

    if os.path.isfile("handlers/" + name + ".py" ) :
        print "Handler named %s already exist " % (name)
        return False


    print "make handler %s for %s " % (name,url)
    handlerTpl = """#!/usr/bin/env python
#coding=utf-8

import sys
import requests
import pyquery

def Handler():
    articles = []
    url = "%(url)s"
    print "get Content %(p)ss " %(p)s url
    response = requests.get(url)
    #response.encoding = "UTF-8"
    doc = pyquery.PyQuery(response.text)
    return articles

if __name__ == "__main__":
    argc = len(sys.argv)
    Handler()

"""
    handlerContent = handlerTpl % {"url":url,"p":"%"}
    m = open("handlers/" + name + ".py","w")
    m.writelines(handlerContent)

    u = open("handlers/utils.py","a+")
    lines = """
#AUTOCODE:%(name)s
import %(name)s
addHandler(%(name)s.Handler)
#AUTOCODE_END:%(name)s
"""

    lines = lines % {"name":name}
    u.writelines(lines)


if __name__ == "__main__":
    argc = len(sys.argv)
    if 3 != argc :
        print "Usage : python %s name [url | -d]" % (sys.argv[0])
        sys.exit(1)
    else :
        name = sys.argv[1]
        url = sys.argv[2]
        makeHandler(name,url)
