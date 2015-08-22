#!/usr/bin/env python
#coding=utf-8

import sys
import requests

def simpleTest():
	url = 'http://www.baidu.com'
	r = requests.get(url)
	print r.text

if __name__ == "__main__":
	argc = len(sys.argv)
	simpleTest()
