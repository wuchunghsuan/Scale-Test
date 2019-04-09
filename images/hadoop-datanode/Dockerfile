#wuchunghsuan/hdfs-namenode:latest

FROM java:openjdk-8-jre

MAINTAINER chunghsuan.wu wuchunghsuan@gmail.com

ADD ./hadoop-2.8.5/ /wuchunghsuan/hadoop-2.8.5/
ADD ./start-datanode.sh /

ENTRYPOINT ["/start-datanode.sh"]
