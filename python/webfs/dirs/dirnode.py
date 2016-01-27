#!/usr/bin/env python
# --*-- coding:utf-8 --*--
#目录类
import os
import pdb
import encrypt
import jt_global as GLOBAL
import jt_list
import jt_common
import jt_machine_list
import traceback
import jt_log

class dirnode(object):
	#上级目录的全路径
	__parent_name=""
	#目录的名字
	__name=""
	#目录的权限
	__power=666
	#目录中保存的条目 __childs=0
	__childs=0
	#目录不够的时候使用链接下n个块的位置
	__dirnexts=0
	#根据名字加密的主键
	__key=""
	#初始化目录节点，传入的参数有两个：目录名name,权限控制power	
	def __init__(self,name,parent_name,power=666):
		self.__name=str(name)
		self.__parent_name=parent_name
		self.__power=power
		self.__key=encrypt.jiami(self.__name)
		self.__childs=jt_list.xlist()
		self.__dirnexts=jt_list.xlist()
	
	#获取目录的名字
	def getName(self):
		return self.__name

	def getFullName(self):
		return self.__parent_name+"/"+self.__name

	#更改名字
	def setName(self,name):
		self.__name=name
		self.__key=encrypt.jiami(name)
		
	#获取目录的主键
	def getKey(self):
		return self.__key

	#获取列表长度	
	def getLength(self):
		pass

	#新增目录
	def mkdir(self,path):
		if path=="":
			return 0
		temp_path=jt_common.pathSplit(path)
		name=temp_path['name']
		name_left=temp_path['name_left']

		temp_dir=dirnode(name,self.__parent_name+"/"+self.__name)
		temp_max=False

		#第一级目录没有满，可以放到里面.
		if self.__childs.getLength()<GLOBAL.dir_size:
			if self.__childs.insert(name,temp_dir)<0:
				return -1
			else:
				#递归生成目录
				temp_dir.mkdir(name_left)
				return 0

		#如果第一级目录满了，并且key小于最大值则插入进去后取出最大值放到下一个块中
		elif temp_dir.getKey()<self.__childs.getMax():
			if self.__childs.insert(name,temp_dir)<0:
				return -2
			temp_max=self.__childs.max()
			self.__childs.deleteByName(temp_max.getName())
		else:
			temp_max=temp_dir

		#当前有一个巨大块，需要插入到链表中,需要明确的是：块不满则插入，满了则需要分裂	
		if temp_max:
			temp_max.mkdir(name_left)
			if self.__dirnexts.getLength()==0:
				temp_next_dir=dirnext(GLOBAL.MacList.getBestMC(),0,0)
				if self.__dirnexts.insert(temp_max.getName(),temp_next_dir)<0:
					return -3

			target_block_index=self.__dirnexts.bSearch(temp_max.getKey())
			
			if not target_block_index['success']:
				if target_block_index['index']<=0 or self.__dirnexts.getLength()==0:
					target_block_index['index']=0

			temp_max_key=self.__dirnexts[target_block_index['index']].getMaxKey()
       		        temp_min_key=self.__dirnexts[target_block_index['index']].getMinKey()

			if temp_max.getKey()>temp_max_key and target_block_index['index']<self.__dirnexts.getLength()-1:
               		   	target_block_index['index']+=1
               		elif temp_max.getKey()<temp_min_key and target_block_index['index']>=1:
		           	target_block_index['index']-=1

			if self.__dirnexts[target_block_index['index']].getLength()<GLOBAL.dir_next_size:
				if self.__dirnexts[target_block_index['index']].insert(temp_max.getName(),temp_max)<0:
					return -4
			else:
				#先获取一个目标地址
				new_dirnext_address=GLOBAL.MacList.getBestMC()
				#生成一个链接块
				new_dirnext=dirnext(new_dirnext_address)
				#分裂旧的块
				new_block=self.__dirnexts[target_block_index['index']].split(new_dirnext)
				#将新块插入到链表中
				if new_block!=False:
					self.__dirnexts.insert("",new_block)
					old_block=self.__dirnexts[target_block_index['index']]
					if temp_max.getKey()>old_block.getMaxKey():
						new_block.insert(temp_max.getName(),temp_max)
					else:
						old_block.insert(temp_max.getName(),temp_max)
					return 0
				else:
					print "block split faile"
		return 0

	#删除目录
	def rmdir(self,path):
		if path=="":                                                     		
                	print "empty path"
                	return
                                                                                 
                temp_name=jt_common.pathSplit(path)
		name=temp_name['name']
		name_left=temp_name['name_left']

		key=encrypt.jiami(name)
		if key>=self.__childs.getMin() and key<=self.__childs.getMax():
                	res=self.__childs.bSearch(key)
                	if res['success']:
                		if name_left!="":#如果不是最后一层
                			self.__childs[res['index']].rmdir(name_left)
				else:
					self.__childs.deleteByIndex(res['index'])
                	else:
                		return -1
                else:
                	res=self.__dirnexts.bSearch(key)
                	if res['index']<=0:
                		res['index']=0
                	if self.__dirnexts.getLength()==0:
                		return -4
                	temp=self.__dirnexts[res['index']]
                	if not isinstance(temp,bool):
                		temp_max=temp.getMaxKey()
                		temp_min=temp.getMinKey()

                		if key>temp_max and res['index']<temp.getLength()-1:
                			res['index']+=1
                			temp=self.__dirnexts[res['index']]
                		elif key<temp_min and res['index']>=1:
                			res['index']-=1
                			temp=self.__dirnexts[res['index']]

				if name_left!="":
					temp.rmdir(name_left,key)
				else:
					temp.deleteByName(name,key)
                	else:
                		return -3
	
	#获取目录或者文件
	def __getitem__(self,path):
		if path=="":
			print "empty path"
			return False

		temp_name=jt_common.pathSplit(path)
		name=temp_name['name']
		name_left=temp_name['name_left']
		
		key=encrypt.jiami(name)
		if name==self.__name:
			if name_left=="":
				return self
			else:
				return self[name_left]

		if key>=self.__childs.getMin() and key<=self.__childs.getMax():
			res=self.__childs.bSearch(key)
			if res['success']:
				if name_left=="":#如果是最后一层
					return self.__childs[res['index']]
				else:
					return self.__childs[res['index']][name_left]
			else:
				return False
		else:
			res=self.__dirnexts.bSearch(key)
			if res['index']<=0:
				res['index']=0

			if self.__dirnexts.getLength()==0:
				return False

			temp=self.__dirnexts[res['index']]
			if not isinstance(temp,bool):
				temp_max=temp.getMaxKey()
				temp_min=temp.getMinKey()

				if key>temp_max and res['index']<self.__dirnexts.getLength()-1:
					res['index']+=1
					temp=self.__dirnexts[res['index']]
				elif key<temp_min and res['index']>=1:
					res['index']-=1
					temp=self.__dirnexts[res['index']]
			
				if isinstance(temp,bool):
					return False
				if name_left=="":
					return temp.getByKey(key)
				else:
					return temp.getByName(name_left)
			else:
				return False                                                           


	#重命名目录
	def rename(self,old_name,new_name):
		if old_name==new_name:
			print "name equal"
			return
		name_list_1=old_name.split('/')
		name_list_2=new_name.split('/')
		if len(name_list_1)==len(name_list_2):
			i=0
			while i<len(name_list_1)-1:
				if name_list_1[i]!=name_list_2[i]:
					print "wrong new name"
					return
				i=i+1
		else:
			print "wrong new name"
			return

		old_node=self[old_name]
		if isinstance(old_node,dirnode):
			self.mkdir2(new_name)
			curr_node=self[new_name]
			if isinstance(curr_node,dirnode):
				curr_node._dirnode__childs=old_node._dirnode__childs
				curr_node._dirnode__dirnexts=old_node._dirnode__dirnexts
				self.rmdir(old_name)
			else:
				print "rename fail 1"
		else:
			print "rename fail 2"

	#显示目录中的内容
	def ls(self,level=0):
		count=0
		blank=""
		while count<level:
			blank+="  "
			count+=1
		print blank+self.getName()
		alls=self.__childs.getAll()
		blank+=" "
		for item in alls:
			item.ls(level+1)
	
		alls=self.__dirnexts.getAll()
		for item in alls:
			if item.getLength()>0:
				item.ls(level+1)

	def ls2(self):
		try:
			res=[]
			alls_childs=self.__childs.getAll()
			for item in alls_childs:
				res.append(item.getName())
			alls_nexts=self.__dirnexts.getAll()
			for item in alls_nexts:
				if item.getLength():
					temp=item.getAll()
					for temp_item in temp:
						res.append(temp_item.getName())
			return res
		except Exception,e:
			traceback.print_exc()
			jt_log.log.write(GLOBAL.error_log_path,e.message)
			return False

