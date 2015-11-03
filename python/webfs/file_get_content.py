#!/usr/bin/env python
import sys
import urllib2

def file_get_contents(url):
	temp_data=urllib2.urlopen(url)
	data=temp_data.read()
	return data
	
def store_src(data,url,path):
	store_path=path+get_url_filename(url)
	filehandler=open(store_path,'wb+')
	filehandler.write(data)
	filehandler.close()
	return True
	
def get_url_filename(urlpath):
	str_split=urlpath.split('/')
	filename=str_split[-1]
	return filename
		
if __name__=='__main__':
	if len(sys.argv)<3:
		print "Usage:./file_get_content url path "
		print "Need at least two arg"
		exit()
	file_get_contents(sys.argv[1],sys.argv[2])
