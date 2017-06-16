#!/bin/sh
#统计accessLog中每个url的pv数据
dataFile=$1
sort -u $dataFile > uniqData
while read line 
do
    echo `grep -r "$line" $dataFile | wc -l` "$line"
done < uniqData
rm uniqData
