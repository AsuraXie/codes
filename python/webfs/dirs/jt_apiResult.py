#!/usr/bin/env python
# --*-- coding:utf-8 --*--

import jt_respcode as RespCode

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
		res={}
		res['code']=self.__code
		res['msg']=self.__msg
		res['data']=self.__data
		return res
		
