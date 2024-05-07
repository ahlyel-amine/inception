
FROM debian:bullseye

RUN apt update
RUN apt-get install -y php php-mysqli
RUN apt-get install -y wget

WORKDIR /var/www

RUN wget -O adminer.php https://www.adminer.org/latest.php && \
    mv adminer.php index.php && chown -R root:root /var/www/

EXPOSE 8080

CMD [ "php", "-S", "0.0.0.0:8080"]