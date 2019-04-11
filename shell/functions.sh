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
