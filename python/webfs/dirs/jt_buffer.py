#!/usr/bin/env python
import jt_global as GLOBAL
import encrypt
import time
try:
	import cPickle as pickle
except ImportError:
	import pickle

def bufferpop():
	if len(GLOBAL.JTBuffer)>=1000:
		keys=GLOBAL.JTBuffer.keys()
		for i in range(0,10):
			GLOBAL.JTBuffer.pop(keys[i])

def StoreBufferGet(urls,data,age=5):
	bufferpop()
	key=encrypt.jiami(urls)
	s_data={}
	s_data['start']=time.time()
	s_data['data']=data
	s_data['age']=int(age)
	GLOBAL.JTBuffer[key]=s_data

def StoreBufferPost(urls,params,data,age=5):
	bufferpop()
	key=encrypt.jiami(urls+str(pickle.dumps(params)))
	s_data={}
	s_data['start']=time.time()
	s_data['data']=data
	s_data['age']=int(age)
	GLOBAL.JTBuffer[key]=s_data

def bufferGet(urls):
	key=encrypt.jiami(urls)
	if key in GLOBAL.JTBuffer:
		res=GLOBAL.JTBuffer[key]
		if (time.time()-res['start'])>res['age']:
			GLOBAL.JTBuffer.pop(key)
			return False	
		else:
			return res['data']
	else:
		return False

def bufferPost(urls,params):
	key=encrypt.jiami(urls+str(pickle.dumps(params)))
	if key in GLOBAL.JTBuffer:
		res=GLOBAL.JTBuffer[key]
		if (time.time()-res['start'])>res['age']:
			GLOBAL.JTBuffer.pop(key)
			return False
		else:
			return res['data']
	else:
		return False

def getMaxAge(params):
	if 'cmd' in params:
		if params['cmd']=="cd":
			return 50
	return 0

if __name__=="__main__":
	GLOBAL.JTBuffer={}
	StoreBufferGet("1234","erwere",2)
	StoreBufferPost("123456",['a'],['i3','r3',3423],3)
	print bufferGet("1234")
	print bufferPost("123456",['a'])
	print bufferGet("1234")
	print bufferPost("123456",['a'])
	print bufferGet("1234")
	print bufferPost("123456",['a'])
	time.sleep(5)
	print bufferGet("1234")
	print bufferPost("123456",['a'])
	print bufferGet("1234")
	print bufferPost("123456",['a'])
