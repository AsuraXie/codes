#!/usr/bin/env bash
#set -x
#set -e
width=30
height=10
persons=40
#颜色定义
color_red=31
color_green=32
color_yellow=33
color_blue=34
color_purple=35
color_white=37

declare -a cells
declare -a cells_new

#初始化数组
function init(){
	for ((i=0;i<width*height;i++))
	do
		cells[i]=0
		cells_new[i]=0
	done

	total=`expr $width \* $height`
	for ((i=0;i<persons;i++))
	do
		loc=`expr $RANDOM % $total`
		cells[$loc]=1
		cells_new[$loc]=1
	done
}

#判断是否活着
function judge_life(){

	for ((i=1;i<`expr $height - 1`;i++))
	do
		for ((j=1;j<`expr $width - 1`;j++))
		do
			local points=${cells[$j]}
			local loc=`expr $i \* $width + $j`
			#左边的值
			local val_z=${cells[`expr $loc - 1 `]}
			#右边的值
			local val_y=${cells[`expr $loc + 1 `]}
			#上边值的坐标
			local loc_h=`expr $loc + $width`
			#下边值的坐标
			local loc_l=`expr $loc - $width`
			#上边值
			local val_h=${cells[$loc_h]}
			#下边值
			local val_l=${cells[$loc_l]}

			points=`expr $points + $val_z`
			points=`expr $points + $val_y`
			points=`expr $points + $val_h`
			points=`expr $points + $val_l`
			if [[ $points > 3 ]] || [[ $points = 3 ]] ;then
				cells_new[$loc]=0
			elif [[ $points < 2 ]];then
				cells_new[$loc]=0
			else 
				cells_new[$loc]=1
			fi
		done
	done

	for ((i=0;i<width;i++))
	do
		for ((j=0;j<height;j++))
		do
			local loc=`expr $i \* $j`
			if [[ ${cells_new[$loc]} > 0 ]];then
				cells[$loc]=1
			else
				cells[$loc]=0
			fi
		done
	done
}

#显示
function display(){
        x=$1
        y=$2
        content="$3"
        color=$4
        if [[ ! -n "$color" ]] ;then
                color=32
        fi
        loc="\033["$y";"$x"H\033[;"$color"m"$content"\033[0m"
        echo -e "$loc"
}

#输出显示
function show(){
	for ((i=0;i<width;i++))
	do
		for ((j=0;j<=height;j++))
		do
			local loc=`expr $i \* $j`
			if (( cells_new[$loc]==0 ));then
				display $i $j 0 $color_white
			else
				display $i $j ${cells_new[$loc]} $color_green
			fi

		done
	done
}

init
#show
while true
do
	judge_life
	show
	sleep 5
done
