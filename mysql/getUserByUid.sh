#!/usr/bin/env bash
#set -x
#set -e

uid=$1
if [[ $uid = "" ]] ;then
	echo "no input uid"
	exit
fi

address=`cat db2 | grep server | awk -F "=" '{print $2}'`
user=`cat db2 | grep user | awk -F "=" '{print $2}'`
password=`cat db2  | grep password | awk -F "=" '{print $2}'`
port=`cat db2 | grep port | awk -F "=" '{print $2}'`

if [[ $address = "" ]] || [[ $user = "" ]] || [[ $password = "" ]] || [[ $port = "" ]] ;then
	echo "address,user,password,port is not allowed empty"
	exit;
fi

rm userindex

mysql -h $address -P $port -u $user -p$password << EOF > userindex
use licaishi;
select * from lcs_user_index where id='$uid';
EOF

line_info=`cat userindex`
if [[ $line_info = "" ]] ; then
	echo "no such user in lcs_user_index";
	exit;
fi

user_table=`sed -n '2p;' userindex | awk '{print $1}'`
s_uid=`sed -n '2p' userindex | awk '{print $2}'`
table_suffix=$(($user_table % 10))

mysql -h $address -P $port -u $user -p$password << EOF >> userindex
use licaishi;
select * from lcs_user_$table_suffix where s_uid='$s_uid'\G;
EOF
