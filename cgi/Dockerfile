ARG MYAPP_IMAGE=myorg/centos:latest
FROM $MYAPP_IMAGE
RUN dbus-uuidgen > /etc/machine-id
RUN yum repolist
RUN yum install epel-release -y
RUN yum repolist
RUN yum install shellinabox -y
RUN yum install openssh-server -y
RUN yum install openssh-clients -y
ARG username
RUN useradd $username
ARG password
RUN echo $password | passwd $username --stdin
RUN sed -i 's|# OPTS="-t -s /:SSH:host.example.com"|OPTS="-t -s /:SSH:0.0.0.0"|g' /etc/sysconfig/shellinaboxd
RUN sed -i 's|OPTS="--disable-ssl-menu -s /:LOGIN"|# OPTS="--disable-ssl-menu -s /:LOGIN"|g' /etc/sysconfig/shellinaboxd

