#!/usr/bin/env python
from mydb import *
import download_urls
if root_url=="":
	root_url=raw_input("enter the root_url:")
else:
	print "the root_url = ",root_url
download_urls.download_url(root_url)
