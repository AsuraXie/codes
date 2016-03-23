#!/bin/bash
lines=`wc -l data/spendtime.log | awk '{ print $1 }'`

touch cmd/mkdir
touch cmd/rename
touch cmd/rmdir
touch cmd/find
touch cmd/add
touch cmd/rm
touch cmd/ls
touch cmd/cd

cat data/spendtime.log | while read line

do
	cmd=`echo $line | awk -F '---' '{ print $3 }' `
	time=`echo $line | awk -F '---' '{ print $2 }' `
	size=`echo $line | awk -F '---' '{ print $4 }' `
	echo $time,$size >> cmd/$cmd
	echo $time,$size,$cmd
done
#gnuplot -e "set title 'Cmd Execute Time';set xlabel 'Count';set ylabel 'Time';set term jpeg size 1024,768;set output 'picture/cmd_execute_time.jpg';plot 'cmd/mkdir' title 'mkdir' with line,'cmd/rename' title 'rename' with line,'cmd/rmdir' title 'rmdir' with line,'cmd/find' title 'find' with line,'cmd/add' title 'add' with line,'cmd/rm' title 'rm' with line,'cmd/ls' title 'ls' with line,'cmd/cd' title 'cd' with line;replot"
#awk -F '---' '{ print $1,$2}' spendtime.log > 'cmd/'
