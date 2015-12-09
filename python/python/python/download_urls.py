#!/usr/bin/env python
import sys
import mysql.connector
from mydb import *
import orm
import urllib2
import re
import time
import hashlib
import threading
import socket

def download_url(url=""):
	if url=="":
		url=root_url
	print "download page from " + url
	resp=urllib2.urlopen(url)
	html=resp.read()
	analyze_html(html,url)
	a=threading.Thread(target=print_global_infos,name="print_global_infos")
	a.start()
	b=threading.Thread(target=download_urls,name="download_urls")
	b.start()
	c=threading.Thread(target=download_img,name="download_img")
	c.start()

def print_global_infos():
	global all_next_urls
	global all_img_urls
	print "all_next_urls:"+str(len(all_next_urls))
	print "all_img_urls:"+str(len(all_img_urls))	
	time.sleep(10)
	print_global_infos()
	
def download_urls():
	global all_next_urls
	global used_next_urls
	socket.setdefaulttimeout(10.0)
	while True:
		if len(all_next_urls)==0:
			time.sleep(1)
			print "empty next urls"
			continue
		temp_url=all_next_urls.pop()
		if temp_url in used_next_urls:
			continue
	#	if temp_url.find("baoxxx.com")<0:
	#		continue
		used_next_urls.append(temp_url)
		print "download:"+temp_url
		try:
			resp=urllib2.urlopen(temp_url)
			html=resp.read()
			analyze_html(html,temp_url)
		except Exception,e:
			print e

def store_url(urls=[]):
	for i in urls:
		orm.update("insert into urls(urls,source) values('"+i[0]+"','"+i[1]+"')")

def get_url():
	return orm.query("select * from urls")

def download_img():
	md5=hashlib.md5()
	global all_img_urls
	img_postfix=[]
	global img
	img_postfix=img.split('|')
	print img_postfix
	while True:
		if len(all_img_urls)==0:
			time.sleep(5)
			print "empty list of img_urls"
			continue

		temp_url=all_img_urls.pop()
		if temp_url in used_img_urls:
			continue
		used_img_urls.append(temp_url)
		if type(temp_url)==None:
			time.sleep(1)
			continue
		print temp_url
		try:
			resp=urllib2.urlopen(temp_url)
			img=resp.read()
			md5.update(temp_url)
			file_path=md5.hexdigest()
			temp_postfix="unknow_img"
			for i in img_postfix:
				if temp_url.find(i)>=0:
					temp_postfix=i
			f=open('/home/asura/python/python/img/'+file_path+'.'+temp_postfix,'wb')
			f.write(img)
			f.close()
		except Exception,e:
			print e

def analyze_html(html,url):
	all_urls=href_pattern.findall(html)+src_pattern.findall(html)
	path_urls=[]
	img_urls=[]
	img_postfix=img.split('|')
	temp=""
	count=len(url.split('/'))
	j=0
	for i in url.split('/'):
		if j == count -1:
			break
		temp=temp+i
		temp=temp+"/"
		j=j+1
	url=temp

	for i in all_urls:
		if i.find('href')>=0:
			tempa=i[6:-1].split('.')[-1]
			if tempa in img_postfix:
				if i[6:-1].find("http")>=0:	
					img_urls.append(i[6:-1])
				else:
					img_urls.append(url+i[6:-1])
			else:
				if i[6:-1].find("http")>=0:
					path_urls.append(i[6:-1])
				else:
					path_urls.append(url+i[6:-1])
			continue

		if i.find('src')>=0:
			tempb=i[5:-1].split('.')[-1]
			if tempb in img_postfix:
				if i[5:-1].find("http")>=0:
					img_urls.append(i[5:-1])
				else:
					img_urls.append(url+i[5:-1])
			else:
				if i[5:-1].find("http")>=0:
					path_urls.append(i[5:-1])
				else:
					path_urls.append(url+i[5:-1])
			continue

	global all_next_urls
	global all_img_urls
	
		
	if len(all_next_urls)>0 and len(all_next_urls)<10000:
		all_next_urls=all_next_urls+path_urls
	else:
		all_next_urls=path_urls

	if len(all_img_urls)>0 and len(all_img_urls)<10000:
		all_img_urls=all_img_urls+img_urls
	else:
		all_img_urls=img_urls
	all_next_urls=list(set(all_next_urls))
	all_img_urls=list(set(all_img_urls))
	return [img_urls,path_urls]
