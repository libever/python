#!/usr/bin/env python



import web
import actions
import subapp

urls = actions.urls

def registerSubApp(url,app):
	urls.extend([url,app])

def myNotFound():
	return web.notfound("Not found my page ")

def myInternalError():
	return web.internalerror("Some Error happend ....")

registerSubApp('/sub',subapp.subapp)

app = web.application(urls, globals())  
app.notfound = myNotFound

if(__name__ != "__main__"):
	application = app.wsgifunc() 
else :
	app.run()
