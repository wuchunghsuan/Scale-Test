FROM wuchunghsuan/hadoop-base:latest

MAINTAINER chunghsuan.wu wuchunghsuan@gmail.com

ADD ./start-worker.sh /
ADD ./hosts /etc/hosts

ENTRYPOINT ["/start-worker.sh"]
