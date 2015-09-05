#!/usr/bin/env python
#coding=utf-8

import sys

Handlers = []

def addHandler(h):
    Handlers.append(h)

#AUTOCODE:istrone
import istrone
addHandler(istrone.Handler)
#AUTOCODE_END:istrone
