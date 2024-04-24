FROM debian:bullseye

RUN apt update && apt upgrade -y && apt install -y --no-install-recommends  \
    mariadb-server python3 && apt clean && rm -rf /var/lib/apt/lists/*

COPY ./conf/50-server.cnf /etc/mysql/mariadb.conf.d/
COPY ./tools/script.py /
EXPOSE 3306
# RUN chmod 777 /run/mysqld/mysqld.sock

ENTRYPOINT [ "python3", "script.py"]
