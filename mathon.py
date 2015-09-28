#!/usr/bin/env python
#coding=utf-8

import sys
import pyquery as pq
import os

f = open("mathon.txt","w")

def simpleTest():
    for page in range(1,3551):
        url = 'http://www.runchina.org.cn/portal.php?mod=score&ac=athlete&year=2015&sex=&age=&project=2&page=' + str(page)
        doc = pq.PyQuery(url)
        table = doc.find("table.ranking")
        users = table.find("tr")
        isFirst = True
        lines = []
        for userId in users:
            if isFirst: 
                isFirst = False
            else :
                lines.append(users(userId).text().encode("UTF-8") + "\n")
                print users(userId).text()
        f.writelines(lines)
    f.close()

if __name__ == "__main__":
    argc = len(sys.argv)
    simpleTest()
