#!/usr/bin/env python
#coding=utf-8

import sys
import handlers

def doMain():
    for h in handlers.Handlers :
        h.__call__()

if __name__ == "__main__":
    doMain()
