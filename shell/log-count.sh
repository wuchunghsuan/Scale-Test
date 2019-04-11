#!/bin/bash
RED="\033[31m"
GREEN="\033[32m"
YELLOW="\033[33m"
BLUE="\033[34m"
END="\033[0m"

JOB_ID=$1
EXPOSE_DIR=/home/wuchunghsuan/log-scale-test
OUTPUT_DIR=/home/wuchunghsuan/report-scale-test
OUTPUT_FILE=${OUTPUT_DIR}/report_$JOB_ID

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
                        		#Shuffle
                                TIME=`expr \`cat $LOG_FILE |grep shuffle-stop |awk -F - '{print $2}'\` - \`cat $LOG_FILE |grep shuffle-start |awk -F - '{print $2}'\``
                                NAME_SIZE=`cat $LOG_FILE |grep task |awk -F - '{print $2}	{print $3}'`
                                echo "Shuffle	${NAME_SIZE}   ${TIME}" >> $OUTPUT_FILE
                                #Fetch
				#for LOG in `cat $LOG_FILE |grep fetch_file`; do
                                #	FETCTH=`echo $LOG |awk -F - '{print $2}	{print $3}	{print $4}	{print $5}'`
                                #	echo "Fetch   ${FETCTH}" >> $OUTPUT_FILE	
                                #done
                                #Reduce
                                TIME=`expr \`cat $LOG_FILE |grep reduce-stop |awk -F - '{print $2}'\` - \`cat $LOG_FILE |grep reduce-start |awk -F - '{print $2}'\``
                                NAME=`cat $LOG_FILE |grep reduce-stop |awk -F - '{print $3}'`
                                echo "Reduce    ${NAME}   ${TIME}" >> $OUTPUT_FILE
                        fi
                        TEST=`cat $LOG_FILE |grep map-start`
                        if [ $TEST ]; then
                                TIME=`expr \`cat $LOG_FILE |grep map-stop |awk -F - '{print $2}'\` - \`cat $LOG_FILE |grep map-start |awk -F - '{print $2}'\``
                                NAME=`cat $LOG_FILE |grep map-stop |awk -F - '{print $3}'`
                                echo "Map       ${NAME}   ${TIME}" >> $OUTPUT_FILE
                        fi

                fi
        done
done
