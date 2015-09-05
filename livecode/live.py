#!/usr/bin/env python
#coding=utf-8

import sys

def simpleTest():


    name = "demo"
    liveContent = """
def Run():
    print "Demo RUN "
"""
    o = open("demo.py","w")
    o.writelines(liveContent)
    o.close()

    import demo
    demo.Run()
   



if __name__ == "__main__":
    argc = len(sys.argv)
    simpleTest()
