#!/bin/bash
RED="\033[31m"
GREEN="\033[32m"
YELLOW="\033[33m"
BLUE="\033[34m"
END="\033[0m"

JOB_ID=$1
EXPOSE_DIR=/home/wuchunghsuan/log-scale-test
OUTPUT_DIR=/home/wuchunghsuan/report-scale-test
OUTPUT_FILE=${OUTPUT_DIR}/report-fetch-$JOB_ID

echo -e "${BLUE}Count phase time ${RED}$JOB_ID${END}"

mkdir -p $OUTPUT_DIR
if [ -e $OUTPUT_FILE ]; then
	rm -f $OUTPUT_FILE
fi
touch $OUTPUT_FILE

for WORKER_DIR in `ls $EXPOSE_DIR | grep worker`; do
        for LOG_DIR in `ls $EXPOSE_DIR/$WORKER_DIR/log/nodemanager/$JOB_ID`; do
                if [ -d $EXPOSE_DIR/$WORKER_DIR/log/nodemanager/$JOB_ID/$LOG_DIR ]; then
                        LOG_FILE=$EXPOSE_DIR/$WORKER_DIR/log/nodemanager/$JOB_ID/$LOG_DIR/stdout

                        TEST=`cat $LOG_FILE |grep shuffle-start`
                        if [ $TEST ]; then
                                #Fetch
				for LOG in `cat $LOG_FILE |grep fetch_file`; do
                                	FETCTH=`echo $LOG |awk -F - '{print $2"\t"$3"\t"$4"\t"$5}'`
                                	echo "Fetch   ${FETCTH}" >> $OUTPUT_FILE	
                                done
                        fi
                fi
        done
done
