#!/usr/bin/env bash
#set -x
#set -e

cmd=$1        #捕获第一个参数
pid=$$        #当前脚本的进程pid
msg=msg       #消息管道文件
space=0       #空白
wall='x'      #墙壁
my_box='B'    #我的箱子
other_box='O' #其他的箱子
box_length=30 #地图宽
box_height=20 #地图高
#颜色定义
color_red=31
color_green=32
color_yellow=33
color_blue=34
color_purple=35
color_white=37
#贪吃蛇的坐标
snake_x=(10 10 10)
snake_y=(10 11 12)
old_snake_x=("${snake_x[@]}")
old_snake_y=("${snake_y[@]}")
#最近一次输入方向
last_direct='up'
#地图
old_map=( x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x 
          x 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 x 
          x 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 x 
          x 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 x 
          x 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 x 
          x 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 x 
          x 0 0 M 0 0 0 0 0 0 0 M 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 x 
          x 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 M 0 x 
          x 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 x 
          x 0 0 0 0 0 0 M 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 x 
          x 0 0 0 0 0 0 0 0 0 B B B 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 x 
          x 0 0 0 M 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 x 
          x 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 x 
          x 0 0 0 0 0 0 0 0 0 M 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 x 
          x 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 x 
          x 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 x 
          x 0 0 0 0 0 0 0 0 0 0 0 0 0 M 0 0 0 0 0 0 0 0 0 0 0 0 0 0 x 
          x 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 x 
          x 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 x 
          x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x )

#退出函数
logout()
{
old_map=( x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x 
          x 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 x 
          x 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 x 
          x 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 x 
          x 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 x 
          x 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 x 
          x 0 0 o o 0 0 0 o 0 0 0 0 o 0 o o o o o o 0 0 o o o o o 0 x 
          x 0 o 0 0 o 0 0 o 0 0 0 0 o 0 o 0 0 0 0 0 0 0 o 0 0 0 o 0 x 
          x o 0 0 0 0 o 0 o 0 0 0 0 o 0 o 0 0 0 0 0 0 0 o 0 0 0 o 0 x 
          x o 0 0 0 0 o 0 o 0 0 0 0 o 0 o 0 0 0 0 0 0 0 o o o o o 0 x 
          x o 0 0 0 0 o 0 o 0 0 0 0 o 0 o o o o o o 0 0 o o 0 0 0 0 x 
          x o 0 0 0 0 o 0 o 0 0 0 o 0 0 o 0 0 0 0 0 0 0 o 0 o 0 0 0 x 
          x 0 o 0 0 o 0 0 0 o 0 o 0 0 0 o 0 0 0 0 0 0 0 o 0 0 o 0 0 x 
          x 0 0 o o 0 0 0 0 0 o 0 0 0 0 o o o o o o 0 0 o 0 0 0 o 0 x 
          x 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 x 
          x 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 x 
          x 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 x 
          x 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 x 
          x 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 x 
          x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x )
    if [[ $pid != "" ]];then
        showAllMap
        pids=`ps -ef | grep snake | grep bash | awk '{print $2}'`
        kill -SIGINT $pids > /dev/null 2>&1 
    fi
    exit
}

#退出游戏
exitGame(){
    pids=`ps -ef | grep snake | grep bash | awk '{print $2}'`
    kill -SIGINT $pids > /dev/null 2>&1 
}

#在某个点上显示数据
showPoint(){
    x=`expr $1 + 1`
    y=`expr $2 + 1`
    content="$3"
    color=$4
    if [[ ! -n "$color" ]] ;then
            color=$color_red
    fi
    #颜色
    if [[ $content == 'B' ]];then
        color=$color_green
    elif [[ $content == 'M' ]];then
        color=$color_yellow
    elif [[ $content == '0' ]];then
        content=' '
    fi
    loc="\033["$x";"$y"H\033["$color"m$content\033[0m"
    echo -e "$loc"
}

#显示变化的地图信息
showChangedMap(){
    snake_length=`expr ${#old_snake_x[@]}`
    for ((i=0;i<$snake_length;i++))
    do
        tmp_x=${old_snake_x[$i]}
        tmp_y=${old_snake_y[$i]}
        showPoint $tmp_x $tmp_y ' '
    done

    snake_length=`expr ${#snake_x[@]}`
    for ((i=0;i<$snake_length;i++))
    do
        tmp_x=${snake_x[$i]}
        tmp_y=${snake_y[$i]}
        showPoint $tmp_x $tmp_y 'B'
    done
}

#显示完整地图
showAllMap(){
    for ((i=0;i<$box_height;i++))
    do
        for ((j=0;j<$box_length;j++))
        do
            point=`expr $i \* $box_length + $j`
            showPoint $i $j "${old_map[$point]}"
        done
    done
}

