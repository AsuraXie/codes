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
	#mac=GLOBAL.MacList.getBestMC()
	mac=jt_machine_list.machine("abcdefg","127.0.0.1","8803",{})
	mac2=jt_machine_list.machine("aworie","127.0.0.1","8802",{})
	res=jt_common.post(mac,"",{"cmd":"mkdirnext","mypath":"home"})
	for i in range(1,40):
		temp=dirnode.dirnode(str(i),"")
		res2=jt_common.post(mac,"",{"cmd":"insert","dirnode":temp,"index":res['data']})

	print jt_common.post(mac,"",{"cmd":"ls","index":res['data']})
	temp=dirnode.dirnode(str(10),"")
	res3=jt_common.post(mac2,"",{"cmd":"mkdirnext","mypath":"asura"})
	print res3
	print jt_common.post(mac,"",{"cmd":"split","mac":mac2,"index":res['data'],"target_index":res3['data']})
	
	print jt_common.post(mac,"",{"cmd":"ls","index":res['data']})
	print jt_common.post(mac2,"",{"cmd":"ls","index":res3['data']})
