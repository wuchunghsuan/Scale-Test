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

function draw_fetch_rate() {
	JOB_ID=$1
	echo "python line_fetch_rate.py ${JOB_ID}"
	python line_fetch_rate.py $JOB_ID
}

function draw_job_time() {
	JOB_ID=$1
	echo "python job_time.py ${JOB_ID}"
	python job_time.py $JOB_ID
}

function draw_task_time() {
	JOB_ID=$1
	echo "python task_time.py ${JOB_ID}"
	python task_time.py $JOB_ID
}

IDS=(
application_1559641550938_0001
application_1559641550938_0002
application_1559641550938_0003
application_1559641550938_0004
)

for ID in ${IDS[@]}; do
	draw_average $ID
done

for ID in ${IDS[@]}; do
	draw_fetch $ID
done

for ID in ${IDS[@]}; do
	draw_fetch_rate $ID
done

for ID in ${IDS[@]}; do
	draw_job_time $ID
done

for ID in ${IDS[@]}; do
	draw_task_time $ID
done