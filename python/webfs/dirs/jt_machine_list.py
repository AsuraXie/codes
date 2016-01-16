#!/usr/bin/env python
# --*-- coding:utf-8 --*--
#服务器列表

import jt_global
import jt_list
import encrypt
import random
import socket

#机器对象，保存机器名称，地址，端口，各类属性，attr中包括weight
class machine(object):
	def __init__(self,name,address,port,attr):
		self.name=name
		if "http" in address or "www" in address or ":" in address or "/" in address:
			#是url，需要转化
			self.address=socket.getaddrinfo(address,None)
		else:
			self.address=address
		self.port=port
		self.attr=attr
		
		self.url=""
	def getName(self):
		return self.name

	def getAddress(self):
		return self.address
	
	def getPort(self):
		return self.port

	def getAttr(self,name):
		if name in self.attr:
			return self.attr[name]
		return 0

#机器列表
class mList(object):
	__m_list=''

	def __init__(self):
		for item in jt_global.remote_mac:
			t=machine(item['addr'],item['addr'],item['port'])
			print item
		self.__m_list=jt_list.xlist()

	def add(self,m):
		self.__m_list.insert(m.getName(),m)

	def delete(self,name):
		self.__m_list.deleteByName(name)

	def modify(self,m):
		if self.__m_list.deleteByName(m.getName()):
			self.__m_list.insert(m.getName(),m)

	def getByName(self,name):
		index=encrypt.jiami(name)
		return self.__m_list.getByKey(index)

	def __getitem__(self,index):
		return self.__m_list[index]

	def getBestMC(self):
		weight=0
		index=0
		length=self.__m_list.getLength()
		print length
		for i in range(1,length):
			if weight < self.__m_list[i].getAttr('weight'):
				weight=self.__m_list[i].getAttr('weight')
				index=i
		return self.__m_list[index]

	def show(self):
		self.__m_list.show()

if __name__=="__main__":
	mylist=mList()
	for i in range(1,4):
		t=machine("node_"+str(i),"192.168.0."+str(i),random.randint(8900,9000),{'a':i,'b':2*i})
		mylist.add(t)
	#mylist.show()
	mylist.delete('node_1')
	a=mylist.getByName('node_1')
	b=mylist.getByName('node_2')
	c=mylist.getByName('node_3')
	print a,b,c
	t=machine("node_1","192.168.0.111",random.randint(8900,9000),{"A":'b'})
	mylist.modify(t)
	a=mylist.getByName('node_1')
	print a
	print mylist.getBestMC();
