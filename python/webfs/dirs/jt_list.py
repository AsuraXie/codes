#!/usr/bin/env python
# --*-- coding:utf-8 --*--

#扩展的list结构
import encrypt

class xlist(object):
	__max=0x0
	__min=0x0
	__data={}
	__orderKey=[]
	
	#初始化list结构
	def __init__(self):
		self.__data={}
		self.__orderKey=[]
	
	#插入元素到指定位
	def insert(self,name,data):
		key=encrypt.jiami(str(name))
		bResult=self.bSearch(key)
		if not bResult['success']:
			index=bResult['index']

			if index==0 and len(self.__orderKey)==0:
				index=0
				self.__max=key
				self.__min=key
			else:
				index=index+1

			if self.__max<key:
				self.__max=key
			if self.__min>key:
				self.__min=key
			res=self.__orderKey.insert(index,key)
			self.__data[key]=data
			return True
		else:
			return False
	
	#删除结点
	def deleteByName(self,name):
		key=encrypt.jiami(name)
		res=self.bSearch(key)
		if res['success']==True:
			self.deleteByIndex(res['index'])
			return True
		else:
			return False

	#根据索引删除元素
	def deleteByIndex(self,index):
		if index<0 or index > len(self.__orderKey):
			return False

		key=self.__orderKey[index]
		self.__data.pop(key)
		self.__orderKey.pop(index)
	
	#二分查找
	def bSearch(self,key):
		start=0
		end=len(self.__orderKey)
		if end==0:
			return {'success':False,'index':0}

		mid=(start+end)/2
		signal=0
		while True:
			if start>=end:
				break;

			if self.__orderKey[mid]==key:
				signal=1
				break
			elif key<self.__orderKey[mid]:
				end=mid-1
			elif key>self.__orderKey[mid]:
				start=mid+1

			mid=(start+end)/2

		if signal==1:
			return {'success':True,'index':mid}
		else :
			return {'success':False,'index':mid}

	#弹出最小一个元素
	def min(self):
		if len(self.__orderKey)>0:
			key=self.__orderKey[0]
			return self.__data[key]
		else:
			return False
	#弹出最大一个元素
	def max(self):
		if len(self.__orderKey)>0:
			key=self.__orderKey[len(self.__orderKey)-1]
			return self.__data[key]
		else:
			return False
	
	#根据数组的下标返回结果
	def __getitem__(self,index):

		if index<0 or index >=len(self.__orderKey):
			return False
		else :
			key=self.__orderKey[index]
			return self.__data[key]

	#获取self.__min
	def getMin(self):
		return self.__min

	#获取self.__max
	def getMax(self):
		return self.__max

	#获取list的长度
	def getLength(self):
		return len(self.__orderKey)

	#获取所有条目	
	def getAll(self):
		result=[]
		for item in self.__orderKey:
			result.append(self.__data[item])
		return result

	def show(self):
		print self.__orderKey
		print self.__data
		print "min=%s" % self.__min
		print "max=%s" % self.__max

if __name__=='__main__':
	a=xlist()
	a.insert('a',['wokao'])
	b=a.bSearch('a')
	a.insert('b',['mimei'])
	c=a.bSearch('b')
	print b,c
	a.show()
