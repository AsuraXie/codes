#!/usr/bin/env python
#-*- coding:utf-8 -*-

import mime
import jt_file
import sys
sys.path.append("./project/frame")
import jt_mvc
import jt_log
import time,datetime

class jt_http():

	def __init__(self):
		self.__method=""
		self.__http_type=""
		self.__post={}
		self.__get={}
		self.__url=""
		self.__full_url=""
		self.__file=""
		self.__header={}
		self.__content=""
		self.__suffix=""
		self.__resp_type=""

	def getParam(self):
		return {"method":self.__method,"http_type":self.__http_type,"post":self.__post,"get":self.__get,
				"url":self.__url,"file":self.__file,"header":self.__header,"content":self.__content,
				"full_url":self.__full_url,"suffix":self.__suffix}

	def analyse(self,data):
		request=data.split("\r\n");
		
		request_method=request[0].split(" ");
		if(request_method[0] in ['POST','GET','PUT','DELETE'] and len(request_method)==3):
			self.__method=request_method[0]
			self.__url=request_method[1]
			self.__http_type=request_method[2]
		else:
			return {"code":-1,"msg":"get method error"}

		my_log=jt_log.jt_log()
		my_log.write(self.__method+" "+self.__url+" "+self.__http_type+" "+time.strftime("%Y-%m-%d %H:%M:%S"))
		for i in range(1,len(request)):
			if(request[i]==""):
				self.__content=request[i+1]
				break;
			header_column=request[i].split(":")
			self.__header[header_column[0]]=header_column[1]

		self.doGet()

		self.doPost()

		return self.process()

	def response(self,data):
		header=("HTTP/1.1 200 OK",
			"Content-Length: 3059",
			"Content-Type: text/html",
			"Cache-control: private",
			"Connection: keep-alive",
			"Server:JT-Asura")
		res='\r\n'.join(header)
		res=res+"\r\n\r\n"+data
		return res
	
	def doGet(self):
		if self.__method=="GET":
		    url_array=self.__url.split("?")
		    if len(url_array)==2:
		        url=url_array[0]
		        params=url_array[1]
		    else:
		        url=url_array[0]
		        params=""

		    self.__url=url

		    suffix_array=self.__url.split(".")
		    if(len(suffix_array)==2):
		        self.__suffix=suffix_array[1]

		    url_array=params.split("&")
		    if len(url_array)>0:
		        for i in range(0,len(url_array)):
		            url_str=url_array[i].split("=")
		            if len(url_str)==2:
		                self.__get[url_str[0]]=url_str[1]

	def doPost(self):
		if self.__method=="POST":
		    post_array=self.__content.split("&")
		    for i in range(0,len(post_array)):
		        post_str=post_array[i].split("&")
		        if(len(post_str)==2):
		            self.__post[post_str[0]]=post_str[1]

	def doFile(self):
		pass

	def process(self):
		jt_mime=mime.jt_mime()
		if jt_mime.checkExists(self.__suffix):
		    file_loader=jt_file.jt_file()
		    resp_file=file_loader.load(self.__url)
		    return self.response(resp_file)
		else:
		    application=jt_mvc.jt_mvc(self.getParam())
		    resp_html=application.run()
		    return self.response(resp_html)

