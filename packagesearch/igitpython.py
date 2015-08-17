#!/usr/bin/env python

# coding : utf-8

import sys
import os

url = ""

if __name__ == "__main__" :
	url = sys.argv[1]
	packageName = url.split("/")[-1].split(".")[0]
	os.system("git clone " + url)
	os.system("cd "+packageName + " && python setup.py install")
	os.system("rm -rf " + packageName)
	
	
