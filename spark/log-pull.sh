#!/bin/bash
RED="\033[31m"
GREEN="\033[32m"
YELLOW="\033[33m"
BLUE="\033[34m"
END="\033[0m"

JOB_ID=$1
WORKERS=(192.168.2.11 192.168.2.12)
LOG_DIR=/home/wuchunghsuan/log/nodemanager
OUTPUT_DIR=./log

echo -e "${BLUE}Pull log ${RED}$JOB_ID${END}"

mkdir $OUTPUT_DIR

for WORKER in ${WORKERS[@]}; do
	echo -e "${BLUE}Collect OPS log from ${RED}${WORKER}${GREEN}:${LOG_DIR}${BLUE}"
	ssh ${WORKER} "cat ${LOG_DIR}/${JOB_ID}/container_*/stdout | grep OPS >> ${OUTPUT_DIR}/${JOB_ID}/spark.log"
done
