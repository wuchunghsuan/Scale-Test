#!/bin/bash
docker rm -f `docker ps -a | grep worker- | awk '{print $1}'`
docker rm -f hadoop-master
rm -rf /home/wuchunghsuan/expose/worker-*
#docker rm -f `docker ps -aq`
#rm -rf /home/wuchunghsuan/expose/*
