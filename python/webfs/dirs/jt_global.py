#!/usr/bin/env python
# --*-- coding:utf-8 --*--

#childs的长度
dir_size=1

#dirnexts的长度
dir_next_size=10

#备份数
back_up_num=3

type_file=1
type_dir=2
ROOT="root"

#本地机器列表
MacList="machine list"

#本地存储列表
LocalData="local data"

isotimeformate_brief="%Y%m%d%H%M%S"
isotimeformate="%Y-%m-%d %H:%M:%S"

#错误日志位置
error_log_path="log/data/error.log"

#访问日志位置
visited_log_path="log/http/visited.log"

#访问花费时间日志位置
spend_time_log_path="log/data/spendtime.log"

#本机的ip地址
local_addr="127.0.0.1"
#本机的端口地址
local_port="8800"
#本机的主机名称
local_host="localhost"

#根目录所处位置
root_mac=""

#超时时间
time_out=2

#远程机器有哪些
remote_mac=[{"addr":"127.0.0.1","port":"8803"},
	{"addr":"127.0.0.1","port":"8802"},
	{"addr":"127.0.0.1","port":"8804"},
	{"addr":"127.0.0.1","port":"8805"},
	{"addr":"127.0.0.1","port":"8806"},]
