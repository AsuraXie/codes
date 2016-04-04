#!/usr/bin/env python
# --*-- coding:utf-8 --*--
import os
import dirnode
import jt_global as GLOBAL
import jt_machine_list
import jt_common
import encrypt
import jt_log

#广度遍历
def copydir(mc,index,path):
	roots=os.listdir(path)
	mydirs=[]
	for item in roots:
		if os.path.isdir(path+os.sep+item):
			mydirs.append(path+os.sep+item)
	
	while len(mydirs)>0:
		temp=mydirs.pop(0)
		res=jt_common.post(mc,"",{"cmd":"mkdir","index":index,"mypath":temp})
		print res
		curr=os.listdir(temp)
		for item in curr:
			if os.path.isdir(temp+os.sep+item):
				mydirs.append(temp+os.sep+item)

#深度遍历文件系统
def initdir(level,short,cnf):
	print "curr name :"+str(short)
	if level>=3:
		return
	mc=jt_machine_list.machine("",cnf['data']['mac'][0]['address'],cnf['data']['mac'][0]['port'],"")
	res=jt_common.post([mc],"",{"cmd":"cd","index":cnf['data']['index'],"mypath":short})
	mc=jt_machine_list.machine("",res['data']['mac'][0]['address'],res['data']['mac'][0]['port'],"")
	get_res=jt_common.post([mc],"",{"cmd":"get","index":res['data']['index']})
	for index in range(0,200):
		res2=jt_common.post([mc],"",{"cmd":"mkdir","index":res['data']['index'],"mypath":str(short)+str(index)})
		res3=jt_common.post([mc],"",{"cmd":"cd","index":res['data']['index'],"mypath":str(short)+str(index)})
		mc2=jt_machine_list.machine("",res3['data']['mac'][0]['address'],res3['data']['mac'][0]['port'],"")
		GLOBAL.curr_index=GLOBAL.curr_index+1
		size=jt_common.post([mc],"",{"syscmd":"getSize"})
		print size	
		size=size['data']
		jt_log.log.write("./log/data/size",str(GLOBAL.curr_index)+" "+str(size['total'])+" "+str(size['data']))
		get_res=jt_common.post([mc2],"",{"cmd":"get","index":res3['data']['index']})
		initdir(level+1,str(short)+str(index),res)

#深度遍历
def digui(path,short,cnf):
	roots=os.listdir(path)
	mydirs=[]
	shortdirs=[]
	print cnf
	mc=jt_machine_list.machine("",cnf['data']['mac'][0]['address'],cnf['data']['mac'][0]['port'],"")
	res=jt_common.post([mc],"",{"cmd":"cd","index":cnf['data']['index'],"mypath":short})
	print "cd",short,res	
	mc=jt_machine_list.machine("",res['data']['mac'][0]['address'],res['data']['mac'][0]['port'],"")
	for item in roots:
		if os.path.isdir(path+os.sep+item):
			temp=path+os.sep+item
			mydirs.append(temp)
			shortdirs.append(item)
			res2=jt_common.post([mc],"",{"cmd":"mkdir","index":res['data']['index'],"mypath":item})
			print "mkdir",item,res2,res
			digui(temp,item,res)
	
if __name__=="__main__":
	GLOBAL.MacList=jt_machine_list.mList()
	mc=GLOBAL.MacList.getBestMC()
	#mc=jt_machine_list.machine("","127.0.0.1","8802","")
	res1=jt_common.post([mc],"",{"cmd":"mkdir","name":"root"})
	jt_common.post([mc],"",{"cmd":"mkdir","index":res1['data'],"mypath":"x"})
	address={"address":"","port":""}
	address['address']=mc.getAddress()
	address['port']=mc.getPort()
	cnf={"data":{"mac":[],"index":res1['data']}}
	cnf['data']['mac']=[]
	cnf['data']['mac'].append(address)
	'''
	print jt_common.post(mc,"",{"cmd":"mkdir","index":res1['data'],"mypath":"home"})
	res2=jt_common.post(mc,"",{"cmd":"cd","index":res1['data'],"mypath":"home"})
	print res2
	print jt_common.post(mc,"",{"cmd":"mkdir","index":res2['data']['index'],"mypath":"xie"})
	res3=jt_common.post(mc,"",{"cmd":"cd","index":res2['data']['index'],"mypath":"xie"})
	print res3
	print jt_common.post(mc,"",{"cmd":"mkdir","index":res3['data']['index'],"mypath":"lixiang"})
	res4=jt_common.post(mc,"",{"cmd":"cd","index":res3['data']['index'],"mypath":"lixiang"})
	print res4
	'''
	print cnf
	#digui("/home/asura/dirtest","dirtest",cnf)
	initdir(1,"x",cnf)
