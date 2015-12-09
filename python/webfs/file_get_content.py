#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import urllib2

class HttpFile(object):
	def file_get_contents(self,url):
		temp_data=urllib2.urlopen(url)
		data=temp_data.read()
		return data
	
	def store_src(self,data,url,path):
		store_path=path+self.get_url_filename(url)
		filehandler=open(store_path,'wb+')
		filehandler.write(data)
		filehandler.close()
		return True
	
	def get_url_filename(self,urlpath):
		str_split=urlpath.split('/')
		filename=str_split[-1]
		return filename
		
if __name__=='__main__':
	if len(sys.argv)<3:
		print "Usage:./file_get_content url path "
		print "Need at least two arg"
		exit()
	myfile=HttpFile()
	data=myfile.file_get_contents(sys.argv[1])
	myfile.store_src(data,sys.argv[1],sys.argv[2])
