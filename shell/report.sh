#!/bin/bash

function run() {
	JOB_ID=$1
	echo "log-count ${JOB_ID}"
	./log-count.sh $JOB_ID &
	echo "log-fetch ${JOB_ID}"
	./log-fetch.sh $JOB_ID &
}

IDS=(
application_1555319528923_0002
application_1555319528923_0003
application_1555319528923_0008
application_1555319528923_0009
application_1555319528923_0012
application_1555319528923_0014
application_1555319528923_0017
application_1555319528923_0018
application_1555319528923_0019
application_1555319528923_0021
application_1555319528923_0022
application_1555319528923_0024
application_1555319528923_0025
application_1555319528923_0028
)

for ID in $IDS; do
	run $ID
done
