#!/bin/bash
RED="\033[31m"
GREEN="\033[32m"
YELLOW="\033[33m"
BLUE="\033[34m"
END="\033[0m"

JOB_ID=$1
WORKERS=(
192.168.2.11
192.168.2.12
192.168.2.13
192.168.2.14
192.168.2.15
192.168.2.16
192.168.2.17
192.168.2.18
)

WATCH=/home/wuchunghsuan/watchLog
HIBENCH=/home/wuchunghsuan/HiBench
LOG_DIR=/home/wuchunghsuan/log/nodemanager
OUTPUT_DIR=./spark

echo -e "${BLUE}Pull log ${RED}$JOB_ID${END}"

mkdir -p $OUTPUT_DIR/${JOB_ID}

for WORKER in ${WORKERS[@]}; do
	echo -e "${BLUE}Collect OPS log from ${RED}${WORKER}${GREEN}:${LOG_DIR}${END}"
	ssh ${WORKER} "cat ${LOG_DIR}/${JOB_ID}/container_*/stdout | grep '\[OPS\]'" >> ${OUTPUT_DIR}/${JOB_ID}/spark.log
	ssh ${WORKER} "cat ${LOG_DIR}/${JOB_ID}/container_*/stdout | grep '\[OPS-log\]'" >> ${OUTPUT_DIR}/${JOB_ID}/request.log
done

# cat ${LOG_DIR}/${JOB_ID}/container_*/stdout | grep "\[OPS-log\]" >> ${OUTPUT_DIR}/${JOB_ID}/request.log

cp -r $HIBENCH/report/sort/spark ${OUTPUT_DIR}/${JOB_ID}/

cp $HIBENCH/report/hibench.report ${OUTPUT_DIR}/${JOB_ID}/

cp $WATCH ${OUTPUT_DIR}/${JOB_ID}/
