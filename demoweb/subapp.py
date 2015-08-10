#!/bin/env python

import web

urls = (
		''	, 'main'
)

class main:
	def GET(self):
		return "Hello sub app"

subapp = web.application(urls,globals())
