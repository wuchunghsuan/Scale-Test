FROM wuchunghsuan/hadoop:latest

MAINTAINER chunghsuan.wu wuchunghsuan@gmail.com

ADD ./start-master.sh /
ADD ./hosts /etc/hosts
ADD ./hadoop/yarn-site.xml /wuchunghsuan/hadoop-2.8.5/etc/hadoop/yarn-site.xml
ADD ./hadoop/core-site.xml /wuchunghsuan/hadoop-2.8.5/etc/hadoop/core-site.xml

ENTRYPOINT ["/start-master.sh"]
