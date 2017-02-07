#!/usr/bin/env python
#coding=utf-8

import sys
import requests
import json
from multiprocessing import Pool
import os,time
from pyquery import PyQuery as PQ
import urllib

user_cookie = "_octo=GH1.1.263808671.1467603093; logged_in=yes; dotcom_user=qixingyue; _gh_sess=eyJsYXN0X3dyaXRlIjoxNDg2MTk0NjExMDg1LCJzZXNzaW9uX2lkIjoiODYyNmJmMDhhNDUwYTYyZWQ0MmQxNGUwNzdkZmE2MGIiLCJjb250ZXh0IjoiLyJ9--3cb53d20b784fd44ccf57c8159814e08ac14eafb; _ga=GA1.2.403517303.1477447666; _gat=1; tz=Asia%2FShanghai; user_session=3bBKnItyEqo2icP-d0iAtzw1ufJsZY9YhqtOj6oa_53fl1Y5; __Host-user_session_same_site=3bBKnItyEqo2icP-d0iAtzw1ufJsZY9YhqtOj6oa_53fl1Y5"

## 对勾的utf8表示
end_x="%E2%9C%93"

def testProxy(ip,port):
    #t = proxyItem["type"]
    session = requests.session()
    session.proxies = {
        "https": str(ip) + ":" + str(port)
    }
    try :
        r = session.get("https://baidu.com/",timeout=3)
        if r.status_code == 200:
            #print ip , port ,"OK"
            return True
    except Exception,e:
        pass

def findProxy(notList):
    #print notList
    response = requests.get("http://10.210.76.52:8000/?types=0")
    content = response.text
    pList = json.loads(content)
    for i in range(0,len(pList)):
        istr = str(pList[i][0]) + ":" + str(pList[i][1])
        if True == testProxy(pList[i][0] , pList[i][1]) and istr not in notList:
            #print istr
            return istr


def loadUrl(url,storageHandler):
    global user_cookie
    print url
    notList = []

    while True:

        #proxyAddr = findProxy(notList)
        session = requests.session()
        #session.proxies = {
        #		"https": proxyAddr,
        #		"http": proxyAddr
        #}

        cookieHeaders = {"Cookie":user_cookie}

        try:
            c = session.get(url,timeout=30,headers=cookieHeaders)
        except Exception,e:
            print e
            print "BAD"
            #notList.append(proxyAddr)
            continue

        if c.status_code == 200 :
            doc = PQ(c.text)
            items = doc.find("div.code-list-item")
            for item in items:
                links = PQ(item).find("p.title a")
                item = {
                    "project":PQ(links[0]).attr("href"),
                    "file":PQ(links[1]).attr("href")
                }
                storageHandler(item)

            #nextAddr = c.headers["Link"].split(">")[0][1:]
            #print "%s : OK" % (url)
            #url = nextAddr
            #data = json.loads(c.text)
            #print data[0]["login"]
            break
        else :
            #print "BAD"
            #notList.append(proxyAddr)
            pass


def itemStorage(item):
    print item

def searchKeywordCode(keyword):
    global end_x
    urls = [ "https://github.com/search?p=%d&q=%s&ref=searchresults&type=Code&utf8=%s" % (p,keyword,end_x) for p in range(0,3) ]
    for u in urls:
        loadUrl(u,itemStorage)

def updateGitUserCookie(u,p):
    global end_x

    session = requests.session()
    tokenDom = PQ(session.get("https://github.com/login").text).find("input[name=authenticity_token]")
    tokenValue = PQ(tokenDom).attr("value")

    data = {
        "authenticity_token":tokenValue,
        "login":u,
        "password":p,
        "commit":"Sign in",
        "utf8":end_x
    }

    headers = {
        #"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        #"Accept-Encoding": "gzip, deflate, sdch, br",
        #"Accept-Language": "zh-CN,zh;q=0.8",
        #"Cache-Control": "max-age=0",
        #"Connection": "keep-alive",
        #"Cookie": "logged_in=no; _ga=GA1.2.1617737580.1435283028; _octo=GH1.1.1732531857.1435283028; _gh_sess=eyJsYXN0X3dyaXRlIjoxNDg2MzcxMTYyOTg3LCJzZXNzaW9uX2lkIjoiNzgyZjg0ODEzOGU3ZWQ3Nzc1YTVkNDNkNTg1NTE3ZGYiLCJjb250ZXh0IjoiLyIsInJlZmVycmFsX2NvZGUiOiJodHRwczovL2dpdGh1Yi5jb20vIiwiX2NzcmZfdG9rZW4iOiJjVmJBKzdHUW40OTRDcnROYVVYV1F3Q3Y5TENpNU51RU9IOUlCaUtzcWpvPSIsImZsYXNoIjp7ImRpc2NhcmQiOltdLCJmbGFzaGVzIjp7ImFuYWx5dGljc19sb2NhdGlvbl9xdWVyeV9zdHJpcCI6InRydWUifX19--0fc6cb5876840f0b474fe576303d0eb2970b3c1b; tz=Asia%2FShanghai; _gat=1",
        "Host": "github.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:50.0) Gecko/20100101 Firefox/50.0"
    }

    loginSubmitUrl = "https://github.com/session"
    c = session.post(loginSubmitUrl,data = data,headers=headers)

    cookieStr = ""
    for cookie in session.cookies:
        cookieStr = cookieStr + cookie.name + "=" + cookie.value + "; "
        #print cookie.name
        #print cookie.value
        #print dir(cookie)
    print cookieStr
    global user_cookie 
    user_cookie = cookieStr


u_arr = open("/Users/xingyue/.pwd","r").read().strip().split(":")

updateGitUserCookie(u_arr[0],u_arr[1])
keyword="staff.sina.com.cn"
searchKeywordCode(keyword)

#pool = Pool(processes=6)

#  u="https://api.github.com/users/qixingyue"
#  pool.apply_async(loadUrl,(u,))
#  
# urls = [ "https://api.github.com/users?since=%d" % p for p in range(0,90000000,30) ];
# for u in urls:
# 	print u
# 	pool.apply_async(loadUrl,(u,))

#pool.close()
#pool.join()