#初始化函数，创建进程间管道通信
init()
{
    if [[ ! -p $msg ]];then
        mkfifo $msg
    fi
    showAllMap

    if [[ $cmd != "" ]];then
        pid=""
    fi
}

#写数据到管道
put()
{
    data=$1
    echo $data > $msg
}

#处理贪吃蛇移动
process()
{
    #暂存输入
    cmd=$1
    grow=$2
    #蛇头
    cur_x=${snake_x[0]}
    cur_y=${snake_y[0]}
    #新的位置
    new_x=$cur_x
    new_y=$cur_y
    #复制蛇变化情况
    old_snake_x=("${snake_x[@]}")
    old_snake_y=("${snake_y[@]}")

    if [[ $cmd == 'up' ]];then
        new_x=`expr $cur_x - 1`
        if [[ $new_x -eq 0 ]];then
            exitGame
        fi
    elif [[ $cmd == 'down' ]];then
        new_x=`expr $cur_x + 1`
        if [[ $new_x -eq `expr $box_height - 1` ]];then
            exitGame
        fi
    elif [[ $cmd == 'left' ]];then
        new_y=`expr $cur_y - 1`
        if [[ $new_y -eq 0 ]];then
            exitGame
        fi
    elif [[ $cmd == 'right' ]];then
        new_y=`expr $cur_y + 1`
        if [[ $new_y -eq `expr $box_length - 1` ]];then
            exitGame
        fi
    fi

    #如果需要生长
    position=`expr $new_x \* $box_length + $new_y`
    if [[ $grow == 'grow' ]] || [[ ${old_map[$position]} == 'M' ]] ;then
        snake_x=(0 "${snake_x[@]}")
        snake_y=(0 "${snake_y[@]}")
    fi

    snake_x[0]=$new_x
    snake_y[0]=$new_y

    if [[ $cmd != 'grow' ]];then
        snake_length=`expr ${#old_snake_x[@]}`
        for ((i=1;i<$snake_length;i++))
        do
            snake_x[$i]=${old_snake_x[`expr $i - 1`]}
            snake_y[$i]=${old_snake_y[`expr $i - 1`]}
        done
    fi
    showChangedMap
}

#从管道读取数据
get()
{
    while true
    do
        if read line < $msg ;then
            
            head_x=${snake_x[0]}
            head_y=${snake_y[0]}

            if [[ $line == 'up' ]] && [[ $last_direct != 'down' ]] ;then
                process $line
                last_direct=$line
            elif [[ $line == 'down' ]] && [[ $last_direct != 'up' ]] ;then
                process $line
                last_direct=$line
            elif [[ $line == 'left' ]] && [[ $last_direct != 'right' ]] ;then
                process $line
                last_direct=$line
            elif [[ $line == 'right' ]] && [[ $last_direct != 'left' ]] ;then
                process $line
                last_direct=$line
            elif [[ $line == 'co' ]];then
                loc=`expr $head_x \* $box_length + $head_y`
                if [[ ${old_map[$loc]} == 'M' ]];then
                    process $last_direct 'grow'
                else
                    process $last_direct
                fi
            elif [[ $line == 'feed' ]];then
                food_x=`echo "$RANDOM%20" | bc`
                food_y=`echo "$RANDOM%30" | bc`

                if [[ $food_x -eq 0 ]] ;then
                    food_x=1
                fi

                if [[ $food_y -eq 0 ]];then
                    food_y=1
                fi

                food_position=`expr $food_x \* $box_length + $food_y`
                box_map[$food_position]='M'
                showPoint $food_x $food_y 'M'
            fi
        fi
    done
}

#每秒钟发送信息
everySecondSend(){
    count=0
    while true
    do
        put "co"
        count=`expr $count + 1`
        rem=`echo "$count%2" | bc`
        if [[ $rem -eq 0 ]];then
            put "feed"
        fi
        sleep 2
    done
}

#ctl+c 信号捕获，跳入logout函数
trap "logout" SIGINT
init

if [[ $cmd == 'show' ]];then
    get &
elif [[ $cmd == 'signal' ]];then
    everySecondSend &
else
    #开启显示进程
    bash $0 'show'
    #每秒钟前进一步
    bash $0 'signal'

    inputs=(0 1 2)
    while true
    do
        read -s -n 1 key
        inputs[0]=${inputs[1]}
        inputs[1]=${inputs[2]}
        inputs[2]=$key
        if [ ${inputs[1]} == '[' ] ;then
            if [ ${inputs[2]} == 'A' ] ;then
                put "up"
            elif [ ${inputs[2]} == 'B' ] ;then
                put "down"
            elif [ ${inputs[2]} == 'C' ] ;then
                put "right"
            elif [ ${inputs[2]} == 'D' ] ;then
                put "left"
            fi
        elif [ $key == 'f' ] ;then
            echo "fire the whole"
        fi
    done
fi
