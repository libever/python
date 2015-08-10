#!/usr/bin/env python
import web
import actions
import subapp

urls = actions.urls

def registerSubApp(url,app):
	urls.extend([url,app])

registerSubApp('/sub',subapp.subapp)

if(__name__ != "__main__"):
	app = web.application(urls, globals())  
	application = app.wsgifunc() 
else :
	app = web.application(urls, globals())  
	app.run()
