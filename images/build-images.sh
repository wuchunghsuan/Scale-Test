#!/bin/bash
function build() {
	IMAGE=$1
	docker build -t wuchunghsuan/${IMAGE} ../images/${IMAGE}
}
#build hadoop-base
#build hadoop-master
#build hadoop-worker
#build hadoop-namenode
#build hadoop-datanode

#build ops-hadoop-base
#build ops-hadoop-master
build ops-hadoop-worker
