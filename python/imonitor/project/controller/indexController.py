#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
sys.path.append("./frame")
import jt_controller

class indexController(jt_controller.jt_controller):
	def index(self):
		return self.render("index","index",{"wokao":"nimei"})
