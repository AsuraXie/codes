#!/usr/bin/env python
# --*-- coding:utf-8 --*--
import dirnode
import encrypt

if __name__=='__main__':
	a=dirnode.dirnode("谢莉祥",4)
	print a.getName()
	for i in range(1,25):
		a.mkdir(i)
	a.ls()
