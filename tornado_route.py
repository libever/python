#!/bin/env python
#coding=utf-8

app = {}

# set the route handler
def route(view):
    global app
    url = view.URL
    app.add_handlers('.*$',[(r'%s' % (url), view)])

# set tornado web application instance .
def set_app(real_app):
    global app
    app = real_app

def import_handlers():
    import H

