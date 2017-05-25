#!/usr/bin/env bash

while read line;
do
    video_id=`echo $line | awk '{print $1}'`
    video_title=`echo $line | awk '{print $2}'`
    video_length=`echo $line | awk '{print $3}'`
    echo "mysql -h 10.55.30.35 -u root -p123456q licaishi -e \"insert into lcs_course_class (course_id,chapter_id,type,p_uid,rtmp_url,title,content,length,c_time,u_time) values(1,1,5,'1451326947',$video_id,'$video_title','$video_title',$video_length,'2017-04-07 00:00:00','2017-04-07 00:00:00')\"" >> output
done < data
