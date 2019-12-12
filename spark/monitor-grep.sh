#!/bin/bash
RED="\033[31m"
GREEN="\033[32m"
YELLOW="\033[33m"
BLUE="\033[34m"
END="\033[0m"

JOB_ID=$1

LOG=./spark/$JOB_ID/spark/monitor.log
OUTPUT=./spark/$JOB_ID/spark/network.log
OUTPUT2=./spark/$JOB_ID/spark/network_time.log
OUTPUT3=./spark/$JOB_ID/spark/disk.log
OUTPUT4=./spark/$JOB_ID/spark/disk_time.log

echo -e "${BLUE}Grep Network Throughput ${RED}$JOB_ID${END}"

# SAIL
# cat $LOG| egrep "Network\(label=\'total\'.*?)" -o| egrep "recv_bytes=[0-9]*" -o| egrep "[0-9]+" -o >> $OUTPUT
# cat $LOG| egrep "Network\(label=\'total\'.*?)" | egrep "timestamp.*?," -o| egrep "15[0-9]{8}" -o >> $OUTPUT2

# AWS
cat $LOG| egrep "\'net/total\': Network\(label.*?)" -o| egrep "recv_bytes=[0-9]*" -o| egrep "[0-9]+" -o >> $OUTPUT
cat $LOG| egrep "\'net/total\': Network\(label.*?)" | egrep "timestamp.*?," -o| egrep "15[0-9]{8}" -o >> $OUTPUT2
cat $LOG| egrep "\'disk/total\': Disk\(label=\'nvme0n1\'.*?)" -o| egrep "bytes_write=[0-9]*" -o| egrep "[0-9]+" -o >> $OUTPUT3
cat $LOG| egrep "\'disk/total\': Disk\(label=\'nvme0n1\'.*?)" | egrep "timestamp.*?," -o| egrep "15[0-9]{8}" -o >> $OUTPUT4

