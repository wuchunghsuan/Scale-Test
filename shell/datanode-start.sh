#!/bin/bash
docker run -itd \
--network=net1 \
--hostname 10.11.0.211 \
--ip 10.11.0.211 \
-v /home/wuchunghsuan/expose/datanode-1:/expose \
-v /home/wuchunghsuan/expose-conf:/expose/conf \
wuchunghsuan/hadoop-datanode
