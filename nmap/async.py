#coding=utf-8

"""
pip install python-nmap
"""

import nmap
import time


def callback_(host,result):
    print host 
    print result

nm = nmap.PortScannerAsync()
nm.scan(hosts='10.210.12.18',ports='1-65535',callback=callback_)

while nm.still_scanning() : 
    print "waiting..."
    time.sleep(1)
