#!/usr/bin/env python
# --*-- coding:utf-8 --*--
#目录类

import encrypt
import jt_global

class dirnode(object):
	#目录的名字
	__name=""
	#目录的权限
	__power=666
	#目录中保存的条目
	__childs=[]
	#目录不够的时候使用链接下n个块的位置
	__dirnexts=[]
	#保存的最小key
	__min=0
	#保存的最大key
	__max=0
	#一级块中的最小值
	__leve0_min=0
	#一级块中的最大值
	__leve0_max=0

	#初始化目录节点，传入的参数有两个：目录名name,权限控制power	
	def __init__(self,name,power=666):
		self.__name=name
		self.__power=power
		self.__min=0
		self.__max=0
		self.__leve0_min=0
		self.__leve0_max=0
	
	#获取目录的名字
	def getName(self):
		return self.__name

	#新增目录
	def mkdir(self,name):
		temp_dir=jt_file(name)
		
		#第一级目录没有满，可以放到里面.二分查找到相应位置并存放
		if len(self.__childs)<jt_global.dir_size:
			temp_key=encrypt.encrypt(name)
			self.__childs.insert(0,temp_dir)
		else :
			#循环所有的扩增数组看看有没有空的
			signal=0
			for item in self.__dirnexts:
				if not item.is_full():
					item.insert(0,temp_dir)
					signal=1

			if signal==0:
				temp_next=dirnext("abcdefg",0,0)
				temp_next.append(temp_dir)
				self.__dirnexts.insert(0,temp_next)
		return True

	#删除目录
	def rmdir(self,name):
		index=0
		for temp in self.__childs:
			if temp.getName()==name:
				self.__childs.pop(index)	
			index=index+1

	#重命名目录
	def rename(self,name):
		pass

	#显示目录中的内容
	def ls(self):
		#先显示当前模块中的文件或者目录
		for item in self.__childs:
			print item.getName()
		#显示扩增模块中的文件或者目录
		for item in self.__dirnexts:
			item.ls()
			

#目录类中定义的下一个块的位置
class dirnext(object):
	#给一个id，方便后面查找
	__id=0
	#块中保存的最小key
	__min=0
	#块中保存的最大key
	__max=0
	#list中保存的是块的位置，可以有多个备份
	__address=""
	
	def __init__(self,address,min_key,max_key):
		self.__address=address
		self.__max=max_key
		self.__min=min_key
	#判断当前块中是否满了
	def is_full(self):
		return False
	#在当前块中查找是否有相应的文件名
	def is_find(self,name):
		pass
	#显示当前块中的目录内容
	def ls(self):
		print "block ls %d" % (self.__id)

#保存在目录中的文件条目
class jt_file(object):
	__name=""
	__key=""
	__address=[]
	__power=666
	def __init__(self,name,power=666,address=[]):
		self.__name=name
		self.__power=power
		self.__address=address
		#将文件名转化为key
		self.__key=encrypt.jiami(self.__name)
	def getName(self):
		return self.__name
	def getKey(self):
		return self.__key
