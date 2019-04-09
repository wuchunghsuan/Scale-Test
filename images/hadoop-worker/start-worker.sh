#!/bin/bash
cp /expose/conf/worker-conf/* /wuchunghsuan/hadoop-2.8.5/etc/hadoop/
/wuchunghsuan/hadoop-2.8.5/bin/yarn nodemanager
