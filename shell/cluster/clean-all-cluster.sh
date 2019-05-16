#!/bin/bash
. ./hosts.sh
. ./function-cluster.sh

for host in ${HOSTS[@]}
do
	echo -e "${GREEN}----- CLEAN ALL $host ------${END}"
	clean_cluster $host
done
