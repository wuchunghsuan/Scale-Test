#!/bin/bash
FROM=$1
NUM=$2
. ./ip.sh
. ./functions.sh

echo -e "${BLUE}Scale up ${RED}$NUM${BLUE} hadoop workers.${END}"

SIZE=$((${FROM}+${NUM}))
for ((i=${FROM};i<${SIZE};i++)); do
        NAME="${IP}.$i"
        echo -e "Start ${RED}worker-$NAME${END} CPU_SET=$(($i - 3))"
        start_worker $NAME $(($i - 3))
done

./set-wondershaper.sh