#目录类中定义的下一个块的位置
class dirnext(object):
	#块中保存的最小key
	__min=0
	#块中保存的最大key
	__max=0
	#list中保存的是块的位置，可以有多个备份
	__address=""
	#对应目标机中保存的索引
	__index=""
	#random_name随机名称
	__name=""
	#数组保存数据长度
	__length=0
	#暂时用来保存数据以便单机测试
	#__temp_list=[]
	#初始化
	def __init__(self,address,min_key=0,max_key=0):
		self.__address=address
		self.__max=max_key
		self.__min=min_key
		self.__length=0
		self.__name=jt_common.getRandomName()
		res=jt_common.post(self.__address,self.__name,{"cmd":"mkdirnext"})
		if res:
			if res['code']==0:
				self.__index=res['data']
		else:
			jt_log.log.write(GLOBAL.error_log_path,"初始化dirnext失败，网络获取失败")
		#self.__temp_list=jt_list.xlist()

	#在当前块中查找是否有相应的文件名
	def is_find(self,name):
		pass

	#显示当前块中的目录内容
	def ls(self):
		try:
			res=jt_common.get(self.__address,"",{"cmd":"ls","index":self.__index})
			if res['code']==0:
				return res['data']
			else:
				return res['msg']
		except Exception,e:
			traceback.print_exc()
			jt_log.log.write(GLOBAL.error_log_path,e.message)

	#插入记录到块中
	def insert(self,name,data):
		try:
			if self.__length==0:
				self.__min=data.getKey()
				self.__max=data.getKey()

			if data.getKey()<self.__min:
				self.__min=data.getKey()

			if data.getKey()>self.__max:
				self.__max=data.getKey()

			#远程机创建目录只需要传递目录的名称即可
			if jt_common.post(self.__address,name,{"cmd":"mkdir","index":self.__index,"dirnode":data}):
				self.__length=self.__length+1	
			#return self.__temp_list.insert(name,data)
		except Exception,e:
			traceback.print_exc()
			jt_log.log_write(GLOBAL.error_log_path,e.message())
	
	#重写get函数
	def __getitem__(self,index):
		res=jt_common.post(self.__address,"",{"cmd":"getByIndex","index":self.__index,"sub_index":index})	
		return res

	#根据主键获取内容
	def getByKey(self,key):
		res=jt_common.post(self.__address,"",{"cmd":"getByKey","index":self.__index,"key":key})
		return res

	#获取地址
	def getAddress(self):
		return self.__address

	#获取最大的名称
	def getMaxName(self):
		res=jt_common.post(self.__address,"",{"cmd":"getMaxName","index":self.__index})
		return res

	#根据名字删除结点
	def deleteByName(self,name):
		res=jt_common.post(self.__address,"",{"cmd":"deleteByName","index":self.__index,"name":name})
		return res
	
	#根据下标删除结点
	def deleteByIndex(self,index):
		res=jt_common.post(self.__address,"",{"cmd":"deleteByIndex","index":self.__index,"sub_index":index})
		return res

	#获取最大键值
	def getMaxKey(self):
		res=jt_common.post(self.__address,"",{"cmd":"getMaxKey","index":self.__index})
		return res

	#获取最小键值
	def getMinKey(self):
		res=jt_common.post(self.__address,"",{"cmd":"getMinKey","index":self.__index})
		return res

	#获取当前存储内容的长度
	def getLength(self):
		res=jt_common.post(self.__address,"",{"cmd":"getLength","index":self.__index})
		return res
	
	#根据key将数据拆分成两个块
	def split(self,new_dirnext):
		res=jt_common.post(self.__address,"",{"cmd":"split","mac":new_dirnext.__address,"target_index":new_dirnext.__index})
		if res['code']==0:	
			return res['data']
		else:
			return False

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
