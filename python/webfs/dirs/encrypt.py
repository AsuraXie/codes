#!/usr/bin/env python
# --*-- coding:utf-8 --*--

#加密函数，将字符串转化为key

import hashlib

def jiami(strs):
	m=hashlib.md5()
	m.update(str(strs))
	return m.hexdigest()
