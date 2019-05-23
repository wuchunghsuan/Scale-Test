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

function start_ops_master() {
        docker run -itd \
        --name hadoop-master-ops \
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
	-p 14010:14010 \
	-p 14020:14020 \
        wuchunghsuan/ops-hadoop-master
}

function start_worker() {
	NAME=$1
	CPU_SET=$2
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

function start_ops_worker() {
        NAME=$1
        CPU_SET=$2
        docker run -itd \
        --network=net1 \
        --cpus="1" \
        --name worker-$NAME-ops \
        --hostname $NAME \
        --ip $NAME \
        -v /home/wuchunghsuan/expose/worker-$NAME:/expose \
        -v /home/wuchunghsuan/expose-conf:/expose/conf \
        wuchunghsuan/ops-hadoop-worker
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

function set_wondershaper() {
	CONTAINER_ID=$1
	U_LIMIT=$2
	D_LIMIT=$3
	echo -e "${BLUE}Limit container ${RED}${CONTAINER_ID}${BLUE} bandwidth with ${RED}${U_LIMIT} Kbps${BLUE} upload limit and ${RED}${D_LIMIT} Kbps${BLUE} download limit.${END}"

	PID=$(docker inspect -f '{{.State.Pid}}' $CONTAINER_ID)
	ln -sfT /proc/$PID/ns/net /var/run/netns/$CONTAINER_ID
	ip netns exec $CONTAINER_ID ip link add ifb0 type ifb
	ip netns exec $CONTAINER_ID ip link set dev ifb0 up
	ip netns exec $CONTAINER_ID wondershaper -a eth0 -u $U_LIMIT -d $D_LIMIT
}

function clean_all_wondershaper() {
        for CONTAINER_ID in `docker ps -a | grep worker- | awk '{print $1}'`; do
                clean_wondershaper $CONTAINER_ID
        done
}

function clean_wondershaper() {
	CONTAINER_ID=$1
	echo -e "${BLUE}Clean container ${RED}${CONTAINER_ID}${BLUE} bandwidth limit.${END}"
 
	ip netns exec $CONTAINER_ID wondershaper -c -a eth0
	#ip -all netns delete
}

function clean_etcd() {
	echo -e "${BLUE}Clean etcd.${END}"
        docker rm -f `docker ps -a | grep etcd | awk '{print $1}'`
}

function clean_worker() {
	clean_all_wondershaper
	echo -e "${BLUE}Clean workers.${END}"
	docker rm -f `docker ps -a | grep worker- | awk '{print $1}'`
	echo -e "${BLUE}Clean master.${END}"
	docker rm -f hadoop-master
	rm -rf /home/wuchunghsuan/expose/worker-*
	rm -rf /home/wuchunghsuan/expose/hadoop-master
}

function clean_all() {
	clean_all_wondershaper
	echo -e "${BLUE}Clean all.${END}"
	docker rm -f `docker ps -aq`
	rm -rf /home/wuchunghsuan/expose/*
}
