FROM debian:bullseye

RUN apt update && apt install -y --no-install-recommends \
    vsftpd openssl python3 && apt clean && rm -rf /var/lib/apt/lists/*
RUN mkdir -p /etc/ssl/

COPY ./tools/script.py /
COPY ./conf/vsftpd.conf /etc/vsftpd.conf

EXPOSE 21

ENTRYPOINT ["python3", "script.py"]
