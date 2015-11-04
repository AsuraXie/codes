#!/usr/bin/env python
import re
import sys

re_url=["src=[\"']{1}[^\"']*[\"']{1}","href=[\"']{1}[^\"']*[\"']{1}"]
re_src=["src=[\"']{1}[^\"']*[\"']{1}"]

def analysis(data):
	res_url=[]
	res_src=[]
	for re_temp in re_url:
		pattern=re.compile('r'+re_temp)
		temp_result=pattern.findall(data)
		res_url+=temp_result
	for re_temp in re_src:
		pattern=re.compile('r'+re_temp)
		temp_result=pattern.findall(data)
		res_src+=temp_result

	print res_url,res_src

if __name__=='__main__':
	data=sys.stdin.read()
	analysis(data)
