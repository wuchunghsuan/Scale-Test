#!/bin/bash
. ./hosts.sh
. ./function-cluster.sh

for host in ${HOSTS[@]}
do
	echo -e "${GREEN}----- CLEAN ALL $host ------${END}"
	clean_etcd_cluster $host
done
