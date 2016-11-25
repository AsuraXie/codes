#!/usr/bin/env python
# -*- coding: utf8 -*-

import smtplib 
import sys
from email.mime.text import MIMEText
from email.utils import formataddr
my_sender='xielixiang111@163.com'
my_user='lixiang23@staff.sina.com.cn'

def mail(content):
	ret=True
	try:
		msg=MIMEText(content,'plain','utf-8')
		msg['From']=formataddr(["asura",my_sender])
		msg['To']=formataddr(["pp",my_user])
		msg['Subject']="refresh error"
		server=smtplib.SMTP("smtp.163.com",25)
		server.login(my_sender,"xielixiang321")
		server.sendmail(my_sender,[my_user,],msg.as_string())
		server.quit()
	except Exception,e:
		print e
		ret=False
	return ret

if __name__=="__main__":
	if len(sys.argv)==1:
		print "send msg none fail"
		exit()

	content=sys.argv[1]
	if content=="":
		print "send msg is empty fail"
	else:
		ret=mail(content)
		if ret:
			print("ok")
		else:
			print("filed")
