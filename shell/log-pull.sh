#!/bin/bash
RED="\033[31m"
GREEN="\033[32m"
YELLOW="\033[33m"
BLUE="\033[34m"
END="\033[0m"

JOB_ID=$1
WORKERS=(192.168.2.12 192.168.2.16)
EXPOSE_DIR=/home/wuchunghsuan/expose
OUTPUT_DIR=/home/wuchunghsuan/log-scale-test

echo -e "${BLUE}Pull log ${RED}$JOB_ID${END}"

mkdir $OUTPUT_FILE

for WORKER in ${WORKERS[@]}; do
	scp -r ${WORKER}:${EXPOSE_DIR}/worker-* .
done
