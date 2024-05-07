FROM debian:bullseye-slim

RUN apt update -y && apt install nginx openssl python3 -y --no-install-recommends && \
    apt clean && rm -rf  /var/lib/apt/lists/*

COPY ./tools/script.py /

EXPOSE 443

ENTRYPOINT ["python3", "script.py"]
