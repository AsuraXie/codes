#!/usr/bin/env python
# --*-- coding:utf-8 --*--

import os
import dirnode
import jt_global as GLOBAL
import jt_machine_list
import jt_common
import encrypt
import jt_log
import random
import time,threading

def stress_test(mc,index,mypath):
	print mypath,threading.current_thread().name
	start=time.time()
	locate=jt_common.post(mc,"",{"cmd":"cd","index":index,"mypath":mypath})
	end=time.time()
	jt_log.log.write("./log/data/stress",str(end-start))
	if locate['code']==0:
		start=time.time()
		childs=jt_common.post(getRandomMac(locate['data']['mac']),"",{"cmd":"ls","index":locate['data']['index']})
		end=time.time()
		jt_log.log.write("./log/data/stress",str(end-start))
		if childs['code']!=0:
			return
		for item in childs['data']:
			name=item.split(":")[0]
			addr=item.split(":")[1].split(",")[0]
			port=item.split(":")[1].split(",")[1]
			mc=jt_machine_list.machine("",addr,port,"")
			stress_test([mc],locate['data']['index'],name)

#获取随即服务器地址
def getRandomMac(macs):
	count=len(macs)-1
	index=random.randint(0,count)
	mac=jt_machine_list.machine("",macs[index]['address'],macs[index]['port'],"")
	return [mac]

if __name__=="__main__":
	GLOBAL.MacList=jt_machine_list.mList()
	mc=GLOBAL.MacList.getBestMC()
	root=jt_common.post([mc],"",{"syscmd":"init","name":"root"})
	root_index=root['data']['index']
	root_macs=root['data']['mac']
	thread_arr=[]
	#stress_test(getRandomMac(root_macs),root_index,"x")
	for i in range(0,30):
		t=threading.Thread(target=stress_test,name="process_"+str(i),args=(getRandomMac(root_macs),root_index,"x"))
		thread_arr.append(t)
	for i in range(0,30):
		thread_arr[i].start()
	for i in range(0,30):
		thread_arr[i].join()
