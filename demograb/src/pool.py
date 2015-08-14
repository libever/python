#!/usr/bin/env python
#coding=utf-8

import sys
import threadpool
import time

def do_work(i,j,k):
	print i,j,k
	time.sleep(2)

def simpleTest():
	print "Hello this is a simple test ."
	pool = threadpool.ThreadPool(8)
	for i in range(0,100):
		pool.add_task(do_work,i,2,3)
	pool.destroy()

if __name__ == "__main__":
	argc = len(sys.argv)
	simpleTest()
