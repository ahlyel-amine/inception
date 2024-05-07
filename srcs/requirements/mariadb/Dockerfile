FROM debian:bullseye

RUN apt update && apt install -y --no-install-recommends  \
    mariadb-server=1:10.5.23-0+deb11u1 python3 && apt clean && rm -rf /var/lib/apt/lists/*

COPY ./tools/script.py /

EXPOSE 3306

ENTRYPOINT [ "python3", "script.py"]
