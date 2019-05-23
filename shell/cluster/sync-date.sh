#!/bin/bash
. ./hosts.sh
. ./function-cluster.sh

for host in ${HOSTS[@]}
do
	echo -e "${GREEN}----- SYNC DATE $host ------${END}"
	sync_date $host
done
