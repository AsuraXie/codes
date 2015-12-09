#!/usr/bin/env python
import mysql.connector
from mydb import *

def query(command):
	conn=mysql.connector.connect(user=db_user,host=db_url,password=db_passwd,database=db_name,use_unicode=True)
	cursor=conn.cursor()
	cursor.execute(command)
	values=cursor.fetchall()
	cursor.close()
	conn.close()
	return values

def update(command):
	conn=mysql.connector.connect(user=db_user,host=db_url,password=db_passwd,database=db_name,use_unicode=True)
	cursor=conn.cursor()
	cursor.execute(command)
	values=cursor.rowcount
	if values>=0:
		conn.commit()
	cursor.close()
	conn.close()
	if values==0:
		return False
	else:
		return True

