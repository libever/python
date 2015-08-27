#!/usr/bin/env python
#coding=utf-8

import sys
import re 
import requests
import pyquery
import redis
import proxyhandler

def saveItem(item):
	r = redis.Redis(host="localhost",port=6379,db=1)
	r.sadd("httpproxy",item["ip"] + ":" + item["port"])

def testProxy(proxyItem):
	ip = proxyItem["ip"]
	port = proxyItem["port"]
	t = proxyItem["type"]
	session = requests.session()
	session.proxies = {
			"http": ip + ":" + port
	}
	try :
		r = session.get("http://anyapi.sinaapp.com/ip.php",timeout=1)
		if r.text == ip :
			return True
	except Exception,e:
		return False

def doFindProxyListHandler():
	handlers = proxyhandler.handlers
	for m in handlers:
		for plist in m.__call__():
			if isinstance(plist,list):
				for item in plist:
					doProxyItem(item)
			else :
				doProxyItem(plist)

def doProxyItem(item):
	if testProxy(item):
		saveItem(item)

if __name__ == "__main__":
	doFindProxyListHandler()
