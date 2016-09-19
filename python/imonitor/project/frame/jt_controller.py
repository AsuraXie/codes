#!/usr/bin/env python
#-*- coding:utf-8 -*-

import jt_autoload
import os

class jt_controller():

	def __init__(self):
		self.__current_path=os.getcwd()

	def render(self,directory,filename,param):
		my_autoloader=jt_autoload.jt_autoload()
		res=my_autoloader.loadFile(self.__current_path+"/project/view/"+directory+"/"+filename+".html")
		result=""
		html_array=res.split("<?")
		for i in range(0,len(html_array)):
			if "?>" in html_array[i]:
				python_cmd=html_array[i].split("?>")
				python_cmd[0]=python_cmd[0].strip(" ")
				if python_cmd[0][0:5]=="print":
					result=result+str(eval(python_cmd[0][5:]))
				else:
					result=result+str(eval(python_cmd[0]))

				if python_cmd[1]!="":
					result=result+python_cmd[1]
			else:
				result=result+html_array[i].strip("\n")
		return result

if __name__=="__main__":
	my_controller=jt_controller()
	print my_controller.render("wokao","nimei")
