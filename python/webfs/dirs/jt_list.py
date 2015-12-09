#!/usr/bin/env python
# --*-- coding:utf-8 --*--

#扩展的list结构
import encrypt
class xlist(object):
	__max=0
	__min=0
	__data={}
	__orderKey=[]
	
	#初始化list结构
	def __init__(self):
		self.__data={}
		self.__orderKey=[]
	
	#插入元素到指定位置
	def insert(self,data):
		key=encrypt.jiami(str(data))
		self.__data[key]=data
		bResult=self.bSearch(key)
		print self.__orderKey
		if not bResult['success']:
			index=bResult['index']
			res=self.__orderKey.insert(index,key)
			return True
		else:
			self.__data.pop(key)
			return False

	
	#删除结点
	def deleteByKey(self,data):
		key=encrypt.jiami(data)
		res=self.bSearch(data)
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
	def bSearch(self,data):
		start=0
		end=len(self.__orderKey)
		mid=(start+end)/2
		signal=0
		while True:
			if start>=end:
				break
			if self.__orderKey[mid]==data:
				signal=1
				break
			elif self.__orderKey[mid]>data:
				end=mid-1
				if end<0:
					end=0
				mid=(start+end)/2
				continue 
			elif self.__orderKey[mid]<data:
				start=mid+1
				mid=(start+end)/2
				continue
			else:
				break

		if signal==1:
			return {'success':True,'index':mid,'data':self.__orderKey[mid]}
		else :
			return {'success':False,'index':mid}

	#弹出最后一个元素
	def min(self):
		if len(self.__orderKey)>0:
			key=self.__orderKey[0]
			return self.__data[key]
		else:
			return False

	def max(self):
		if len(self.__orderKey)>0:
			key=self.__orderKey[len(self.__orderKey)-1]
			return self.__data[key]
		else:
			return False
	
	#根据数组的下标返回结果
	def get(self,index):
		if index<0 or index >=len(self.__orderKey):
			return False
		else :
			key=self.__orderKey[index]
			return self.__data[key]

	def show(self):
		print self.__orderKey
		#print self.__data

	def judge(self):
		i=0
		while i < len(self.__orderKey)-1:
			if self.__orderKey[i]<self.__orderKey[i+1]:
				print 'yes'
			else:
				print 'no'
			i=i+1

if __name__=='__main__':
	a=xlist()
	for i in range(0,5):
		a.insert(i)
	a.judge()
	#a.show()
