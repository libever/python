#!/bin/env python
# -*- coding: utf-8 -*-

import sys,re
import pyquery as pq
import urllib
import HTMLParser
import threadpool
import requests
import time
import os

def tagTjDownload(tagText,tagHref,downloadLrs):
    m = open("result.log","a+")
    lines = []
    lines.append(tagText.encode("UTF-8") + "\n")
    lines.append(tagHref.encode("UTF-8") + "\n")
    lines.append(str(len(downloadLrs)) + "\n")
    m.writelines(lines)
    m.close()


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


def getTagSongs(tagText,tagHref,offset):
    tagUrl = "http://music.baidu.com" + tagHref +"?start=" + str(offset)  + "&size=25&third_type=0"
    #print tagUrl
    doc = pyQueryGet(tagUrl)
    songLinks = doc.find("span.song-title a")
    songList = {}
    for songId in songLinks:
        songHref = songLinks(songId).attr("href")
        songName = songLinks(songId).text()
        if 0 == songHref.find("/song/"):
            songList[songHref] = songName 
    return songList

def doSongList(songList,**kwargs):
    downloadLrs = []
    for songHref in songList:
        songName = songList[songHref]
        songUrl = "http://music.baidu.com" + songHref
        #print songName , songUrl
        print songName.encode("UTF-8")
    #kwargs.setdefault("tagText","")
    #kwargs.setdefault("tagHref","")
    #tagTjDownload(kwargs.get("tagText"),kwargs.get("tagHref"),downloadLrs)
    return len(downloadLrs) 

def debugDict(dic):
    for i in dic:
        print i , dic[i]

def daemonTask():
    try :
        pid = os.fork()
        if  pid > 0 :
            sys.exit(0)
    except OSError,e :
        print >> sys.stderr , "fork error %d (%s)"  % (e.errno,e.strerror)
        sys.exit(1)
    #os.chdir("/")
    os.setsid()
    os.umask(0)

    try :
        pid = os.fork()
        if pid > 0 :
            print "Daemon PID  %d " % pid
            sys.exit(0)
    except OSError,e:
        print >> sys.stderr , e
        sys.exit(1)

    logfile = open("daemon.log","w",0)
    sys.stdout = logfile

if __name__ == "__main__" :
    daemonTask()
    tags = getTags()
    pool = threadpool.ThreadPool(2)
    index = 0
    for tagtext in tags:
        for i in range(1,20):
            offset = i * 25
            songList = getTagSongs(tagtext,tags[tagtext],offset)	
            pool.add_task(doSongList,songList,tagText=tagtext,tagHref = tags[tagtext])
            index += 1
            if index % 10 == 0 :
                break
        #doSongList(songList)
    pool.destroy()
