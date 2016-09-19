#!/usr/bin/env python
#-*- coding: utf-8 -*-

import socket
import sys
import threading
import thread
import jt_http

class jt_server():
	def run(self,port):
		try:
			mysocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			mysocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
			mysocket.bind(("",int(port)))
			mysocket.listen(10)
			print "jt_server is listen to ",port

			while 1:
				conn,addr=mysocket.accept()
				th1=threading.Thread(target=jt_server.handlerData,args=(self,conn))
				th1.start()
				th1.join()

			mysocket.close()
		except Exception,msg:
			print msg
			mysocket.close()
			sys.exit()

	def handlerData(self,conn):
		data=conn.recv(1024)
		my_http_analyse=jt_http.jt_http()
		res=my_http_analyse.analyse(data)
		conn.sendall(res)
		conn.close()
