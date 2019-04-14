#!/bin/bash
RED="\033[31m"
GREEN="\033[32m"
YELLOW="\033[33m"
BLUE="\033[34m"
END="\033[0m"

function prepare_sort() {
	SIZE=${1}000000
	MAP=$2
	REDUCE=$3
	NAME=$(($SIZE/1000000000))
	COMMAND="/wuchunghsuan/hadoop-2.8.5/bin/hadoop \
--config /wuchunghsuan/hadoop-2.8.5/etc/hadoop \
jar /wuchunghsuan/hadoop-2.8.5/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.8.5.jar \
randomtextwriter \
-D mapreduce.randomtextwriter.totalbytes=${SIZE} \
-D mapreduce.randomtextwriter.bytespermap=$((${SIZE}/${MAP})) \
-D mapreduce.job.maps=${MAP} \
-D mapreduce.job.reduces=${REDUCE} \
hdfs://10.11.0.201:9000/HiBench/Sort/Input-${NAME}G"
	echo -e "${BLUE}Docker exec hadoop-master:${END}"
	echo -e "${GREEN}$COMMAND${END}"
	docker exec hadoop-master $COMMAND
}

function run_sort() {
        SIZE=${1}000000
        MAP=$2
        REDUCE=$3
        NAME=$(($SIZE/1000000000))
	RM_COMMAND="/wuchunghsuan/hadoop-2.8.5/bin/hadoop fs -rm -r -skipTrash /HiBench/Sort/Output-${NAME}G"
	COMMAND="/wuchunghsuan/hadoop-2.8.5/bin/hadoop \
--config /wuchunghsuan/hadoop-2.8.5/etc/hadoop \
jar /wuchunghsuan/hadoop-2.8.5/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.8.5.jar \
sort \
-outKey org.apache.hadoop.io.Text \
-outValue org.apache.hadoop.io.Text \
-r ${REDUCE} \
hdfs://10.11.0.201:9000/HiBench/Sort/Input-${NAME}G \
hdfs://10.11.0.201:9000/HiBench/Sort/Output-${NAME}G"
	echo -e "${BLUE}Docker exec hadoop-master:${END}"
	echo -e "${GREEN}$RM_COMMAND${END}"
	docker exec hadoop-master $RM_COMMAND
        echo -e "${GREEN}$COMMAND${END}"
        docker exec hadoop-master $COMMAND
}

prepare_sort 12800 128 32 
sleep 30
run_sort 12800 128 32 
sleep 30
run_sort 12800 128 32

#prepare_sort 25600 256 64
#sleep 30
#run_sort 25600 256 64
#sleep 30
#run_sort 25600 256 64

#prepare_sort 38400 384 96
#sleep 30
#run_sort 38400 384 96
#sleep 30
#run_sort 38400 384 96





