#wuchunghsuan/hdfs-namenode:latest

FROM java:openjdk-8-jre

MAINTAINER chunghsuan.wu wuchunghsuan@gmail.com

ADD ./hadoop-2.8.5/ /wuchunghsuan/hadoop-2.8.5/
ADD ./start-datanode.sh /
ADD ./hadoop/hdfs-site.xml /wuchunghsuan/hadoop-2.8.5/etc/hadoop/hdfs-site.xml
ADD ./hadoop/core-site.xml /wuchunghsuan/hadoop-2.8.5/etc/hadoop/core-site.xml

ENTRYPOINT ["/start-datanode.sh"]
