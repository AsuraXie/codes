#!/usr/bin/env python
# --*-- coding:utf-8 --*--
import dirnode
import encrypt
import sys

if __name__=='__main__':
	a=dirnode.dirnode("root",4)
	print a.getName()
	start=int(sys.argv[1])
	end=int(sys.argv[2])
	print str(start)+"----"+str(end)
	for i in range(start,end):
		a.mkdir(i)
	a.ls()
