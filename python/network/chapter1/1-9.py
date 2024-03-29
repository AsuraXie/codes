#!/usr/bin/env python

import socket
import sys

def reuse_socket_addr():
	sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	old_state=sock.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)
	print "Old sock state:%s" %old_state
	sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	new_state=sock.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)
	print "New sock state:%s" %new_state
	local_port=8282
	src=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	src.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	src.bind(('127.0.0.1',local_port))
	src.listen(1)
	print ("Listening on port :%s" %local_port)
	while True:
		try:
			connection,addr=src.accept()
			print "Connected by %s:%s" %(addr[0],addr[1])
		except KeyboardInterrupt:
			break
		except socket.error,msg:
			print '%s' %(msg,)

if __name__=='__main__':
	reuse_socket_addr()
	
