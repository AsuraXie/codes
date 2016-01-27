#!/usr/bin/env python
# --*-- coding:utf-8 --*--
import dirnode
import jt_machine_list
import jt_list
import jt_global as GLOBAL
import jt_common

if __name__=="__main__":
	GLOBAL.MacList=jt_machine_list.mList()
	GLOBAL.LocalData=jt_list.xlist()
	mac=GLOBAL.MacList.getBestMC()
	res=jt_common.post(mac,"",{"cmd":"mkdirnext","mypath":"home"})
	print res	
	
	for i in range(1,40):
		temp=dirnode.dirnode(str(i),"")
		res2=jt_common.post(mac,"",{"cmd":"insert","dirnode":temp,"index":res['data']})

	print jt_common.post(mac,"",{"cmd":"ls","index":res['data']})
	res3=jt_common.post(mac,"",{"cmd":"mkdirnext","mypath":"asura"})
	print res3
	print jt_common.post(mac,"",{"cmd":"split","mac":mac,"index":res['data'],"target_index":res3['data']})
	print jt_common.post(mac,"",{"cmd":"ls","index":res['data']})
	print jt_common.post(mac,"",{"cmd":"ls","index":res3['data']})
