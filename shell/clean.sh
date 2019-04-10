#!/bin/bash
#docker rm -f `docker ps -a | grep worker- | awk '{print $1}'`
#rm -rf /home/wuchunghsuan/expose/worker-*
docker rm -f `docker ps -aq`
rm -rf /home/wuchunghsuan/expose/*
