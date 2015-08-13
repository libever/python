#!/bin/env python
# -*- coding: utf-8 -*-
import sys,re
import pyquery as pq
import urllib
import HTMLParser

reload(sys)
sys.setdefaultencoding('utf8')


def urlGet(url):
	page = urllib.urlopen(url)
	content = unicode(page.read(),"utf-8")
	return content

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
	for songHref in songList:
		songName = songList[songHref]
		songUrl = "http://music.baidu.com" + songHref
		doc = pyQueryGet(songUrl)
		lrcPath = doc.find("a.down-lrc-btn").attr("data-lyricdata").split('"')
		if len(lrcPath) > 3 :
			lrcUrl = "http://music.baidu.com" + lrcPath[3]
			lrcContent = urlGet(lrcUrl)
			lines = []
			lines.append("\n================================================================================\n")
			lines.append(songName)
			lines.append(lrcContent)
			f = open("lrc.log","a+")
			f.writelines(lines)
			f.close()
			print songName, songUrl, lrcUrl

def debugDict(dic):
	for i in dic:
		print i , dic[i]

if __name__ == "__main__" :
	tags = getTags()
	for tagText in tags:
		songList = getTagSongs(tagText,tags[tagText])	
		doSongList(songList)
		break

