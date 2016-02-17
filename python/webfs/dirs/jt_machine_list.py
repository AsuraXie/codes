#!/usr/bin/env python
# --*-- coding:utf-8 --*--
#服务器列表

import jt_global as GLOBAL
import jt_list
import encrypt
import random
import socket
import jt_common
import jt_log

#机器对象，保存机器名称，地址，端口，各类属性，attr中包括weight
class machine(object):
	def __init__(self,name,address,port,attr):
		self.name=name
		if "http" in address or "www" in address or ":" in address or "/" in address:
			#如果传入的是url，需要转化为ip地址
			self.address=socket.getaddrinfo(address,None)
		else:
			self.address=address
		self.port=port
		self.attr=attr
		self.index=encrypt.jiami(name)

	def getName(self):
		return self.name

	def getAddress(self):
		return self.address
	
	def getPort(self):
		return self.port

	def getAttr(self,name):
		if name in self.attr:
			return self.attr[name]
		return False

	def setAttr(self,name,value):
		self.attr[name]=value

	def getIndex(self):
		return self.index

	#将所有内容已字符串的方式显示出来	
	def show(self):
		print "name:"+self.name+";address:"+self.address+";port:"+self.port+";"+self.__getAttrs__()

	#将属性转换为字符串处理
	def __getAttrs__(self):
		res=""
		for item in self.attr:
			res=res+"attr_name:"+str(item)+";attr_value:"+str(self.attr[item])
		return res
		

#机器列表
class mList(object):
	__m_list=''

	def __init__(self):
		self.__m_list=jt_list.xlist()
		for item in GLOBAL.remote_mac:
			t=machine(jt_common.getRandomName(),item['addr'],item['port'],{})
			t.setAttr("weight",0)
			self.__m_list.insert(t.getName(),t)

	def add(self,m):
		self.__m_list.insert(m.getName(),m)

	def delete(self,name):
		self.__m_list.deleteByName(name)

	def deleteByIndex(self,index):
		self.__m_list.deleteByIndex(index)	

	def modify(self,m):
		if self.__m_list.deleteByName(m.getName()):
			self.__m_list.insert(m.getName(),m)

	def getByName(self,name):
		index=encrypt.jiami(name)
		return self.__m_list.getByKey(index)

	def __getitem__(self,index):
		return self.__m_list[index]

	#获取当前最佳状态的机器
	def getBestMC(self):
		weight=1000000
		index=0
		length=self.__m_list.getLength()
		for i in range(0,length):
			address=self.__m_list[i].getAddress()
			port=self.__m_list[i].getPort()
			#不安排本机处理
			if str(address)==str(GLOBAL.local_addr) and str(port)==str(GLOBAL.local_port):
				continue
			if weight > self.__m_list[i].getAttr('weight'):
				weight=self.__m_list[i].getAttr('weight')
				index=i
		self.__m_list[index].setAttr("weight",weight+1)
		address=self.__m_list[index].getAddress()
		port=self.__m_list[index].getPort()
		if address==GLOBAL.local_addr and port==GLOBAL.local_port:
			jt_log.log.write(GLOBAL.error_log_path,"getBestMC error,get self")
		return self.__m_list[index]

	#更新所有的机器
	def refreshAll(self):
		length=self.__m_list.getLength()
		data=[]
		for i in range(0,length):
			data.append({"index":self.__m_list[i].getIndex(),"data":self.__m_list[i]})
		for i in range(0,length):
			jt_common.post(self.__m_list[i],"",{"syscmd":"refresh_mc","data":data})	

	def show(self):
		alldata=self.__m_list.getAll()
		for item in alldata:
			item.show()

if __name__=="__main__":
	mylist=mList()
	mylist=mList()
	for i in range(1,4):
		t=machine("node_"+str(i),"192.168.0."+str(i),random.randint(8900,9000),{'a':i,'b':2*i})
		mylist.add(t)
	for i in range(1,10):
		print mylist.getBestMC();
