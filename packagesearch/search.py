#!/usr/bin/env python

#https://github.com/search?l=Python&q=lxml&type=Repositories
	#$(".repo-list-item").eq(0).find("a:eq(2)")

import sys,urllib
import pyquery as pq

if __name__ == "__main__"  and len(sys.argv) == 2:
	packageName = sys.argv[1]
	url = "https://github.com/search?l=Python&q=%s&type=Repositories" % (packageName)
	page = urllib.urlopen(url)
	content = page.read()
	doc = pq.PyQuery(content)
	panels = doc.find(".repo-list-item")
	for panelID in panels :
		links = panels(panelID).find("a")
		href = pq.PyQuery(links[0]).attr("href")
		href = href.split("/stargazers")[0]
		print "https://github.com/%s.git" % (href)
