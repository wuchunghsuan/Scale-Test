#!/bin/bash
RED="\033[31m"
GREEN="\033[32m"
YELLOW="\033[33m"
BLUE="\033[34m"
END="\033[0m"
ST_PATH="/home/wuchunghsuan/github/Scale-Test/shell/"

function do_ssh() {
	host=$1
	cmd=$2
	ssh $host "$cmd"
}

function do_scp() {
	host=$1
	from=$2
	to=$3
	echo "scp $from ${host}:${to}"
	scp $from ${host}:${to}
}

function sync_date() {
	host=$1
	cmd="ntpdate -u ntp.api.bz"
	do_ssh $host "$cmd"
} 

function gitpull_cluster() {
        host=$1
        cmd="cd /home/wuchunghsuan/github/Scale-Test/shell/; git pull"
        do_ssh $host "$cmd"
}

function clean_cluster() {
	host=$1
	cmd="cd /home/wuchunghsuan/github/Scale-Test/shell/; ./clean.sh -a"
	do_ssh $host "$cmd"
}

function clean_yarn_cluster() {
        host=$1
        cmd="cd /home/wuchunghsuan/github/Scale-Test/shell/; ./clean.sh"
        do_ssh $host "$cmd"
}

function clean_etcd_cluster() {
        host=$1
        cmd="rm -rf /home/wuchunghsuan/etcd; cd /home/wuchunghsuan/github/Scale-Test/shell/; ./clean-etcd.sh"
        do_ssh $host "$cmd"
}

function start_namenode() {
	host=$1
	cmd="cd $ST_PATH; ./namenode-start.sh"
	do_ssh $host "$cmd"
}

function start_datanode() {
        host=$1
        cmd="cd $ST_PATH; ./datanode-start.sh"
	do_ssh $host "$cmd"
}

function start_resourcemanager() {
        host=$1
        cmd="cd $ST_PATH; ./master-start.sh"
        do_ssh $host "$cmd"
}

function start_ops_master() {
        host=$1
        cmd="cd $ST_PATH; ./ops-master-start.sh"
        do_ssh $host "$cmd"
}

function ops_worker_scale() {
        host=$1
        from=$2
        num=$3
        cmd="cd $ST_PATH; ./ops-scale-workers.sh $from $num"
        do_ssh $host "$cmd"
}

function worker_scale() {
        host=$1
	from=$2
	num=$3
        cmd="cd $ST_PATH; ./scale-workers.sh $from $num"
        do_ssh $host "$cmd"
}

function distribute_image() {
	host=$1
	dir="/home/wuchunghsuan"
	name=$2
	file="${dir}/${name}.tar"
	cmd="docker load<${file}"
	do_scp $host $file $dir
	do_ssh $host "$cmd"
}
