#!/usr/bin/env python
import os
import socket
import threading
import SocketServer

server_host='localhost'
server_port=0
buf_size=1024
echo_msg="hello python world"

class ForkingClient():
	def __init__(self,ip,port):
		self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.sock.connect((ip,port))

	def run(self):
		current_process_id=os.getpid()
		print "PID %s Sending echo message to the server:%s" %(current_process_id,echo_msg)
		sent_data_length=self.sock.send(echo_msg)
		print "Sent:%d characters,so far..." %sent_data_length
		response=self.sock.recv(buf_size)
		print "PID %s received:%s" %(current_process_id,response[5:])
	
	def shutdown(self):
		self.sock.close()

class ForkingServerRequestHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		data=self.request.recv(buf_size)
		current_process_id=os.getpid()
		response="%s:%s" %(current_process_id,data)
		print "Server sending response [current_process_id:data]=[%s]" %response
		self.request.send(response)
		return

class ForkingServer(SocketServer.ForkingMixIn,SocketServer.TCPServer):
	pass

def main():
	server=ForkingServer((server_host,server_port),ForkingServerRequestHandler)
	ip,port=server.server_address
	server_thread=threading.Thread(target=server.serve_forever)
	server_thread.setDaemon(True)
	server_thread.start()
	print 'Server loop running PID:%s' % os.getpid()
	client1=ForkingClient(ip,port)
	client1.run()

	client2=ForkingClient(ip,port)
	client2.run()

	server.shutdown()
	client1.shutdown()
	client2.shutdown()
	server.socket.close()

if __name__=='__main__':
	main()
