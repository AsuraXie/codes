#!/usr/bin/env python
# --*-- coding:utf-8 --*--
import jt_global as GLOBAL
import jt_common
import jt_machine_list

if __name__=="__main__":
	GLOBAL.MacList=jt_machine_list.mList()
	print GLOBAL.MacList.show()
	for i in range(1,20):
		mc=GLOBAL.MacList.getBestMC() 
		print mc.show()
		GLOBAL.MacList.refreshAll()	
