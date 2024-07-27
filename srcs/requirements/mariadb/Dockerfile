FROM debian:bullseye

RUN apt-get update && apt-get install -y \
    --no-install-recommends  \
    mariadb-server python3 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY ./config/50-server.cnf /etc/mysql/mariadb.conf.d/
COPY ./tools/script.py /

# EXPOSE 3306

CMD [ "python3", "script.py"]
