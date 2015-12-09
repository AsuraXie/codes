#!/usr/bin/env python
import socket
def find_service_name():
	for port in range(65535):
		try:
			print "Port : %s=>Service name : %s" %(port,socket.getservbyport(port,'tcp'))
			print "Port : %s=>Service name : %s" %(port,socket.getservbyport(port,'udp'))
		except :
			a=1
if __name__=='__main__':
	find_service_name()
