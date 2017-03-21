#!/usr/bin/env python
# -*- coding:utf8 -*-

import socket
import base64
import time
import os

def sendHello(s):
    print "helo smtp.163.com"
    s.send("helo smtp.163.com\n")

def authLogin(s):
    print "auth login"
    s.send("auth login\n")

def sendUserAuth(s):
    print "send auth"
    #邮箱帐号
    s.send(base64.b64encode("xielixiang111@163.com"))
    #邮箱密码
    s.send(base64.b64encode("xielixiang321"))

def sendData(s):
    print "send data"
    s.send("mail from:<xielixiang111@163.com>\n")
    s.send("rcpt to:<lixiang23@staff.sina.com.cn>\n")
    s.send("data\n")

def sendBody(s):
    print "send body"
    s.send("from:<xielixiang111@163.com>\n")
    s.send("to:<lixiang23@staff.sina.com.cn>\n")
    s.send("subject:信达数据库备份\n")
    s.send("some thing wrong\n")
    s.send(".\n")

def mail():
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print s.connect(("smtp.163.com",25))
        while(1):
            print "wait data"
            recv_data = s.recv(4096)
            if(len(recv_data)>0):
                print "msg:"+recv_data
                if("220 163.com" in recv_data):
                    print "point a"
                    sendHello(s)
                elif("250 OK" in recv_data):
                    print "point b"
                    authLogin(s)
                elif("334" in recv_data):
                    print "point c"
                    sendUserAuth(s)
                elif("235 Authentication successfu" in recv_data):
                    print "point d"
                    sendData(s)
                elif("354 End data with" in recv_data):
                    print "point e"
                    sendBody(s)
                elif("250 Mail OK queued" in recv_data):
                    s.send("quit\n")
                    break
                elif("554 DT:SPM" in recv_data):
                    print "send fail"
                    break
                else:
                    print "nothing"
        s.close()

    except Exception,e:
        s.close()
        print e
        if s!=None:
            s.close()

if __name__=="__main__":
    mail()
