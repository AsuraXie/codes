#!/usr/bin/env bash
#set -x
#set -e
echo "hello"

space=0      #空白
wall=1       #墙壁
my_box=2     #我的箱子
other_box=3  #其他的箱子
#地图
map=( 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 )
if_change=0  #地图是否发生变化，如果发生变化则重绘显示内容

logout()
{
    echo 'world'
    exit
}

trap "logout" SIGINT

inputs=(0 1 2)

while(true)
do
    read -s -n 1 key
    inputs[0]=${inputs[1]}
    inputs[1]=${inputs[2]}
    inputs[2]=$key
    if [ ${inputs[1]} == '[' ] ;then
        if [ ${inputs[2]} == 'A' ] ;then
            echo "上"
        elif [ ${inputs[2]} == 'B' ] ;then
            echo "下"
        elif [ ${inputs[2]} == 'C' ] ;then
            echo "右"
        elif [ ${inputs[2]} == 'D' ] ;then
            echo "左"
        fi
    elif [ $key == 'f' ] ;then
        echo "fire the whole"
    fi
done
