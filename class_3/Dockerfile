FROM centos:7

MAINTAINER ax003d <ax003d@gmail.com>

RUN yum update -y && \
    yum install -y java-1.8.0-openjdk.x86_64 && \
    yum install -y php && \
    yum install -y wget && \
    yum install -y unzip && \
    yum install -y python-setuptools
ENV JAVA_HOME /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.65-3.b17.el7.x86_64
WORKDIR /opt
RUN wget http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm && \
    rpm -ivh mysql-community-release-el7-5.noarch.rpm && \
    yum update -y && \
    yum install -y mysql-server && \
    yum clean all
RUN mysql_install_db
RUN chown -R mysql:mysql /var/lib/mysql/mysql
RUN wget http://apache.fayea.com/tomcat/tomcat-7/v7.0.67/bin/apache-tomcat-7.0.67.zip && \
    unzip apache-tomcat-7.0.67.zip
RUN easy_install supervisor
ADD supervisord.conf /etc/supervisor/supervisord.conf

EXPOSE 8080, 8066, 9066

ENTRYPOINT ["supervisord -c /etc/supervisor/supervisord.conf -n"]
CMD [""]