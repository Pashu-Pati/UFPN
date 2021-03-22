FROM ubuntu

RUN mkdir /opt/app
WORKDIR /opt/app
COPY run.sh /opt/app
RUN apt-get update -y && \
    apt-get install sshpass -y \
    && apt-get install systemd -y 
VOLUME /opt/app
EXPOSE 223
CMD ["/bin/bash", "sftp.sh"]
ENTRYPOINT ["sshpass -p '*,<R#!$(2udw{Zgz' sftp testuser@207.244.229.74:/opt/testuser/logfile.log"]
