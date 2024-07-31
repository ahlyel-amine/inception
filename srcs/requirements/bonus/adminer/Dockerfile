
FROM debian:bullseye

RUN apt update && apt install -y php php-mysqli wget && apt clean && rm -rf /var/lib/apt/lists/*

WORKDIR /var/www/

RUN wget --no-check-certificate  -O adminer.php https://www.adminer.org/latest.php && \
    mv adminer.php index.php && chown -R root:root /var/www/

ENTRYPOINT [ "php", "-S", "0.0.0.0:8080"]
