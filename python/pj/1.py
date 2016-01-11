#!/usr/bin/env python 
n=0
s=0
m=0
x=[]
y=[]

def init():
	f=open("input","r")
	data=f.readlines()
	global n,s,m,x,y
	n=data[0].strip()
	s=data[1].strip()
	m=data[2].strip()
	k=3
	for i in range(0,int(n)):
		a=data[k].strip()
		x.append(a.split(" "))
		k=k+1
	for j in range(0,int(n)):
		a=data[k].strip()
		y.append(a.split(" "))
		k=k+1

def sum_x_S(i,list_j):
	global x
	res=0
	for index in list_j:
		res=res+float(x[index-1][i])
	return res

def sum_y_S(list_r,j):
	global y
	res=0
	for index in list_r:
		res=res+float(y[index-1][j])
	return res

def generateFull(data):
	res=[]
	for index in range(1,len(data)):
		temp=generateS(index,data)
		for item in temp:
			res.append(item)
	res.append(data)
	return res

def generateS(n,data):
	res=[]
	if len(data) > n and n > 0:
		for i in range(0,len(data)):
			temp=[]
			for item in data:
				temp.append(item)
			temp.pop(i)
			temp_res=generateS(n-1,temp)
			if len(temp_res)==0:
				res_temp=[]
				res_temp.append(int(data[i]))
				res.append(res_temp)
				continue
			for item in temp_res:
				item.append(data[i])
				res.append(item)
	return duplicateRemove(res)

def duplicateRemove(res):
	del_index=[]
	for a in range(0,len(res)):
		b=a
		while b < len(res):
			if a!=b and compare(res[a],res[b]) and not b in del_index:
				del_index.append(b)
			b=b+1
	if len(del_index)>0:
		del_index.sort()
	k=0
	for item in del_index:
		res.pop(item-k)
		k=k+1
	return res

def compare(a,b):
	for i in a:
		signal=0
		for j in b:
			if int(i)==int(j):
				signal=1
				break
		if signal==0:
			return  False
	return True

def calculate():
	global n
	global s
	global m
	w=generateFull(range(1,int(n)+1))
	for item in w:
		i=0
		while i < int(s):
			res="u"+str(i)+"*"+str(sum_y_S(item,i))
			j=0
			while j < int(m):
				res=res+"-v"+str(j)+"*"+str(sum_x_S(j,item))
				j=j+1
			i=i+1
			print res
	pass

if __name__=="__main__":
	init()
	calculate()
