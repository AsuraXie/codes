#!/usr/bin/env bash

input_db_config=$1

if [[ $1 == "-h" ]];then
	help_info=
	echo 
fi

if [[ $input_db_config == "" ]];then
	db_config="db"
else
	db_config=$input_db_config
fi

address=`cat $db_config | grep server | awk -F "=" '{ print $2 }'`
user=`cat $db_config | grep user | awk -F "=" '{ print $2 }'`
port=`cat $db_config | grep port | awk -F "=" '{ print $2 }'`
password=`cat $db_config | grep password | awk -F "=" '{ print $2 }'`
echo $address,$user,$port,$password

mysql -h $address -P $port -u $user -p$password << EOF > mysqluserinfo
use mysql;
select Host,User from user;
select * from user\G;
EOF
