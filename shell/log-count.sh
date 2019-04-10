#!/bin/bash
RED="\033[31m"
GREEN="\033[32m"
YELLOW="\033[33m"
BLUE="\033[34m"
END="\033[0m"

JOB_ID=$1
EXPOSE_DIR=/home/wuchunghsuan/expose
OUTPUT_FILE=./output_$JOB_ID

echo -e "${BLUE}Grep ${RED}$JOB_ID${END}"

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
				TIME=`expr \`cat $LOG_FILE |grep shuffle-stop |awk -F - '{print $2}'\` - \`cat $LOG_FILE |grep shuffle-start |awk -F - '{print $2}'\``
				SIZE=`cat $LOG_FILE |grep task |awk -F - '{print $3}'`
				NAME=`cat $LOG_FILE |grep task |awk -F - '{print $2}'`
				echo "${NAME}	${TIME}	${SIZE}" >> $OUTPUT_FILE
				#cat $EXPOSE_DIR/$dir/syslog | grep -F "[IST]" >> $tmp_file
			fi
		fi
	done
done
