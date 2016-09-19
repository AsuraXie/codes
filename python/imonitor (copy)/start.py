#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys,getopt;
import server.jt_server as jt_server;

if __name__=="__main__":
    '''默认port'''
    port=80;
    try:
        opts,argv=getopt.getopt(sys.argv[1:],"hp:",["help","port="]);
        for key,value in opts:
            if key=="-p":
                port=value;
        my_server=jt_server.jt_server();
        my_server.run(port);
    except getopt.GetoptError:
        print "输入参数错误";
