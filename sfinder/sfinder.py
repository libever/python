#!/bin/env python
#coding=utf-8

import url_manager
import downloader 
import parser
import output

class sfinder :

    def __init__(self):
        self.manager = url_manager.manager() 
        self.downloader = downloader.simple()
        self.parser = parser.simple()
        self.output = output.simple()

    def start(self,url):
        self.manager.add(url)

        while self.manager.has_new() :
            url = sef.manager.get_new()
            content = self.downloader.download(url)
            urls,items = self.parser.parse(content)
            self.manager.add(urls)
            self.output.out(items)

if __name__ == "__main__" :
    url = ""
    sf = sfinder()
    sf.start(url)
