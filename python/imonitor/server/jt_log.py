#!/usr/bin/env python
#-*- coding:utf-8 -*-

import jt_config

class jt_log():
	def write(self,content):
		my_config=jt_config.jt_config()
		log_path=my_config.getLogPath()
		f=open(log_path,'a')
		f.write(content+"\n")
		f.close()	
