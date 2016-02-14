#!/usr/bin/env python
# --*-- coding:utf-8 --*--
import os
import jt_log
import httplib,urllib
import socket
import jt_machine_list
import random
import jt_global as GLOBAL
import traceback
try:
	import cPickle as pickle
except ImportError:
	import pickle

#重名名/home/asura/python + aws = /home/asura/aws
def rename(path,name):
	dirs=path.split(os.sep)
	if name!="" and len(dirs)>1:
		temp_path=dirs[0:-1]
		new_name=os.sep.join(temp_path)+os.sep+name
	else:
		new_name=name
	print new_name

#
def dictToString(mdict):
	res=""
	for k in mdict:
		v=mdict[k]
		if isinstance(v,str) or isinstance(v,int) or isinstance(v,float):
			res=res+str(k)+":"+str(v)+";"
		else:
			res=res+str(k)+":unknow;"
	return res

#名字解析
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

#将名字切分
def pathSplit(path):
	names=path.split(os.sep)
	name=""
	name_left=""
	index=0
	for item in names:
		index=index+1
		if item!="":
			name=item
			break
	name_left=os.sep.join(names[index:])
	return {"name":name,"name_left":name_left}

#解析命令
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

#获取随机的名字
def getRandomName(count=8):
	origin_str="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	length=len(origin_str)
	res=""
	i=0
	while i < count:
		index=random.randint(0,length-1)
		res=res+origin_str[index]
		i=i+1
	return res
		

#调用GET方法
def get(machine,dirs,params):
	try:
		#解析命令参数
		cmds=urllib.urlencode(params)
		conn=httplib.HTTPConnection(machine.getAddress(),machine.getPort(),GLOBAL.time_out)
		conn.request("GET",dirs+"?"+cmds)
		res=conn.getresponse()
		if res.status==200 and res.reason=="OK":
			return pickle.loads(res.read())
		else:
			jt_log.log.write("log/data/error.log","jt_common,get"+res.read())
			return False
	except Exception,e:
		traceback.print_exc()
		jt_log.log.write(GLOBAL.error_log_path,"get error"+e.message)

#调用POST方法
def post(machine,dirs,params):
	try:
		#params=urllib.urlencode(params)
		params=pickle.dumps(params)
		headers={"Content-type":"application/x-www-form-urlencoded","Accept":"text/plain"}
		conn=httplib.HTTPConnection(machine.getAddress(),machine.getPort(),GLOBAL.time_out)
		conn.request("POST",dirs,params,headers)
		res=conn.getresponse()
		if res.status==200 and res.reason=='OK':
			return pickle.loads(res.read())
		else:
			jt_log.log.write("log/data/error.log","jt_common,post"+res.read())
			return False
	except Exception,e:
		traceback.print_exc()
		jt_log.log.write(GLOBAL.error_log_path,"post error"+e.message)

if __name__=="__main__":
	rename("a.txt","b.txt")
	a=cmds("/home/asura/xielixiang/a.txt?cmd=rmdir&a=b&c=d&e=f")
	#print a
	b=pathFilter("txt")
	#print b
	mac=jt_machine_list.machine("test","127.0.0.1",8802,{'a':'b'})
	#print get(mac,'/index.html',{"cmd":"ls"})
	#print post(mac,"/index.html",{"cmd":"ls"},{"a":"b","p":3,"d":'ebe'})
	print getRandomName()
	print getRandomName()
	print pathSplit("/home/asura/xielixiang")
	print pathSplit("/home")
	print pathSplit("/home/")
	print pathSplit("home")
	print pathSplit("/home/asura")
	print pathSplit("/home/asura/")
