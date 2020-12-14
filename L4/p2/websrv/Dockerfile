FROM httpd

SHELL ["/bin/bash", "-c"]
RUN apt-get -qq update
RUN apt-get -qq install -y apt-utils
RUN apt-get -qq install -y python3
RUN apt-get -qq install -y python3-pip
RUN apt-get -qq install -y libpq-dev

RUN chmod -R 755 /usr/local/apache2/cgi-bin
COPY ./httpd.conf /usr/local/apache2/conf/httpd.conf