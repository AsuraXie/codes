#!/usr/bin/env bash
#set -e
#set -x

phone=$1
if [[ $phone = "" ]];then
	echo "phone is empty";
	exit;
fi

address=`cat db2 | grep server | awk -F "=" '{print $2}'`
user=`cat db2 | grep user | awk -F "=" '{print $2}'`
password=`cat db2  | grep password | awk -F "=" '{print $2}'`
port=`cat db2 | grep port | awk -F "=" '{print $2}'`
					 
if [[ $address = "" ]] || [[ $user = "" ]] || [[ $password = "" ]] || [[ $port = "" ]] ;then
	echo "address,user,password,port is not allowed empty"
	exit;
fi

function encodePhone()
{
	phone=$1

	phone_prefix=`echo ${phone:0:2}`
	phone_suffix=`echo ${phone:2}`
	temp_phone_suffix=$phone_suffix

	phone_suffix=`echo $(( temp_phone_suffix & 0xff000000 ))`

	temp=`echo $(( temp_phone_suffix & 0x0000ff00 ))`
	temp=`echo $(( temp << 8 ))`
	phone_suffix=`echo $(( phone_suffix + temp ))`

	temp=`echo $(( temp_phone_suffix & 0x00ff0000 ))`
	temp=`echo $(( temp >> 8 ))`
	phone_suffix=`echo $(( phone_suffix + temp ))`

	temp=`echo $(( temp_phone_suffix & 0x0000000f ))`
	temp=`echo $(( temp << 4 ))`
	phone_suffix=`echo $(( phone_suffix + temp ))`

	temp=`echo $(( temp_phone_suffix & 0x000000f0 ))`
	temp=`echo $(( temp >> 4 ))`
	phone_suffix=`echo $(( phone_suffix +temp ))`

	phone_suffix=`echo $(( phone_suffix ^ 21184816 ))`

	echo $phone_prefix$phone_suffix
}
rm userphone
encode_phone=`encodePhone $phone` 
echo "encode phone:"$encode_phone
mysql -h $address -P $port -u $user -p$password << EOF > userphone
use licaishi;
select * from lcs_user_index where phone=$encode_phone;
EOF

line_info=`cat userphone`
if [[ $line_info = "" ]] ; then
	echo "no such user in lcs_user_index";
	exit;
fi
	   
user_table=`sed -n '2p;' userphone | awk '{print $1}'`
s_uid=`sed -n '2p' userphone | awk '{print $2}'`
table_suffix=$(($user_table % 10))
mysql -h $address -P $port -u $user -p$password << EOF >> userphone
use licaishi;
select * from lcs_user_$table_suffix where s_uid='$s_uid'\G;
EOF
