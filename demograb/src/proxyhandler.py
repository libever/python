#!/usr/bin/env python
#coding=utf-8

import sys
import requests
import pyquery
import time

def getProxyList():
	for index in range(1,10):
		proxyList = []
		url = "http://www.kuaidaili.com/proxylist/%d/" % (index)
		response = requests.get(url)
		content = response.text.encode("UTF-8")	
		doc = pyquery.PyQuery(content)
		proxys = doc.find("#list").find("tr")
		for proxyId in proxys:
			ip = proxys(proxyId).find("td").eq(0).text()
			port = proxys(proxyId).find("td").eq(1).text()
			t = proxys(proxyId).find("td").eq(3).text()
			proxyList.append({"ip":ip,"port":port,"type":t})
		yield proxyList

handlers = []
handlers.append(getProxyList)

def simpleTest():
	pass

if __name__ == "__main__":
	argc = len(sys.argv)
	simpleTest()
