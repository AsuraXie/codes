#!/usr/bin/env python
# -*- coding:utf8 -*-

import socket
import base64
import time

def mail():
	try:
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		print s.connect(("smtp.163.com",25))
		print s.send("helo smtp.163.com")
		print "msg:",s.recv(1024)

		print s.send("auth login")
		print "msg:",s.recv(1024)

		print s.send(base64.b64encode("xielixiang111@163.com"))
		print "msg:",s.recv(1024)

		print s.send(base64.b64encode("xielixiang321"))
		print s.recv(1024)

		print s.send("mail from:<xielixiang111@163.com")
		print s.recv(1024)

		print s.send("rcpt to:<lixiang23@staff.sina.com.cn>")
		print s.recv(1024)

		print s.send("data")
		print s.recv(1024)

		print s.send("from:<xielixiang111@163.com>\n\r"
				+"to:<lixiang23@staff.sina.com.cn>\n\r"
				+"subject:test\n\r"
				+"hello world mta"
				+"\n\r.\n\r")
		print s.recv(1024)

		print s.send("quit")
		print s.recv(1024)
		s.close()
	except Exception,e:
		s.close()
		print e
		if s!=None:
			s.close()

if __name__=="__main__":
	mail()
