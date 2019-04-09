#!/bin/bash
yes | /wuchunghsuan/hadoop-2.8.5/bin/hdfs namenode -format
/wuchunghsuan/hadoop-2.8.5/sbin/hadoop-daemon.sh start namenode
/start-master.sh
