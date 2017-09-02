#-*- coding: utf-8 -*-
import logging 

log_file = "x.log"

logging.basicConfig(
	level=logging.INFO,
	format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
	datefmt='%a, %d %b %Y %H:%M:%S',
	filename =  log_file ,
	filemode='a'
)

class XHandler(logging.StreamHandler) :
	
	def __init__(self,filename):
		logging.StreamHandler.__init__(self,open(filename,"a"))

	def emit(self,record):
		logging.StreamHandler.emit(self,record)

class XFilter(logging.Filter):

	def filter(self,record):
		record.msg = "changed!"
		return True

	
ch = XHandler("b.log")
ch.addFilter(XFilter())

ch.setLevel(logging.DEBUG) 
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') 
ch.setFormatter(formatter) 

logging.getLogger('').addHandler(ch)

logging.info("hello world")
