FROM debian:bullseye

RUN apt update && apt upgrade -y && apt install -y --no-install-recommends \
    vsftpd openssl python3 && apt clean && rm -rf /var/lib/apt/lists/*
RUN mkdir -p /ftp /etc/ssl/certs && \
    openssl req -x509 -newkey rsa:4096 -nodes -keyout /etc/ssl/certs/inception.key -out /etc/ssl/certs/inception.crt -sha256 -days 365 -subj "/C=MA/ST=BeniMellal/L=Khouribga/O=1337/OU=io/CN=inception/"

COPY ./tools/script.py /
COPY ./conf/vsftpd.conf /etc/vsftpd.conf

EXPOSE 20 21 21110 21100

ENTRYPOINT ["python3", "script.py"]
