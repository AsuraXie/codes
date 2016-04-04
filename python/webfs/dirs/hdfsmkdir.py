#!/usr/bin/env python
# --*-- coding:utf-8 --*--
import commands
import time
import jt_log
import os

def hdfsmkdir(parent,level):
	if level>=3:
		return
	for i in range(0,200):
		path=parent+os.sep+str(i)
		print path
		cmds="hadoop fs -mkdir "+str(path)
		start=time.time()
		commands.getstatusoutput(cmds)
		end=time.time()
		jt_log.log.write("log/hdfs/mkdir",str(end-start))
		cmds="hadoop fs -test -d "+str(path)
		start=time.time()
		commands.getstatusoutput(cmds)
		end=time.time()
		jt_log.log.write("log/hdfs/test",str(end-start))
		hdfsmkdir(path,level+1)


if __name__=="__main__":
	hdfsmkdir("root",1)
