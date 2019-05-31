#!/bin/bash
. ./hosts.sh
. ./function-cluster.sh

FROM=$1
NUM=$2

for host in ${HOSTS[@]}
do
	echo -e "${GREEN}----- SCALE UP WORKER $host FROM ${FROM} TO $((${FROM}+${NUM})) ------${END}"
	ops_worker_scale $host $FROM $NUM
done
