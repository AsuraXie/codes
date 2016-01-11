#!/usr/bin/env python
import argparse
import sys
import dirnode
import jt_log
import jt_global
import jt_common
import main
import dircopy
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

DEFAULT_HOST="127.0.0.1"
DEFAULT_PORT=8800
ROOT="root"

class RequestHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		try:
			self.store_request()
			params=self.getCommand()
			resp=main.process(ROOT,params)
			self.send_response(200)
			self.send_header('Content-type','text/html')
			self.send_header("Server","JT xlx")
			self.end_headers()
			self.wfile.write(resp)
		except Exception,e:
			self.store_request()
			self.send_response(500)
			self.send_header("Content-type","text/html")
			self.send_header("Server","JT xlx")
			self.end_headers()
			self.wfile.write(e)	
		return

	def do_POST(self):
		pass
		return

	def store_request(self):
		logs=self.client_address[0]+str(self.client_address[1])+"  "+self.command+"  "+self.path
		jt_log.log.write(jt_global.visited_log_path,logs)

	def getCommand(self):
		if self.command=="GET":
			params=jt_common.cmds(self.path)
			return params
		else:
			print "post"
	
class CustomHTTPServer(HTTPServer):
	def __init__(self,host,port):
		server_address=(host,port)
		global ROOT
		ROOT=dirnode.dirnode("/")
		dircopy.copydir(ROOT,"/home/asura/codes/python")
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
	run_server(port)
