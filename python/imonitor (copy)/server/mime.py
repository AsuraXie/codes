#!/usr/bin/env python
#-*- coding:utf-8 -*-

class jt_mime:

	def __init__(self):
		self.__mime=["html"]
	
	def checkExists(self,type):
		if(type in self.__mime):
			return True;
		else:
			return False;
