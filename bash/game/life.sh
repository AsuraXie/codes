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
	total=`expr $width \* $height`
	for ((i=0;i<$total;i++))
	do
		cells[i]=0
		cells_new[i]=0
	done

	for ((i=0;i<persons;i++))
	do
		loc=`expr $RANDOM % $total`
		cells[$loc]=1
		cells_new[$loc]=1
	done

	for ((i=0;i<$height;i++))
	do
		for ((j=0;j<$width;j++))
		do
            if (( $i==0 )) || (( $j==0 )) || (( $i==`expr $height - 1` )) || (( $j==`expr $width - 1`));then
                loc=`expr $i \* $width + $j`
                cells_new[$loc]=0
		        cells[$loc]=0
            fi
        done
    done
}

#判断是否活着
function judge_life(){

	for ((i=1;i<`expr $height - 1`;i++))
	do
        show_str=""
		for ((j=1;j<`expr $width - 1`;j++))
		do
			local points=0
			local loc=`expr $i \* $width + $j`
			#左边的值
			local val_z=${cells[`expr $loc - 1 `]}
			#右边的值
			local val_y=${cells[`expr $loc + 1 `]}
			#上边值的坐标
			local loc_h=`expr $loc - $width`
			#下边值的坐标
			local loc_l=`expr $loc + $width`
			#上边值
			local val_h=${cells[$loc_h]}
            temp=`expr $loc_h - 1`
            val_h=`expr $val_h + ${cells[$temp]}`
            temp=`expr $loc_h + 1`
            val_h=`expr $val_h + ${cells[$temp]}`

			#下边值
			local val_l=${cells[$loc_l]}
            temp=`expr $loc_l - 1`
            val_l=`expr $val_l + ${cells[$temp]}`
            temp=`expr $loc_l + 1`
            val_l=`expr $val_l + ${cells[$temp]}`

			points=`expr $points + $val_z`
			points=`expr $points + $val_y`
			points=`expr $points + $val_h`
			points=`expr $points + $val_l`
            cells_new[$loc]=$points

			if [[ ${cells_new[$loc]} > 3 ]] || [[ ${cells_new[$loc]} < 2 ]];then
				cells[$loc]=0
			else
				cells[$loc]=1
			fi

			if (( ${cells[$loc]} == 0 ));then
                show_str=$show_str" "
			else
                show_str=$show_str"*"
			fi
		done
        display $i 0 "$show_str" $color_red
	done
}

#显示
function display(){
        x=`expr $1 + 1`
        y=`expr $2 + 1`
        content="$3"
        color=$4
        if [[ ! -n "$color" ]] ;then
                color=$color_red
        fi
        #loc="\033["$x";"$y"H\033["$color"m"$content"\033[0m"
        loc="\033["$x";"$y"H\033["$color"m$content\033[0m"
        echo -e "$loc"
}

#输出显示
function show(){
	for ((i=0;i<$height;i++))
	do
		for ((j=0;j<$width;j++))
		do
			local loc=`expr $i \* $width + $j`
			if (( ${cells[$loc]} == 0 ));then
				display $i $j ' ' $color_white
			else
			#	display $i $j ${cells[$loc]} $color_red
				display $i $j '*' $color_red
			fi
		done
	done
}

#输出空白板
function showBlank(){
	for ((i=0;i<$height;i++))
	do
        display $i 0 "                                                              "
	done
}

init
while true
do
    showBlank
	judge_life
	#show
	sleep 2
done
