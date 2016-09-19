#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import jt_autoload
import os

class jt_mvc():
	
	def __init__(self,params):
		self.__global=params
		url=self.__global['url'].split("/")

		self.__controller="index"
		self.__function="index"

		if len(url)==2:
			self.__controller=url[0]
			self.__function=url[1]

	def run(self):
		controller_file=os.getcwd()+"/project/controller/"+self.__controller+"Controller.py"
		my_loader=jt_autoload.jt_autoload()

		if not my_loader.ifExists(controller_file):
			return 	controller_file+" file not exists"
		
		sys.path.append("/home/asura/codes/python/imonitor/project/controller/")
		my_controller=__import__(self.__controller+"Controller")
		my_controller=getattr(my_controller,self.__controller+"Controller")
		my_controller=my_controller()
		return eval("my_controller."+self.__function+"()")
