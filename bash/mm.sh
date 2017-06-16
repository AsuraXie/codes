#!/usr/bin/env bash
#set -x
#set -e

#监控本地服务器相关指标，生成数据并转储到ElasticSearch中以便实时监控

#导入配置文件
source mm.conf

#程序运行局部变量，不要做任何修改
cpu_info=''
mem_info=''
disk_info=''
net_info=''

#统计CPU相关
function statCpu(){
    load_avg_info=`cat /proc/loadavg`
    load_avg_array=(${load_avg_info})
    cpu_info='"loadavg_1":'${load_avg_array[0]}',"loadavg_5":'${load_avg_array[1]}',"loadavg_15":'${load_avg_array[2]}
}

#统计内存相关
function statMem(){
    while read line
    do
        mem_item=`echo $line | awk '{print $1}'`
        mem_value=`echo $line | awk '{print $2}'`
        temp_mem_info='"'$mem_item'":'$mem_value
        if [[ $mem_info = '' ]];then
            mem_info=$temp_mem_info
        else
            mem_info=$mem_info','$temp_mem_info
        fi
    done < "/proc/meminfo"
}

#统计硬盘相关
function statDisk(){
    disk_source_info=`df | sed -n '2,$p' | awk '{print $6","$2","$4","$5}'`
    for item in `echo $disk_source_info | awk '{for(i=0;i<=NF;i++) print $i}'`
    do
        single_disk_info=(${item//,/ })
        disk_result_info='"'${single_disk_info[0]}'":{"total":'${single_disk_info[1]}',"ava_size":'${single_disk_info[2]}',"usage":'${single_disk_info[3]//%/}'}'
        if [[ $disk_info = '' ]]; then
            disk_info=$disk_result_info
        else
            disk_info=$disk_info','$disk_result_info
        fi
    done
}

#统计网络相关
function statNet(){
    net_info='"input":"0","output":"0"'
}

#存储数据到ES
function storeES(){
    #current_time=`date +"%Y-%m-%dT%H:%M:%SZ"`
    current_time=`date -Ins`
    current_date=`date +%Y-%m-%d`
    json_result='{"@timestamp":"'$current_time'","machine_name":"'$machine_name'","ip":"'$machine_ip'","disk_info":{'$disk_info'},"mem_info":{'$mem_info'},"cpu_info":{'$cpu_info'},"net_info":{'$net_info'}}'
    echo $json_result

    #echo `curl -l -H "Content-type: application/json" -X POST -d $json_result $es_addr/$es_index-$current_date/$machine_name`
}

#获取机器名字
function getMachineName(){
    if [[ $machine_name == '' ]] ; then
        machine_name=`uname -n`
    fi
}

#获取机器IP地址
function getMachineIP(){
    if [[ $machine_ip == '' ]];then
        machine_ip=`ifconfig | grep "inet addr" | awk '{print $2}' | awk -F ':' '{print $2}' | grep -v '127.'| grep -v '172.' | grep -v '192.'`
    fi
}

#初始化，获取机器名字及其IP地址
function init(){
    getMachineName
    getMachineIP
}

function main(){

    for item in `echo $stat_item | awk -F ',' '{for(i=1;i<=NF;i++) print $i}'`
    do
        case $item in
            cpu)
                statCpu
                ;;
            mem)
                statMem
                ;;
            disk)
                statDisk
                ;;
            net)
                statNet
                ;;
            *)
                echo "wrong stat item"
                ;;
        esac
    done
    storeES
}

#启动
init
main
