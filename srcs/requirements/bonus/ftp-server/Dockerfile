FROM debian:bullseye

RUN apt update && apt upgrade -y && apt install -y --no-install-recommends \
    vsftpd openssl python3 && apt clean && rm -rf /var/lib/apt/lists/*
RUN mkdir -p /etc/ssl/certs

COPY ./tools/script.py /
COPY ./conf/vsftpd.conf /etc/vsftpd.conf

EXPOSE 20 21 21110 21100

ENTRYPOINT ["python3", "script.py"]
