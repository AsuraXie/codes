#!/usr/bin/env python
# --*-- coding:utf-8 --*--
import dirnode
import encrypt
import sys
import random

if __name__=='__main__':
	#a=dirnode.dirnode("root",4)
	#print a.getName()
	#start=int(sys.argv[1])
	#end=int(sys.argv[2])
	#print str(start)+"----"+str(end)
	#for i in range(start,end):
	#	a.mkdir(i)
	#for i in range(start,end):
	#	temp=a[i]
	#	if temp<0:
	#		print "wrong index="+str(temp)+";start="+str(start)+",end="+str(end) 	
	n=0
	while n<100:
		a=dirnode.dirnode("root",4)
		print a.getName()
		n+=1
		start=random.randint(10,200)
		end=random.randint(200,800)
		for i in range(start,end):
			a.mkdir(i)
	
		for i in range(start,end):
			temp=a[i]
			if temp<0:
				print "wrong index="+str(temp)+";start="+str(start)+",end="+str(end)
	print "GAME OVER!!!"
		
