#!/usr/bin/env python
import os
import dirnode

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
		root.mkdir2(temp)
		curr=os.listdir(temp)
		for item in curr:
			if os.path.isdir(temp+os.sep+item):
				mydirs.append(temp+os.sep+item)
				count=count+1
	#a=root['/home/asura/codes/python']
	#return a.ls2()
	#print "total file:"+str(count)

if __name__=="__main__":
	root=dirnode.dirnode("/")
	copydir(root,"/home/asura/codes/python")
	b=root['/home/asura/codes/python']
	print b.ls2()
	print b.ls2()
	#print b.ls()
