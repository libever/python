#!/usr/bin/env python
import web
import actions

urls = actions.urls

if(__name__ != "__main__"):
	app = web.application(urls, globals())  
	application = app.wsgifunc() 
else :
	app = web.application(urls, globals())  
	app.run()
