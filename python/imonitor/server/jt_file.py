#!/usr/bin/env python
#-*- coding:utf-8 -*-

class jt_file():

	def __init__(self):
		self.__wwwroot="/home/asura/codes/python/imonitor/project"
	
	def load(self,path):
		try:
			f=open(self.__wwwroot+path,"r")
			res=f.read()
			f.close()
			return res	
		except Exception,msg:
			return False;
