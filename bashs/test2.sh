#!/usr/bin/env bash
bash test.sh&

function exitAll(){
	local pid_show
	(( pid_show=$1 ))
	kill -9 $pid_show
	exit
}

pid_show=`echo $!`

sig_left=10
sig_right=12
sig_up=28
sig_down=29

trap "exitAll $pid_show" INT
aKey=(0 0 0)
sp_key=`echo -ne "\033"`

while :
do
	read -s -n 1 key
	if [[ $key==$sp_key ]];then
		read -s -n 1 key
		if [[ $key=="[" ]];then
			read -s -n 1 key
			if [[ $key == 'A' ]];then
				kill -$sig_left $pid_show
			elif [[ $key == 'B' ]];then
				kill -$sig_right $pid_show
			elif [[ $key == 'C' ]];then
				kill -$sig_up $pid_show
			elif [[ $key == 'D' ]];then
				kill -$sig_down $pid_show
			else
				continue
			fi
		fi
	fi
done;
