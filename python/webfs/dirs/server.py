#!/usr/bin/env python
# --*-- coding:utf-8 --*--
import argparse
import sys
import dirnode
import jt_log
import jt_list
import jt_global as GLOBAL
import jt_common
import main
import dircopy
import time
import jt_machine_list
import threading
import socket
import urllib
from json import *
from SocketServer import ThreadingMixIn
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
try:
	import cPickle as pickle
except ImportError:
	import pickle

DEFAULT_HOST=GLOBAL.local_addr
DEFAULT_PORT=GLOBAL.local_port

class RequestHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.storeRequest()
		params=self.getCommand()
		paths=self.splitPath()
		print params
		if paths[0]=='web' or 'favicon.ico' in self.path:
			if 'favicon.ico' in self.path:
				name="favicon.ico"
			elif len(paths)>=2:
				name=paths[1]
			else:
				name="index.html"
			resp=self.getFile(name)
		else:
			process_start=time.time()	
			resp=main.process(params)
			process_end=time.time()
			if 'cmd' in params:
				self.storeDealTime(process_start,process_end,params['cmd'])
			else:
				self.storeDealTime(process_start,process_end,"get")
			print resp
			resp=JSONEncoder().encode(resp)
		self.send_response(200)
		self.send_header('content-type','text/html,charset=utf-8')
		self.send_header("Server","JT xlx")
		self.send_header("Access-Control-Allow-Origin","*")
		self.end_headers()
		self.wfile.write(resp)
		return 

	def do_POST(self):
		self.storeRequest()
		#print self.rfile.read(int(self.headers['content-length']))
		params=self.getCommand()
		print params
		process_start=time.time()
		resp=main.process(params)
		process_end=time.time()
		if 'cmd' in params:
			self.storeDealTime(process_start,process_end,params['cmd'])
		else:
			self.storeDealTime(process_start,process_end,"get")
		self.send_response(200)
		self.send_header("content-type","text/html")
		self.send_header("Server","JT xlx")
		self.end_headers()
		self.wfile.write(pickle.dumps(resp))
		return 

	def storeRequest(self):
		logs=self.client_address[0]+str(self.client_address[1])+"  "+self.command+"  "+self.path
		jt_log.log.write(GLOBAL.visited_log_path,logs)
		return
	
	def getFile(self,name="index.html"):
		file_object=open("web/"+name)
		try:
			all_the_text=file_object.read()
		except Exception,e:
			all_the_text=e.message
		finally:
			file_object.close()
		return all_the_text
			
	def splitPath(self):
		res=[]
		paths=self.path.split("/")
		for item in paths:
			if item!="":
				res.append(item)
		return res

	def storeDealTime(self,start,end,cmd):
		spend=round((float(end)-float(start))*1000,3)
		jt_log.log.write(GLOBAL.spend_time_log_path,str(spend)+"---"+cmd)
		return

	def getCommand(self):
		if self.command=="GET":
			params=jt_common.cmds(urllib.unquote(self.path))
			return params
		else:
			params=jt_common.cmds(self.path)
			post_params_str=self.rfile.read(int(self.headers['content-length']))
			post_params=pickle.loads(post_params_str)
			for key in params:
				post_params[key]=params[key]
			return post_params
	
class CustomHTTPServer(ThreadingMixIn,HTTPServer):
	def __init__(self,host,port):
		server_address=(host,port)
		#global ROOT
		#global MacList
		#global LocalData
		#本地存储有序链表结构
		GLOBAL.LocalData=jt_list.xlist()
		#初始化目录结构
		#ROOT=dirnode.dirnode("root","")
		#GLOBAL.LocalData.insert("/",ROOT)
		#初始化机器列表
		GLOBAL.MacList=jt_machine_list.mList()
		GLOBAL.MacList.show()
		#dircopy.copydir(ROOT,"/home/asura/codes/python")
		HTTPServer.__init__(self,server_address,RequestHandler)
	
def run_server(port):
	try:
		server=CustomHTTPServer(DEFAULT_HOST,port)
		print "JT Distribute FileSystem started on port:%s" % port
		server.serve_forever()
	except Exception,err:
		print "Error:%s" % err
	except KeyboardInterrupt:
		print "Server interrupted and is shutting down..."
		server.socket.close()

if __name__=="__main__":
	parser=argparse.ArgumentParser(description="JT distribute file system")
	parser.add_argument("--port",action="store",dest="port",type=int,default=DEFAULT_PORT)
	given_args=parser.parse_args()
	port=given_args.port
	'''
	GLOBAL.LocalData=jt_list.xlist()
	ROOT=dirnode.dirnode("root","")
	GLOBAL.MacList=jt_machine_list.mList()
	'''
	GLOBAL.local_addr=socket.gethostbyname("localhost")
	GLOBAL.local_port=port
	print GLOBAL.local_addr
	print GLOBAL.local_port
	run_server(port)
