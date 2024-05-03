FROM debian:bullseye-slim

RUN apt update && apt upgrade -y && apt install -y --no-install-recommends \
    ftp vsftpd openssl python3 && apt clean && rm -rf /var/lib/apt/lists/*

COPY ./conf/vsftpd.conf /etc/vsftpd/vsftpd.conf
COPY ./tools/script.py ./
# COPY ./tools/ ./
# ENV FTP_USER=saba
# ENV FTP_U_PSWD=saba
# EXPOSE 21 21110 21100

ENTRYPOINT ["python3", "script.py"]
