import urllib2
import re
import mysql.connector

def check_exist(url):
	conn=mysql.connector.connect(usr='root',password='',databases='webdb',use_unicode=True)
	tempcur=conn.cursor()
	urls=url.split(';')
	for temp in urls:
		tempcur.execute('select * from usedurl where usedurl =')
		result=tempcur.fetchall()
			
		
conn=mysql.connector.connect(user='root',password='',databases='webdb',use_unicode=True)
cursor=conn.cursor()
cursor.execute('select * from unusedurl limit 100')
unusedurl=cursor.fetchall()

response=urllib2.urlopen("http://www.baidu.com/")
html=response.read();
m=re.findall(r"href='[^']*'",html)

