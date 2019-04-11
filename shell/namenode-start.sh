#!/bin/bash
docker run -itd \
--network=net1 \
--name hadoop-namenode \
--hostname 10.11.0.201 \
--ip 10.11.0.201 \
-p 50070:50070 \
-v /home/wuchunghsuan/expose/namenode-1:/expose \
-v /home/wuchunghsuan/expose-conf:/expose/conf \
wuchunghsuan/hadoop-namenode
