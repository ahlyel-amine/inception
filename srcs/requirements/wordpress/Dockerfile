FROM debian:bullseye-slim

RUN apt update && apt install -y --no-install-recommends \
    wordpress ftp default-mysql-client php-fpm php-mysql curl python3 && \
    apt clean && rm -rf /var/lib/apt/lists/* && \
    chmod 755 /var/www/html/  && \
    curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar && \ 
    chmod +x wp-cli.phar && \
    mv wp-cli.phar /usr/local/bin/wp && \
    wp core download --path=/var/www/html/ --allow-root && \
    mv /var/www/html/wp-config-sample.php /var/www/html/wp-config.php > /dev/null 2>&1 

COPY ./tools/script.py /

EXPOSE 9000

ENTRYPOINT [ "python3", "script.py"]
