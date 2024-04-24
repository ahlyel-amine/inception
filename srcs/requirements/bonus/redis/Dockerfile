FROM debian:bullseye-slim

RUN apt update && apt install -y redis-server && apt clean && rm -rf /var/lib/apt/lists/*

COPY ./config/config /etc/redis/redis.conf

ENTRYPOINT [ "redis-server" ]
