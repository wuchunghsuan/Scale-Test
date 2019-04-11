#!/bin/bash
cp /expose/conf/master-conf/* /wuchunghsuan/hadoop-2.8.5/etc/hadoop/
yes | /wuchunghsuan/hadoop-2.8.5/bin/hdfs namenode -format
/wuchunghsuan/hadoop-2.8.5/bin/hdfs namenode
