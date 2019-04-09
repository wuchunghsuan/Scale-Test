#wuchunghsuan/hdfs-namenode:latest

FROM wuchunghsuan/hadoop-master:0.1

MAINTAINER chunghsuan.wu wuchunghsuan@gmail.com

ADD ./start-namenode.sh /
ADD ./hadoop/hdfs-site.xml /wuchunghsuan/hadoop-2.8.5/etc/hadoop/hdfs-site.xml
ADD ./hadoop/core-site.xml /wuchunghsuan/hadoop-2.8.5/etc/hadoop/core-site.xml

ENTRYPOINT ["/start-namenode.sh"]
