#!/bin/bash
RED="\033[31m"
GREEN="\033[32m"
YELLOW="\033[33m"
BLUE="\033[34m"
END="\033[0m"

JOB_ID=$1

LOG=./spark/$JOB_ID/watchLog
mkdir ./spark/$JOB_ID/watchData
OUTPUT_CREATE=./spark/$JOB_ID/watchData/create
OUTPUT_DELETE=./spark/$JOB_ID/watchData/delete

echo -e "${BLUE}Grep watchLog ${RED}$JOB_ID${END}"

cat $LOG | grep CREATE | grep "blockmgr" >> $OUTPUT_CREATE
sed -i '' "/ISDIR/d" $OUTPUT_CREATE
cat $LOG | grep DELETE | grep "blockmgr" >> $OUTPUT_DELETE
