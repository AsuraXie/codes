#!/usr/bin/env bash
#set -x
#set -e
#监控本地服务器相关指标，生成数据并转储到ElasticSearch中以便实时监控

#配置本机名称，如果配置为空则使用默认主机名'uname -n'
machine_name=''
machine_ip='10.13.3.25'

#stat_item 统计指标,统计内容包括:cpu,mem,disk,net各项通过逗号隔开，比如:
stat_item=cpu,mem,disk,net

#ElasticSearch相关配置，包括主机ip，基础索引等信息
es_addr='http://es.sina.com.cn'
#假定es_index='example',则存入ES后的索引为example-20170426
es_index='mc'


#程序运行局部变量，不要做任何修改
cpu_info=''
mem_info=''
disk_info=''
net_info=''

function statCpu(){
    load_avg_info=`cat /proc/loadavg`
    load_avg_array=(${load_avg_info})
    cpu_info='"loadavg_1":"'${load_avg_array[0]}'","loadavg_5":"'${load_avg_array[1]}'","loadavg_15":"'${load_avg_array[2]}'"'
}

function statMem(){
    while read line
    do
        mem_item=`echo $line | awk '{print $1}'`
        mem_value=`echo $line | awk '{print $2}'`
        temp_mem_info='"'$mem_item'":"'$mem_value'"'
        if [[ $mem_info = '' ]];then
            mem_info=$temp_mem_info
        else
            mem_info=$mem_info','$temp_mem_info
        fi
    done < "/proc/meminfo"
}

function statDisk(){
    disk_source_info=`df | sed -n '2,$p' | awk '{print $6","$2","$4","$5}'`
    for item in `echo $disk_source_info | awk '{for(i=0;i<=NF;i++) print $i}'`
    do
        single_disk_info=(${item//,/ })
        disk_result_info='"'${single_disk_info[0]}'":{"total":"'${single_disk_info[1]}'","ava_size":"'${single_disk_info[2]}'","usage":"'${single_disk_info[3]}'"}'
        if [[ $disk_info = '' ]]; then
            disk_info=$disk_result_info
        else
            disk_info=$disk_info','$disk_result_info
        fi
    done
}

function statNet(){
    net_info='"input":"0","output":"0"'
}

function storeES(){
    current_time=`date +"%Y-%m-%dT%H:%M:%SZ"`
    current_date=`date +%Y-%m-%d`
    echo $current_time
    json_result='{"@timestamp":"'$current_time'","machine_name":"'$machine_name'","ip":"'$machine_ip'","disk_info":{'$disk_info'},"mem_info":{'$mem_info'},"cpu_info":{'$cpu_info'},"net_info":{'$net_info'}}'
    echo $json_result

    echo `curl -l -H "Content-type: application/json" -X POST -d $json_result $es_addr/$es_index-$current_date/$machine_name`
}

function getMachineName(){
    if [[ $machine_name = '' ]] ; then
        machine_name=`uname -n`
    fi
}

function getMachineIP(){
    machine_ip='10.13.3.25'
}

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
