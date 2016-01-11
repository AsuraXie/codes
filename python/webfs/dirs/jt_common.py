#!/usr/bin/env python
import os
import jt_log
def rename(path,name):
	dirs=path.split(os.sep)
	if name!="" and len(dirs)>1:
		temp_path=dirs[0:-1]
		new_name=os.sep.join(temp_path)+os.sep+name
	else:
		new_name=name
	print new_name

def pathFilter(path):
	dirs=path.split(os.sep)
	res={"path":"","file":"","filename":"","type":""}
	if len(dirs)>0:
		if len(dirs)==1:
			files=dirs[0].split('.')
			if len(files)==2:
				res['file']=dirs[0]
				res['filename']=files[0]
				res['type']=files[1]
		else:
			res['path']=os.sep.join(dirs[0:-1])
			res['file']=dirs[-1]
			files=dirs[-1].split('.')
			if len(files)==2:
				res['filename']=files[0]
				res['type']=files[1]
	return res

def cmds(path):
	res={}
	alls=path.split("?")
	if len(alls)>=1:
		res['path']=alls[0]
	if len(alls)>1:
		left_params=alls[1].split("&")
		for item in left_params:
			temp=item.split("=")
			if len(temp)==2:
				if temp[0] in res:
					jt_log.write("error","repeate key in url request")
					continue
				else:
					res[temp[0]]=temp[1]
	return res

if __name__=="__main__":
	rename("a.txt","b.txt")
	a=cmds("/home/asura/xielixiang/a.txt?cmd=rmdir&a=b&c=d&e=f")
	print a
	b=pathFilter("txt")
	print b
