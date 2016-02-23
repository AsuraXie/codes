#!/usr/bin/env python
# --*-- coding:utf-8 --*--
import os
import dirnode
import jt_global as GLOBAL
import jt_machine_list
import jt_common
import encrypt

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
#深度遍历
def digui(path,short,cnf):
	roots=os.listdir(path)
	mydirs=[]
	shortdirs=[]
	mc=jt_machine_list.machine("",cnf['data']['address'],cnf['data']['port'],"")
	res=jt_common.post(mc,"",{"cmd":"cd","index":cnf['data']['index'],"mypath":short})
	print "cd",short,res	
	mc=jt_machine_list.machine("",res['data']['address'],res['data']['port'],"")
	for item in roots:
		if os.path.isdir(path+os.sep+item):
			temp=path+os.sep+item
			mydirs.append(temp)
			shortdirs.append(item)
			res2=jt_common.post(mc,"",{"cmd":"mkdir","index":res['data']['index'],"mypath":item})
			print "mkdir",item,res2,res
			digui(temp,item,res)
	
if __name__=="__main__":
	GLOBAL.MacList=jt_machine_list.mList()
	mc=GLOBAL.MacList.getBestMC()
	#mc=jt_machine_list.machine("","127.0.0.1","8802","")
	res1=jt_common.post(mc,"",{"cmd":"mkdir","name":"root"})
	jt_common.post(mc,"",{"cmd":"mkdir","index":res1['data'],"mypath":"codes"})
	cnf={"data":{"address":"","port":"","index":""}}
	cnf['data']['address']=mc.getAddress()
	cnf['data']['port']=mc.getPort()
	cnf['data']['index']=res1['data']
	'''
	print res1
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
	digui("/home/asura/codes","codes",cnf)
