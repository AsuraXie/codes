#!/usr/bin/env python
import re
import sys

re_url=[r"src=[\"']{1}[^\"']*[\"']{1}",r"href=[\"']{1}[^\"']*[\"']{1}"]
re_src=[r"src=[\"']{1}[^\"'.]*[\"']{1}"]

def analysis(data):
	res_url=[]
	res_src=[]
	result={"next_url":"","src_url":""}

	for re_temp in re_url:
		pattern=re.compile(re_temp)
		temp_result=pattern.findall(data)
		res_url+=temp_result

	result['next_url']=res_url

	for re_temp in re_src:
		pattern=re.compile(re_temp)
		temp_result=pattern.findall(data)
		res_src+=temp_result

	result['src_url']=res_src

	print result
	return result


if __name__=='__main__':
	data=sys.stdin.read()
	analysis(data)
