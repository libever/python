#!/usr/bin/env python

import sys,urllib
import pyquery as pq

if __name__ == "__main__"  and len(sys.argv) == 2:
	packageName = sys.argv[1]
	url = "http://anyapi.sinaapp.com/a.php?url=https://pypi.python.org/simple/%s/" % (packageName)
	page = urllib.urlopen(url)
	content = page.read()
	doc = pq.PyQuery(content)
	links = doc.find("a")
	for linkId in links:
		print links(linkId).text() , links(linkId).attr("href").replace("../..","https://pypi.python.org")
