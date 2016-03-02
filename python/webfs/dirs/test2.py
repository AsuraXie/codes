#!/usr/bin/env python
# --*-- coding:utf-8 --*--
import jt_global as GLOBAL
import jt_common
import jt_machine_list

if __name__=="__main__":
	mc2=jt_machine_list.machine("test machine","127.0.0.1","8802","")
	mc3=jt_machine_list.machine("test machine2","127.0.0.1","8803","")
	mc4=jt_machine_list.machine("test machine3","127.0.0.1","8804","")
	res=jt_common.get(mc2,"",{"cmd":"ls","index":"63a9f0ea7bb98050796b649e85481845"})
	#temp=jt_common.get(mc,"",{"cmd":"cd","index":"63a9f0ea7bb98050796b649e85481845","mypath":"codes"})	
	print res
	#print temp
	#res2=jt_common.get(mc2,"",{"cmd":"ls","index":"80ddcff0b5d0e9646166b4672def90ee"})
	#print res2
	#temp2=jt_common.get(mc2,"",{"cmd":"cd","index":"80ddcff0b5d0e9646166b4672def90ee","mypath":"howto"})
	#print temp2
	#res2=jt_common.get(mc,"",{"cmd":"ls","index":"d41d8cd98f00b204e9800998ecf8427e;23eeeb4347bdd26bfc6b7ee9a3b755dd;82ad9b26019ac203c2f22d8f0d8d3cc4;e3e2a9bfd88566b05001b02a3f51d286"})
	#print res2
