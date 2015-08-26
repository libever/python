#!/usr/bin/env python
#coding=utf-8

import sys
import re 
import requests
import pyquery

def writeItem(item):
	lines = []
	lines.append(item["ip"] + ":" + item["port"] + "\n")
	m = open("proxylist.txt","a+")
	m.writelines(lines)
	m.close()

def getProxyList(index):
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
	return proxyList

def testProxy(proxyItem):
	print proxyItem
	ip = proxyItem["ip"]
	port = proxyItem["port"]
	t = proxyItem["type"]
	session = requests.session()
	session.proxies = {
			"http": ip + ":" + port
	}
	try :
		r = session.get("http://anyapi.sinaapp.com/ip.php",timeout=1)
		writeItem(proxyItem)
		print "OK"
	except Exception,e:
		print e
		pass

def simpleTest():
	for index  in range(1,10):
		print index
		proxyList = getProxyList(index)
		for k,item in enumerate(proxyList) :
			testProxy(item)

if __name__ == "__main__":
	argc = len(sys.argv)
	simpleTest()
