#coding=utf-8

"""
pip install python-nmap
"""

import nmap

nm = nmap.PortScanner()
nm.scan("10.210.12.18","1-65535")
print nm.scaninfo()

print nm.csv()
    


