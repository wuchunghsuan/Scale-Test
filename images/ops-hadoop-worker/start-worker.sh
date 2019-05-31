#!/bin/bash
/start-yarn.sh &>yarn.log &

cd /wuchunghsuan/OPS/scripts
./ops.sh worker start
