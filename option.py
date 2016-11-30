#!/usr/bin/env python
#coding=utf-8

from optparse import OptionParser

parser = OptionParser()
parser.add_option(
    "-o",
    "--operation",
    dest="action",
    help="action to do",
    metavar="main",
    default="main"
)

(options,args) = parser.parse_args()

print options,args
