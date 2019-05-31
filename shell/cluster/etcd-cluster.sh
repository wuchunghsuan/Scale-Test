#!/bin/bash
. ./hosts.sh
. ./function-cluster.sh

for host in ${HOSTS[@]}
do
	echo -e "${GREEN}----- START DATANODE $host ------${END}"
	start_etcd $host
done
