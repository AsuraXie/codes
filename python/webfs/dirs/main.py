#!/usr/bin/env python
# --*-- coding:utf-8 --*--
import dirnode
import encrypt
import sys
import random
import jt_common
import jt_log

def process(params):
	global ROOT
	try:
		if 'cmd' in params and 'path' in params:
			if params['cmd']=='mkdir':
				ROOT.mkdir2(params['path'])
			elif params['cmd']=='rename' and 'name' in params:
				ROOT.rename(params['path'],params['name'])
			elif params['cmd']=='rmdir':
				ROOT.rmdir(params['path'])
			elif params['cmd']=='find':
				ROOT[params['path']]
			elif params['cmd']=='add':
				print "add"
				pass
			elif params['cmd']=="rm":
				print "rm"
				pass
			elif params['cmd']=="ls":
				a=ROOT[params['path']]
				if isinstance(a,dirnode.dirnode):
					return a.ls2()
				else:
					return "not found path"
			elif params['cmd']=="cd":
				ROOT[params['path']]
			return {"code":0,"msg":"success","data":""}
		else:
			return {"code":0,"msg":"error cmd","data":""}
	except Exception,e:
		jt_log.log.write('log/data/error.log','error in process cmd')
		return {"code":-1,"msg":"error","data":""}
	
if __name__=='__main__':
	a=dirnode.dirnode("/")
	a.mkdir2("home/asura/codes/python/webfs/dirs/a/b/c")
	a.mkdir2("home/asura/codes/python/webfs/dirs/f/e/c")
	#a.ls()
	a.rename("home/asura/codes","home/asurar/ttt")
	#a.ls()
