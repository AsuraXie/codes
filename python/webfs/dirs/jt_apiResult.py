#!/usr/bin/env python
# --*-- coding:utf-8 --*--

import jt_respcode as RespCode
try:
	import cPickle as pickle
except ImportError:
	import pickle

class ApiResult(object):
	__code=""
	__msg=""
	__data=""
	
	def __init__(self):
		self.__code=RespCode.RespCode['RESULT_NOT_INIT']['code']
		self.__msg=RespCode.RespCode['RESULT_NOT_INIT']['msg']
		self.__data=""

	def setSuccess(self,data=""):
		self.__code=RespCode.RespCode['SUCCESS']['code']
		self.__msg=RespCode.RespCode['SUCCESS']['msg']
		self.__data=data

	def setError(self,RespCode,data=""):
		self.__code=RespCode['code']
		self.__msg=RespCode['msg']
		self.__data=data

	def display(self):
		'''
		res=""
		res=res+"{\"code\":\""+str(self.__code)+"\""
		res=res+",\"msg\":\""+str(self.__msg)+"\""
		if isinstance(self.__data,str) or isinstance(self.__data,int) or isinstance(self.__data,bool):
			res=res+",\"data\":\""+str(self.__data)+"\""
		else:
			res=res+",\"data\":"+pickle.dumps(self.__data)
		res=res+"}"
		'''
		res={}
		res['code']=self.__code
		res['msg']=self.__msg
		res['data']=self.__data
		return res
