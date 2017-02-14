#coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_string = "mysql+mysqldb://giteye:g@8i2017@10.210.12.18/giteye?charset=utf8"

def getSession(db_string):
	engine = create_engine(db_string,echo = False,pool_size=20,pool_recycle=30)
	Seesion =sessionmaker(bind=engine,autoflush = True)
	s = Seesion()
	return s

def exesql(sql):
	s = getSession(db_string)

	try:
		o = s.execute(sql)
	except Exception,e:
		print e
		print sql
		s.close()
		exit()
		return

	t = sql[0:3].lower()

	if t == "sel":
		s.close()
		return o.fetchall()
	elif t == "ins":
		s.commit()
		s.close()
		return o.lastrowid
	elif t == "upd":
		s.commit()
		print dir(o)
		s.close()
		return o.rowcount
	else :
		s.commit()
		s.close()
		return o.rowcount

def sSaveDb(item,tableName):
	x = "SELECT COUNT(*) FROM %s WHERE ukey = '%s' " % (tableName,item["ukey"]) 
	c = exesql(x)[0][0]
	if c > 0 :
		return 

	s = "INSERT INTO %s(%s) VALUES (%s)"  % (tableName,item["fields"],item["values"])
	exesql(s)
