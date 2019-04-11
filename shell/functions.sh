#!/bin/bash
RED="\033[31m"
GREEN="\033[32m"
YELLOW="\033[33m"
BLUE="\033[34m"
END="\033[0m"

function start_master() {
	docker run -itd \
	--name hadoop-master \
	--network=net1 \
	--hostname 10.11.0.1 \
	--ip 10.11.0.1 \
	-v /home/wuchunghsuan/expose/hadoop-master:/expose \
	-v /home/wuchunghsuan/expose-conf:/expose/conf \
	-p 8088:8088 \
	-p 8030:8030 \
	-p 8031:8031 \
	-p 8032:8032 \
	-p 8033:8033 \
	-p 9000:9000 \
	wuchunghsuan/hadoop-master
}

function start_worker() {
	NAME=$1
	docker run -itd \
	--network=net1 \
	--cpus="1" \
	--name worker-$NAME \
	--hostname $NAME \
	--ip $NAME \
	-v /home/wuchunghsuan/expose/worker-$NAME:/expose \
	-v /home/wuchunghsuan/expose-conf:/expose/conf \
	wuchunghsuan/hadoop-worker
}

function start_namenode() {
	IP=$1

	docker run -itd \
	--network=net1 \
	--name hadoop-namenode \
	--hostname $IP \
	--ip $IP \
	-p 50070:50070 \
	-v /home/wuchunghsuan/expose/namenode-1:/expose \
	-v /home/wuchunghsuan/expose-conf:/expose/conf \
	wuchunghsuan/hadoop-namenode
}

function start_datanode() {
	IP=$1

	docker run -itd \
	--network=net1 \
	--hostname $IP \
	--ip $IP \
	-v /home/wuchunghsuan/expose/datanode-1:/expose \
	-v /home/wuchunghsuan/expose-conf:/expose/conf \
	wuchunghsuan/hadoop-datanode
}

function clean_worker() {
	echo -e "${BLUE}Clean workers.${END}"
	docker rm -f `docker ps -a | grep worker- | awk '{print $1}'`
	docker rm -f hadoop-master
	rm -rf /home/wuchunghsuan/expose/worker-*
}

function clean_all() {
	echo -e "${BLUE}Clean all.${END}"
	docker rm -f `docker ps -aq`
	rm -rf /home/wuchunghsuan/expose/*
}
