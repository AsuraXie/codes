import urllib2
import re
import mysql.connector
import time


unusedurl=[]
g_mysql="usr='root',password='',databases='webdb',use_unicode=True"

def check_exist(urls):
	conn=mysql.connector.connect(g_mysql)
	tempcur=conn.cursor()
	for temp in urls:
		tempcur.execute('select * from usedurl where usedurl ='+temp)
		result=tempcur.fetchall()
		if result:
			continue
		else:
			unusedurl.append(temp)
	tempcur.close()
	conn.close()

def get_unusedurl():
	conn=mysql.connector.connect(g_mysql)
	tempcur=conn.cursor()
	tempcur.execute('select * from unusedurl')
	unusedurl=tempcur.fetchall()
	tempcur.close()
	conn.close()

def store_usedurl(url1,url2):
	conn=mysql.connector.connect(g_mysql)
	tempcur=conn.cursor()
	for tt in url1:
		tempcur.execute("insert into use
	tempcur.close()
	conn.close()

def store_unusedurl(url1,url2):
	conn=mysql.connector.connect(g_mysql)
	tempcur=conn.cursor()
	for tt in url1:
		tempcur.execute("insert into unusedurl('usedurl','shijian','laiyuan') values('"+tt+","+time.time()+","+url2+"')")
	tempcur.close()
	conn.close()

print "1 start from a rooturl"
print "2 start from mysqldb"	
print "chose the mode"
type=raw_input()
if type=="1":
	print "enter the root url"
	rooturl=raw_input()	
	unusedurl.append(rooturl)
else:
	get_unusedurl()

while 1:
	if len(unusedurl)==0:
		get_unusedurl()
	tempurl=unusedurl.pop()
	print "get url "+tempurl
	response=urllib2.urlopen(tempurl)
	print "get html"
	html=response.read();
	print "analyse html"
	m=re.findall(r"href='[^']*'",html)
	check_exist(m)
	print "check urls"
	print "current url :"+tempurl		

