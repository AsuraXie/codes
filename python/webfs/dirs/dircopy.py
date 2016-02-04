#!/usr/bin/env python
import os
import dirnode
import jt_global as GLOBAL
import jt_machine_list
import jt_common

def copydir(mc,index,path):
	count=0
	roots=os.listdir(path)
	mydirs=[]
	for item in roots:
		if os.path.isdir(path+os.sep+item):
			mydirs.append(path+os.sep+item)
			count=count+1
	
	while len(mydirs)>0:
		temp=mydirs.pop(0)
		print temp
		jt_common.post(mc,"",{"cmd":"mkdir","index":index,"mypath":temp})
		curr=os.listdir(temp)
		for item in curr:
			if os.path.isdir(temp+os.sep+item):
				mydirs.append(temp+os.sep+item)
				count=count+1

if __name__=="__main__":
	GLOBAL.MacList=jt_machine_list.mList()
	mc=GLOBAL.MacList.getBestMC()
	res=jt_common.post(mc,"",{"cmd":"mkdir"})
	copydir(mc,res['data'],"/home/asura/dirtest")
	print jt_common.post(mc,"",{"cmd":"ls","mypath":"/home/asura/dirtest"})
	print "db"
