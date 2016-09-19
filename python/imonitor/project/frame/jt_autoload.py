#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os

class jt_autoload():
	
	def ifExists(self,filename):
		if os.path.exists(filename):
			return True
		else:
			return False

	def loadFile(self,filename):
		if not self.ifExists(filename):
			return "not found file"
		else:
			f=open(filename,"r")
			content=f.read()
			f.close()
			return content
