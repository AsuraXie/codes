#!/bin/bash

plotfiles=""

for (( column=1;column<=11;column++ ))
do
	touch output/$column
	cat /dev/null > output/$column
	awk -F '/' '{ print $'$column'}' data/req.log > 'output/'$column
	sed = 'output/'$column | sed 'N;s/\n/\t/' > 'output/temp'
	cat 'output/temp' > 'output/'$column
	#plotfiles=$plotfiles" 'output/$column' with lines"
	#if [ $column!=11 ] 
	#then
	#	plotfiles=$plotfiles","
	#fi
done
rm 'output/temp'
#gnuplot -e "set title 'Response Time';set xlabel 'Count';set ylabel 'Time';set term jpeg size 1024,768 ; set output 'picture/response_time.jpg' ; plot 'output/1' title 'time_total' with line,'output/2' title 'time_namelookup' with line,'output/3' title 'time_connect' with line,'output/4' title 'time_appconnect' with line,'output/5' title 'time_pretransfer' with line,'output/6' title 'time_redirect' with line,'output/7' title 'time_starttransfer' with line,'output/8' title 'size_download' with line,'output/9' title 'size_upload' with line,'output/10' title 'size_header' with line,'output/11' title 'size_request' with line;replot"
