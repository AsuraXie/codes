#!/usr/bin/env python

import socket
send_buf_size=4096
recv_buf_size=4096

def modify_buff_size():
	sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	bufsize=sock.getsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF)
	print "Buffer size [Before]:%d" %bufsize
	sock.setsockopt(socket.SOL_TCP,socket.TCP_NODELAY,1)
	sock.setsockopt(socket.SOL_SOCKET,
			socket.SO_SNDBUF,
			send_buf_size)
	sock.setsockopt(socket.SOL_SOCKET,
			socket.SO_RCVBUF,
			recv_buf_size)
	bufsize=sock.getsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF)
	print "Buffer size [After]:%d" %bufsize
	
if __name__=='__main__':
	modify_buff_size()
