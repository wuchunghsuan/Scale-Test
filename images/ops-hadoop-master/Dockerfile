FROM wuchunghsuan/ops-hadoop-base:latest

MAINTAINER chunghsuan.wu wuchunghsuan@gmail.com

ADD ./start-master.sh /
ADD ./start-yarn.sh /

ENTRYPOINT ["/start-master.sh"]
