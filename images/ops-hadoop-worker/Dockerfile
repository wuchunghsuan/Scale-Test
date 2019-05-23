FROM wuchunghsuan/ops-hadoop-base:latest

MAINTAINER chunghsuan.wu wuchunghsuan@gmail.com

ADD ./start-yarn.sh /
ADD ./start-worker.sh /

ENTRYPOINT ["/start-worker.sh"]
