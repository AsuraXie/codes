#!/usr/bin/env python
import os
import socket
import threading
import SocketServer

server_host="localhost"
server_port=0
buf_size=1024

def client(ip,port,message):
	sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.connect((ip,port))
	try:
		sock.sendall(message)
		response=sock.recv(buf_size)
		print "Client received:%s" %response
	finally:
		sock.close()

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		data=self.request.recv(1024)
		current_thread=threading.current_thread()
		response="%s:%s" %(current_thread.name,data)
		self.request.sendall(response)
	
class ThreadedTCPServer(SocketServer.ThreadingMixIn,SocketServer.TCPServer):
	pass

if __name__=="__main__":
	server=ThreadedTCPServer((server_host,server_port),ThreadedTCPRequestHandler)
	ip,port=server.server_address
	server_thread=threading.Thread(target=server.serve_forever)
	server_thread.daemon=True
	server_thread.start()
	print "Server loop running on thread:%s" %server_thread.name
	
	client(ip,port,"Hello from client1")
	client(ip,port,"Hello from client2")
	client(ip,port,"Hello from client3")
	server.shutdown()

