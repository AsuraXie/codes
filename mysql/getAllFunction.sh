#!/usr/bin/env bash
#set -x
#set -e

server=`cat db | grep server | awk -F "=" '{print $2}'`
user=`cat db | grep user | awk -F "=" '{print $2}'`
password=`cat db | grep password | awk -F "=" '{print $2}'`
port=`cat db | grep port | awk -F "=" '{print $2}'`

if [[ $server = "" ]] || [[ $user = "" ]] || [[ $password = "" ]] || [[ $port = "" ]] ;then
	echo "server or user or password or port is empty"
	exit;
fi

mysql -h $server -P $port -u $user -p$password << EOF > proc
use mysql;
select db,name,type,body from proc;
exit
EOF
sed -n '2,$p' proc | awk '{db=$1;name=$2;ttype=$3;content="";for(i=4;i<=NF;i++){if(i==4){content=content$i;}else{content=(content" "$i)}};system("echo  \""content"\" > "db"."ttype"."name);}'
#sed -n '2,$p' proc | awk -F "\t" 'Begin{system("echo $3;cat $3 > $1$2");}' 
