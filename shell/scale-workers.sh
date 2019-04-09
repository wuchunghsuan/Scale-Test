#!/bin/bash
FROM=$1
NUM=$2
. ./functions.sh

echo -e "${BLUE}Scale up ${RED}$NUM${BLUE} hadoop workers.${END}"

SIZE=$((${FROM}+${NUM}))
for ((i=${FROM};i<${SIZE};i++)); do
        NAME="10.11.0.$i"
        echo -e "Start ${RED}worker-$NAME${END}"
        start_worker $NAME
done
