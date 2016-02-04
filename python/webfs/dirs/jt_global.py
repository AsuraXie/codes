#!/usr/bin/env python

dir_size=1
dir_next_size=3
type_file=1
type_dir=2
ROOT="root"
MacList="machine list"
LocalData="local data"
isotimeformate_brief="%Y%m%d%H%M%S"
isotimeformate="%Y-%m-%d %H:%M:%S"
error_log_path="log/data/error.log"
visited_log_path="log/http/visited.log"
spend_time_log_path="log/data/spendtime.log"
local_addr="127.0.0.1"
local_port="8800"
time_out=2
remote_mac=[{"addr":"127.0.0.1","port":"8803"},
	{"addr":"127.0.0.1","port":"8802"}]
