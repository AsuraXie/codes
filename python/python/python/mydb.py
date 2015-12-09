#!/usr/bin/env python
import re
global db_url
global db_name
global db_passwd
global db_user
global root_url
global all_next_urls
global all_img_urls
global used_next_urls
global used_img_urls

db_url="192.168.0.112"
db_name="webimgs"
db_passwd="123456"
db_user="asura"
root_url=""
img="bmp|dib|fle|emf|gif|jpg|jpeg|jif|pcx|dcx|pic|png|tga|tif|triff|xif|wmf|jfif"
src="css|js"
common_pattern=re.compile(r'https?:[^,;\'") ]*')
url_pattern=re.compile(r'https?:[^,;\'") ]*('+src+'){1}[^,;\'") ]*')
img_pattern=re.compile(r'https?:[^,;\'") ]*('+img+'){1}[^,;\'") ]*')
src_pattern=re.compile(r'src=[\'"][^,;\'") ]*[\'"]')
href_pattern=re.compile(r'href=[\'"][^,;\'") ]*[\'"]')
all_next_urls=[]
all_img_urls=[]
used_next_urls=[]
used_img_urls=[]
