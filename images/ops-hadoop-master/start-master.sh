#!/bin/bash
/start-yarn.sh &>yarn.log &

cp /expose/conf/ops-conf/* /wuchunghsuan/OPS/src/main/resources/
cd /wuchunghsuan/OPS/scripts
./ops.sh master start
