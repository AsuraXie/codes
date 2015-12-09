#!/usr/bin/env python
import select
import socket
import sys
import signal
import cPickle
import struct
import argparse

server_host="localhost"
chat_server_name="server"

def send(channel,*args):
	buffer=cPickle.dumps(args)
	value=socket.htonl(len(buffer))
	size=struct.pack("L",value)
	channel.send(size)
	channel.send(buffer)

def receive(channel):
	size=struct.calcsize("L")
	size=channel.recv(size)
	try:
		size=socket.ntohl(struct.unpack("L",size)[0])
	except struct.error,e:
		return ''

	buf=""
	while len(buf) < size:
		buf=channel.recv(size-len(buf))
	return cPickle.loads(buf)[0]

class ChatServer(object):
	def __init__(self,port,backlog=5):
		self.clients=0
		self.clientmap={}
		self.outputs=[]
		self.server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		self.server.bind((server_host,port))
		print 'Server listening to port:%s....' %port
		self.server.listen(backlog)
		signal.signal(signal.SIGINT,self.sighandler)
		
	def sighandler(self,signum,frame):
		print 'Shutting down server...'
		for output in self.outputs:
			output.close()
		self.seerver.close()

	def get_client_name(self,client):
		info=self.clientmap[client]
		host,name=info[0][0],info[1]
		return '@'.join((name,host))

	def run(self):
		inputs=[self.server,sys.stdin]
		self.outputs=[]
		running=True
		while running:
			try:
				readable,writable,exceptional=select.select(inputs,self.outputs,[])
			except select.error,e:
				break
		for sock in readable:
			if sock==self.server
