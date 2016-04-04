#!/bin/bash
tar -cvf temp.tar ../
tar_file="temp.tar"
addr_base="192.168.0."
for ip in 201 202 203 204 205 206
do
	addr=$addr_base$ip
	echo $addr
	ssh asura@$addr "rm -rf *"
	res=$?
	echo "delete webfs $res"
	if [ $res -eq 0 ]
	then
		ssh asura@$addr "mkdir webfs"
		echo "mkdir finished"
		scp $tar_file asura@$addr:~/webfs
		echo "scp tar finished"
		ssh asura@$addr "tar xf webfs/temp.tar "
		echo "untar file finished"
		ssh asura@$addr "./kill_process.sh"
		echo "kill process finished"
		#ssh asura@$addr "./server.py --port 8802 &;echo abc"
		#echo "start server finished"
	fi
done

#scp /home/asura/codes/python/webfs/temp.tar asura@192.168.0.201:~/webfs
#scp * asura@192.168.0.202:~/webfs
#ssh 192.168.0.201 "./webfs/server.py --port 8802"
