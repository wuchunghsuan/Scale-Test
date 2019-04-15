#!/bin/bash
RED="\033[31m"
GREEN="\033[32m"
YELLOW="\033[33m"
BLUE="\033[34m"
END="\033[0m"

JOB_ID=$1
WORKERS=(192.168.2.16 192.168.2.12)
EXPOSE_DIR=/home/wuchunghsuan/expose
OUTPUT_DIR=/home/wuchunghsuan/log-scale-test

echo -e "${BLUE}Pull log ${RED}$JOB_ID${END}"

mkdir $OUTPUT_DIR

for WORKER in ${WORKERS[@]}; do
	echo -e "${BLUE}SCP log from ${RED}${WORKER}${GREEN}:${EXPOSE_DIR}${BLUE} to ${GREEN}${OUTPUT_DIR}/${END}"
	scp -q -r ${WORKER}:${EXPOSE_DIR}/worker-* ${OUTPUT_DIR}
done
