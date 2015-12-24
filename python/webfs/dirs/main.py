#!/usr/bin/env python
# --*-- coding:utf-8 --*--
import dirnode
import encrypt
import sys
import random

if __name__=='__main__':
	a=dirnode.dirnode("/")
	a.mkdir2("home/asura/codes/python/webfs/dirs/a/b/c")
	temp=a["/home/asura/codes/python/webfs/dirs"]
	temp.setName("aa")
	if isinstance(temp,dirnode.dirnode):
		print "------------"+temp.getName()
	#a.rmdir("hello")
	a.ls()
