#!/usr/bin/env python

import web

urls = (
		'/', 'actions.index.main'
)


if(__name__ != "__main__"):
	app = web.application(urls, globals())  
	application = app.wsgifunc() 
else :
	app = web.application(urls, globals())  
	app.run()
