#!/bin/env python
# -*- coding: utf-8 -*-
import sys
import pyquery as pq
import urllib

if __name__ == "__main__" :
	reload(sys)
	sys.setdefaultencoding('utf8')
	url = "http://music.baidu.com/tag"
	page = urllib.urlopen(url)
	content = page.read()
	doc = pq.PyQuery(content)
	tagPanel = doc.find("div.mod-tag")
	tagLinks = tagPanel.find("a.tag-item")
	for tagId in tagLinks :
		print tagLinks(tagId).text()
	
