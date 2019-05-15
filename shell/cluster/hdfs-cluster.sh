#!/bin/bash
. ./hosts.sh
. ./function-cluster.sh

echo -e "${GREEN}----- START NAMENODE ${HOSTS[0]} ------${END}"
start_namenode ${HOSTS[0]}

for host in ${HOSTS[@]}
do
	echo -e "${GREEN}----- START DATANODE $host ------${END}"
	start_datanode $host
done
