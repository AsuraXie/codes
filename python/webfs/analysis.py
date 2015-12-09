#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys

class analysis(object):
	def __init__(self):
		self.re_url=[r"src=[\"']{1}[^\"']*[\"']{1}",r"href=[\"']{1}[^\"']*[\"']{1}"]
		self.mime_type=[]
                self.mime_path='/home/asura/codes/python/webfs/mime.new.types'

	def analysis(self,data):
		all_url=[]
		res_url=[]
		res_src=[]
		result={"next_url":[],"src_url":[]}

		#get all url
		for re_temp in self.re_url:
			pattern=re.compile(re_temp)
			temp_result=pattern.findall(data)
			all_url+=temp_result

		#divide url into two part nexturl or srcurl

		index=0
		for mime_temp in self.mime_type:
			for temp_url in all_url:
				if temp_url.find(mime_temp.strip())>=0:
					res_src.append(temp_url)
				else:
					res_url.append(temp_url)

		result['next_url']=res_url
		result['src_url']=res_src
		print result


	def read_mime(self):
		mime_file=open(self.mime_path,'r')
		while True:
			line=mime_file.readline()
			if line:
				self.mime_type.append(line)
			else:
				break

if __name__=='__main__':
	myanalysis=analysis();
	if len(sys.argv)>1:
		myanalysis.mime_path=sys.argv[1]
	myanalysis.read_mime()
	data=sys.stdin.read()
	myanalysis.analysis(data)
