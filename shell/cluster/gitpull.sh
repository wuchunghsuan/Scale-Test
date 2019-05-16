#!/bin/bash
. ./hosts.sh
. ./function-cluster.sh

for host in ${HOSTS[@]}
do
	echo -e "${GREEN}----- GIT PULL $host ------${END}"
	gitpull_cluster $host
done
