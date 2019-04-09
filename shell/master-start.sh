#!/bin/bash
docker run -itd \
--name hadoop-master \
--network=net1 \
--hostname 10.11.0.1 \
--ip 10.11.0.1 \
-p 8088:8088 \
-p 8030:8030 \
-p 8031:8031 \
-p 8032:8032 \
-p 8033:8033 \
-p 9000:9000 \
-p 50070:50070 \
-p 10020:10020 \
wuchunghsuan/hadoop-master


