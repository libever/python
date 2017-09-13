#!/data1/python27/bin/python
#coding=utf-8

import pcap
import dpkt

pc = pcap.pcap('eth0')

pc.setfilter('udp port 1812')
for ptime,pdata in pc:
	frame = dpkt.ethernet.Ethernet(pdata)
	ip = '%d.%d.%d.%d' % tuple(map(ord,list(frame.data.dst)))
	transfer = frame.data.data.__class__.__name__
	print ip,transfer
	print frame.data.data
