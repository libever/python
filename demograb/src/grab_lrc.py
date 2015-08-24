#!/bin/env python
# -*- coding: utf-8 -*-

import sys,re
import pyquery as pq
import urllib
import HTMLParser
import threadpool
import requests
import time

def urlGet(url,**kwargs):
	kwargs.setdefault("encoding","UTF-8")
	charset = kwargs.get("encoding")
	r = requests.get(url)
	r.encoding = charset
	return r.text.encode(charset)

def pyQueryGet(url):
	content = urlGet(url)
	doc = pq.PyQuery(content)
	return doc

def getTags():
	m = {} 
	doc = pyQueryGet("http://music.baidu.com/tag")
	tagPanel = doc.find("div.tag-main")
	tagLinks = tagPanel.find("a.tag-item")
	for tagId in tagLinks:
		href = tagLinks(tagId).attr("href")
		tagText = tagLinks(tagId).text()
		if -1 == href.find("lebo") :
			m[tagText] = href
	return m


def getTagSongs(tagText,tagHref):
	tagUrl = "http://music.baidu.com" + tagHref
	print tagUrl
	doc = pyQueryGet(tagUrl)
	songLinks = doc.find("span.song-title a")
	songList = {}
	for songId in songLinks:
		songHref = songLinks(songId).attr("href")
		songName = songLinks(songId).text()
		if 0 == songHref.find("/song/"):
			songList[songHref] = songName 
	return songList

def doSongList(songList):
	i = 0
	for songHref in songList:
		songName = songList[songHref]
		songUrl = "http://music.baidu.com" + songHref
		print songName , songUrl
		doc = pyQueryGet(songUrl)
		lrcPath = doc.find("a.down-lrc-btn").attr("data-lyricdata")
		if None != lrcPath and len(lrcPath.split('"')) > 3 :
			lrcPath = lrcPath.split('"')
			lrcUrl = "http://music.baidu.com" + lrcPath[3]
			lrcContent = urlGet(lrcUrl)
			lines = []
			lines.append("\n================================================================================\n")
			lines.append(songName.encode("UTF-8"))
			lines.append(lrcContent)
			f = open("lrc.log","a+")
			f.writelines(lines)
			f.close()
			print songName, songUrl, lrcUrl
			i += 1
	return i

def debugDict(dic):
	for i in dic:
		print i , dic[i]

if __name__ == "__main__" :
	tags = getTags()
	pool = threadpool.ThreadPool(2)
	for tagtext in tags:
		songList = getTagSongs(tagtext,tags[tagtext])	
		pool.add_task(doSongList,songList)
		#doSongList(songList)

	pool.show_results()

	time.sleep(1800)
