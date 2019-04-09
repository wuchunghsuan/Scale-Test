FROM wuchunghsuan/hadoop:latest

MAINTAINER chunghsuan.wu wuchunghsuan@gmail.com

ADD ./start-worker.sh /
ADD ./hosts /etc/hosts
ADD ./hadoop/yarn-site.xml /wuchunghsuan/hadoop-2.8.5/etc/hadoop/yarn-site.xml
ADD ./hadoop/core-site.xml /wuchunghsuan/hadoop-2.8.5/etc/hadoop/core-site.xml

ENTRYPOINT ["/start-worker.sh"]
