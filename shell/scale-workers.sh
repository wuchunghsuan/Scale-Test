#!/bin/bash
FROM=$1
NUM=$2
. ./ip.sh
. ./functions.sh

echo -e "${BLUE}Scale up ${RED}$NUM${BLUE} hadoop workers.${END}"

SIZE=$((${FROM}+${NUM}))
for ((i=${FROM};i<${SIZE};i++)); do
        NAME="${IP}.$i"
        echo -e "Start ${RED}worker-$NAME${END} CPU_SET=$(($i - 1))"
        start_worker $NAME $(($i - 1))
done

./set-wondershaper.sh
