#!/bin/env python 

import web
from models.sample import sample as sf
from util import render,getLayoutRender

class main:
	def GET(self):
		return getLayoutRender().index("Hello world.")
