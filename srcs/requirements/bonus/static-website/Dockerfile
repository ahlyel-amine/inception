FROM debian:bullseye-slim

RUN apt update -y && apt install nginx -y --no-install-recommends

COPY conf/default etc/nginx/sites-enabled/
COPY ./tools/ /var/www/html/
EXPOSE 5484
ENTRYPOINT ["nginx", "-g", "daemon off;"]
