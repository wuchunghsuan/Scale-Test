#!/bin/bash
NUM=$1
. ./functions.sh
echo -e "${BLUE}Start ${RED}$NUM${BLUE} hadoop workers.${END}"

SIZE=$((${NUM}+3))
for ((i=3;i<${SIZE};i++)); do
	NAME="10.11.1.$i"
	echo -e "Start ${RED}worker-$NAME${END} CPU_SET=$(($i - 3))"
	start_worker $NAME $(($i - 3))
done

./set-wondershaper.sh
