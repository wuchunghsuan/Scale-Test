#!/bin/bash
. ./hosts.sh
. ./function-cluster.sh

name=$1
file=/home/wuchunghsuan/${name}.tar

docker save wuchunghsuan/${name}>${file}

for host in ${HOSTS[@]}
do
        echo -e "${GREEN}----- DISTRIBUTE $image TO $host ------${END}"
        distribute_image $host $name
done
