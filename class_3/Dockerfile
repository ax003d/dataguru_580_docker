FROM centos:7

MAINTAINER ax003d <ax003d@gmail.com>

RUN yum update -y && \
    yum install -y java-1.8.0-openjdk.x86_64 \
                php \
                wget \
                unzip \
                python-setuptools
ENV JAVA_HOME /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.65-3.b17.el7.x86_64
WORKDIR /opt
RUN wget http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm && \
    rpm -ivh mysql-community-release-el7-5.noarch.rpm && \
    yum update -y && \
    yum install -y mysql-server && \
    yum clean all
RUN mysql_install_db
RUN chown -R mysql:mysql /var/lib/mysql/mysql
RUN wget http://apache.mirrors.spacedump.net/tomcat/tomcat-7/v7.0.67/bin/apache-tomcat-7.0.67.zip && \
    unzip apache-tomcat-7.0.67.zip && \
    rm -f apache-tomcat-7.0.67.zip
RUN wget https://github.com/MyCATApache/Mycat-download/raw/master/1.4-RELEASE/Mycat-server-1.4-release-20151019230038-linux.tar.gz && \
    tar -xzvf Mycat-server-1.4-release-20151019230038-linux.tar.gz && \
    rm -f Mycat-server-1.4-release-20151019230038-linux.tar.gz
ADD schema.xml /opt/mycat/conf/schema.xml
ADD wrapper.conf /opt/mycat/conf/wrapper.conf
ADD setuser.py /opt/
ENV MYCAT_USER mycat
ENV MYCAT_PWD mycat
RUN /usr/bin/python /opt/setuser.py
RUN easy_install supervisor
ADD supervisord.conf /etc/supervisor/supervisord.conf

EXPOSE 8080
EXPOSE 8066
EXPOSE 9066

ENTRYPOINT ["supervisord -c /etc/supervisor/supervisord.conf -n"]
CMD [""]