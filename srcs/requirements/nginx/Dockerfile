FROM debian:bullseye

RUN apt update -y && apt install nginx openssl python3 -y --no-install-recommends && \
    apt clean && rm -rf  /var/lib/apt/lists/* && \
    mkdir -p /etc/nginx/ssl/ && \
    openssl req -x509 -newkey rsa:4096 -nodes -keyout /etc/nginx/ssl/inception.key -out /etc/nginx/ssl/inception.crt -sha256 -days 365 -subj "/C=MA/ST=BeniMellal/L=Khouribga/O=1337/OU=io/CN=inception/"

COPY conf/default etc/nginx/sites-enabled/

EXPOSE 443
ENTRYPOINT ["nginx", "-g", "daemon off;"]
