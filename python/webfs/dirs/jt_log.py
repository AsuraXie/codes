#!/usr/bin/env python
import os
import time
import jt_global
import jt_common
from os.path import getsize
class log(object):
	@staticmethod
	def write(path,logs):
		if os.path.exists(path):
			size=getsize(path)
			if size>=1024*1024*4:
				newpath=time.strftime(jt_global.isotimeformate_brief)
				print jt_common.rename(path,newpath)
				
		try:
			temp_file=open(path,'a')
			temp_file.write(time.strftime(jt_global.isotimeformate)+"---"+logs+"\n")
			temp_file.close()
		except Exception,e:
			print e
			print "write log failed"

if __name__=="__main__":
	a=log()
	a.write('log/http/a.txt',"xielixiang")
