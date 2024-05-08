
FROM debian:bullseye

RUN apt update && apt install -y php php-mysqli wget && apt clean && rm -rf /var/lib/apt/lists/*

WORKDIR /var/www/

RUN wget -O adminer.php https://www.adminer.org/latest.php && \
    mv adminer.php index.php && chown -R root:root /var/www/

EXPOSE 8080

ENTRYPOINT [ "php", "-S", "0.0.0.0:8080"]
