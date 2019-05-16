#!/bin/bash

function draw_average() {
	JOB_ID=$1
	echo "python average.py ${JOB_ID}"
	python average.py $JOB_ID
}

function draw_fetch() {
	JOB_ID=$1
	echo "python average_fetch.py ${JOB_ID}"
	python average_fetch.py $JOB_ID
}

IDS=(
application_1557987582981_0001
application_1557987582981_0002
application_1557987582981_0004
application_1557987582981_0005
application_1557987582981_0008
application_1557987582981_0009
application_1557987582981_0011
application_1557987582981_0012
)

for ID in ${IDS[@]}; do
	draw_average $ID
done

for ID in ${IDS[@]}; do
	draw_fetch $ID
done
