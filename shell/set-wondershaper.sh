#!/bin/bash
. ./functions.sh

while getopts 'c' OPT; do
	case $OPT in
		c) clean_all_wondershaper; exit 0;;
	esac
done

U_LIMIT=240000
D_LIMIT=240000
mkdir /var/run/netns
for CONTAINER_ID in `docker ps -a | grep worker- | awk '{print $1}'`; do
	set_wondershaper $CONTAINER_ID $U_LIMIT $D_LIMIT
done
