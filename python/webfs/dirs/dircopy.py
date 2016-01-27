#!/usr/bin/env python
import os
import dirnode
import jt_global as GLOBAL
import jt_machine_list

def copydir(root,path):
	count=0
	roots=os.listdir(path)
	mydirs=[]
	for item in roots:
		if os.path.isdir(path+os.sep+item):
			mydirs.append(path+os.sep+item)
			count=count+1
	
	while len(mydirs)>0:
		temp=mydirs.pop(0)
		root.mkdir(temp)
		curr=os.listdir(temp)
		for item in curr:
			if os.path.isdir(temp+os.sep+item):
				mydirs.append(temp+os.sep+item)
				count=count+1
	#a=root['/home/asura/codes/python']
	#return a.ls2()
	#print "total file:"+str(count)

if __name__=="__main__":
	GLOBAL.MacList=jt_machine_list.mList()
	root=dirnode.dirnode("home","")
	copydir(root,"/home/asura/codes/python")
	root.mkdir("/home/asura/codes/python/a/b/c")
	b=root['/home/asura/codes/python/game']
	print b.ls2()
	print b.getFullName()
