#!/bin/bash
RED="\033[31m"
GREEN="\033[32m"
YELLOW="\033[33m"
BLUE="\033[34m"
END="\033[0m"

function start_worker() {
	NAME=$1
	docker run -itd \
	--network=net1 \
	--cpus="2" \
	--name worker-$NAME \
	--hostname $NAME \
	--ip $NAME \
	-v /home/wuchunghsuan/expose/worker-$NAME:/expose \
	wuchunghsuan/hadoop-worker
}
