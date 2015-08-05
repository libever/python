#!/bin/env python 

import web

render = web.template.render('templates')

def getLayoutRender(layoutName = 'main'):
	return web.template.render('templates',base = 'layout/' + layoutName)
