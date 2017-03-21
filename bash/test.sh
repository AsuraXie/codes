#!/usr/bin/env bash
#set -x
#set -e
clear
for (( i=1;i<=40;i++ ));
do
	echo -e ""
done;

count=0

x=25
y=5

function left()
{
	x=$(( $x-1 ))
}

function right()
{
	x=$(( $x+1 ))
}

function up()
{
	y=$(( $y+1 ))
}

function down()
{
	y=$(( $y-1 ))
}

#left
trap "left" USR1
#right
trap "right" USR2
#up
trap "up" WINCH
#down
trap "down" IO

while :
do
	if [[ $x -le 0 ]];then
		(( x=1 ))
	fi

	if [[ $x -ge 100 ]];then
		(( x=100 ))
	fi

	if [[ $y -le 0 ]];then
		(( y=1 ))
	fi

	if [[ $y -ge 10 ]];then
		(( y=10 ))
	fi

	count=$(( count+1 ))
	str="\033[$x;$y""H $count"
	echo -ne "\033[2J"
	echo -e $str
	sleep 0.02
done;
