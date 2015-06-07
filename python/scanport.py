#!/usr/bin/env python
import socket
def scan_port():
	err_count=0
	for port in range(65525):
		try:
			print "%s -> %s" %(port,socket.getservbyport(port,'tcp'))
			print "%s -> %s" %(port,socket.getservbyport(port,'udp'))
		except socket.error,err_msg:
			err_count=err_count+1
	print "%s not founds" %(err_count)
	print "%s founds" %(65525-err_count)	
			
if __name__=='__main__':
	scan_port()

