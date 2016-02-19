#!/usr/bin/env python
import os
import dirnode
import jt_global as GLOBAL
import jt_machine_list
import jt_common
import encrypt

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

if __name__=="__main__":
	GLOBAL.MacList=jt_machine_list.mList()
	mc=GLOBAL.MacList.getBestMC()
	print mc.getPort()
	res1=jt_common.post(mc,"",{"cmd":"mkdir"})
	print jt_common.post(mc,"",{"cmd":"mkdir","index":[res1['data']],"mypath":"home"})
	print jt_common.post(mc,"",{"cmd":"mkdir","index":[res1['data']],"mypath":"xie"})
	print jt_common.post(mc,"",{"cmd":"mkdir","index":[res1['data']],"mypath":"lixiang"})
	print jt_common.post(mc,"",{"cmd":"ls","index":[res1['data']]})
	res=jt_common.post(mc,"",{"cmd":"cd","index":[res1['data']],"mypath":"home"})
	print jt_common.post(mc,"",{"cmd":"ls","index":res['data']['index']})
	print jt_common.post(mc,"",{"cmd":"mkdir","index":res['data']['index'],"mypath":"pj"})
	res2=jt_common.post(mc,"",{"cmd":"cd","index":res['data']['index'],"mypath":"pj"})
	print jt_common.post(mc,"",{"cmd":"rmdir","index":res['data']['index']})
	print jt_common.post(mc,"",{"cmd":"ls","index":[res1['data']]})
