#!/usr/bin/env python
# --*-- coding:utf-8 --*--
#目录类

import encrypt
import jt_global
import jt_list

class dirnode(object):
	#目录的名字
	__name=""
	#目录的权限
	__power=666
	#目录中保存的条目
	__childs=0
	#目录不够的时候使用链接下n个块的位置
	__dirnexts=0
	#根据名字加密的主键
	__key=""
	#初始化目录节点，传入的参数有两个：目录名name,权限控制power	
	def __init__(self,name,power=666):
		self.__name=name
		self.__power=power
		self.__key=encrypt.jiami(self.__name)
		self.__childs=jt_list.xlist()
		self.__dirnexts=jt_list.xlist()
	
	#获取目录的名字
	def getName(self):
		return self.__name
	#获取目录的主键
	def getKey(self):
		return self.__key
	
	def getLength(self):
		pass

	#新增目录
	def mkdir(self,name):
		temp_dir=dirnode(name)
		temp_max=False

		#第一级目录没有满，可以放到里面.
		if self.__childs.getLength()<jt_global.dir_size:
			self.__childs.insert(name,temp_dir)
			return True
		#如果第一级目录满了，并且key小于最大值则插入进去后取出最大值放到下一个块中
		elif temp_dir.getKey()<self.__childs.getMax():
			self.__childs.insert(name,temp_dir)
			temp_max=self.__childs.max()
			self.__childs.deleteByName(temp_max.getName())
		else:
			temp_max=temp_dir

		#当前有一个巨大块，需要插入到链表中,需要明确的是：块不满则插入，满了则需要分裂	
		if temp_max:
			if self.__dirnexts.getLength()==0:
				temp_next_dir=dirnext(name,0,0)
				self.__dirnexts.insert(temp_max.getName(),temp_next_dir)
	
			target_block_index=self.__dirnexts.bSearch(temp_max.getName())
			if not target_block_index['success']:
				if target_block_index['index']==0 and self.__dirnexts.getLength()==0:
					target_block_index['index']=0
				else:
					target_block_index['index']=target_block_index['index']+1
			
			if self.__dirnexts[target_block_index['index']].getLength()<jt_global.dir_next_size:
				self.__dirnexts[target_block_index['index']].insert(temp_max.getName(),temp_max)
			else:
				#如何分裂模块
				new_block=self.__dirnexts[target_block_index['index']].split(temp_max.getKey())
				self.__dirnexts.deleteByIndex(target_block_index['index'])
				if new_block['pre'].getLength()<new_block['next'].getLength():
					new_block['pre'].insert(temp_max.getKey(),temp_max)
				else:
					new_block['next'].insert(temp_max.getKey(),temp_max)

				self.__dirnexts.insert(new_block['pre'].getName(),new_block['pre'])
				self.__dirnexts.insert(new_block['next'].getName(),new_block['next'])
		return True

	#删除目录
	def rmdir(self,name):
		key=encrypt.jiami(name)
		if key>=self.__childs.getMin() and key<=self.__childs.getMax():
			self.__childs.removeByKey(name)
			return True	

	#重命名目录
	def rename(self,name):
		pass

	#显示目录中的内容
	def ls(self):
		#self.__childs.show()
		alls=self.__childs.getAll()
		for item in alls:
			print item.getName()
		for item in self.__dirnexts.getAll():
			if item.getLength()>0:
				item.ls()

#目录类中定义的下一个块的位置
class dirnext(object):
	#块中保存的最小key
	__min=0
	#块中保存的最大key
	__max=0
	#list中保存的是块的位置，可以有多个备份
	__address=""
	#暂时用来保存数据以便单机测试
	__temp_list=[]
	#初始化
	def __init__(self,address,min_key=0,max_key=0):
		self.__address=address
		self.__max=max_key
		self.__min=min_key
		self.__temp_list=jt_list.xlist()

	#在当前块中查找是否有相应的文件名
	def is_find(self,name):
		pass

	#显示当前块中的目录内容
	def ls(self):
		alls=self.__temp_list.getAll()
		for item in alls:
			item.ls()
		return self.__temp_list.getLength()

	#插入记录到块中
	def insert(self,name,data):
		return self.__temp_list.insert(name,data)
	
	#重写get函数
	def __getitem__(self,index):
		return self.__temp_list[index]

	#获取地址
	def getAddress(self):
		return self.__address

	#获取最大的名称
	def getName(self):
		temp_dir=self.__temp_list.max()
		if temp_dir:
			return temp_dir.getName()
		else:
			return False

	#获取当前存储内容的长度
	def getLength(self):
		return self.__temp_list.getLength()
	
	#获取所有的内容
	def getAll(self):
		result=[]
		while True:
			temp=self.__temp_list.pop()
			if temp:
				result.append(temp)
			else:
				break
		return result

	#根据key将数据拆分成两个块
	def split(self,key):
		temp_pre=dirnext("a",666)
		temp_next=dirnext("b",666)
		allkeys=self.getAll()
	
		for item in allkeys:
			if item.getKey()>key:
				temp_next.insert(item.getName(),item)
			else:
				temp_pre.insert(item.getName(),item)
		res={"pre":temp_pre,"next":temp_next}
		return res

#保存在目录中的文件条目
class jt_file(object):
	__name=""
	__key=""
	__address=[]
	__power=666
	__type=0

	def __init__(self,name,power=666,address=[]):
		self.__name=name
		self.__power=power
		self.__address=address
		#将文件名转化为key
		self.__key=encrypt.jiami(self.__name)

	#获取名字
	def getName(self):
		return self.__name

	#获取主键
	def getKey(self):
		return self.__key

	#显示当前结点信息
	def ls(self):
		print self.__name
