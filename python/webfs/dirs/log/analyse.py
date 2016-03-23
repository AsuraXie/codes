#!/usr/bin/env python
# --*-- coding:utf-8 --*--
import math

def process(name):
	total=0
	count=0

	f=open('cmd/'+name,'r')
	res={}
	step=0.05
	m=step*1000

	for line in f.readlines():
		if line !="":
			temp=line.split(",")
			if len(temp)!=2:
				continue
			total=total+float(temp[0])
			count=count+1
			t=float(temp[0])*1000
			c=math.ceil(t/m)*m
			d=c/1000
			d=str(d)
			if d in res:
				res[d]+=1
			else:
				res[d]=1
	f.close()

	temp_file=open('res/'+name,'a')
	for item in res:
		temp_file.write(str(item)+" "+str(res[item])+"\n")
	temp_file.close()

	temp_file=open("avg/"+name,'w')
	if count!=0:
		temp_file.write(str(total/count))
	temp_file.close()

if __name__=="__main__":
	process("backup")
	process("mkdir")
	process("ls")
	process("cd")
	process("split")
	process("rmdir")
