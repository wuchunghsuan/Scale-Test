#!/bin/bash
cp /expose/conf/master-conf/* /wuchunghsuan/hadoop-2.8.5/etc/hadoop/
yes | /wuchunghsuan/hadoop-2.8.5/bin/hdfs namenode -format
/wuchunghsuan/hadoop-2.8.5/sbin/hadoop-daemon.sh start namenode
/wuchunghsuan/hadoop-2.8.5/bin/yarn resourcemanager
