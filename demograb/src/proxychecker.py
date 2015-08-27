#!/usr/bin/env python
#coding=utf-8

import sys
import redis
import requests

def testHttpProxy(host,port):
	ip = host
	port = port
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



def doMainCheck():
	r = redis.Redis(host="localhost",port=6379,db=1)
	members = r.smembers('httpproxy')
	for member in members :
		(host,port) = list(member.split(':'))
		if False == testHttpProxy(host,port) :
			r.srem('httpproxy',member)


if __name__ == "__main__":
	argc = len(sys.argv)
	doMainCheck()
