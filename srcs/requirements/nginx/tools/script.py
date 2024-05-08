from os import environ, system

#constants
SSL_PATH = "/etc/nginx/ssl"
SSL_KEY= f"{SSL_PATH}/{environ['SSL_KEY']}"
SSL_CERT= f"{SSL_PATH}/{environ['SSL_CERT']}"

#generate ssl key
system(f"mkdir -p {SSL_PATH}")
system(f"""openssl req -x509 -newkey rsa:4096 -nodes \
        -keyout {SSL_KEY} \
        -out {SSL_CERT} \
        -sha256 \
        -days 365 \
        -subj '/C=MA/ST=BeniMellal/L=Khouribga/O=1337/OU=io/CN=inception/'""")

#launch ngnix deamon in the foreground
system("nginx -g 'daemon off;'")
