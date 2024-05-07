from os import environ,system

#constants

ROOT_PATH = environ['CERTS_']
SERVER_NAME = environ['WP_URL']
SSL_PATH_KEY= environ['SSL_PATH_KEY']
SSL_PATH_CERT= environ['SSL_PATH_CERT']
WP_PORTAL = environ['WP_PORTAL']
NGNIX_CONF_FILE = "/etc/nginx/sites-enabled/default"
NGNIX_LISTEN_ON = environ['NGNIX_LISTEN_ON']
SSL_PATH = environ['SSL_PATH']

NGNIX_CONF = f"""
server
{{
    listen {NGNIX_LISTEN_ON};
    server_name {SERVER_NAME};
    root {ROOT_PATH};
    index index.php index.html index.htm;

    ssl_certificate {SSL_PATH_CERT};
    ssl_certificate_key {SSL_PATH_KEY};
    ssl_protocols TLSv1.3;

    location ~ [^/]\\.php(/|$) {{
        include fastcgi_params;
        fastcgi_pass {WP_PORTAL};
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
    }}
}}
"""

#generate ssl key
system(f"mkdir -p {SSL_PATH}")
system(f"""openssl req -x509 -newkey rsa:4096 -nodes \
        -keyout {SSL_PATH_KEY} \
        -out {SSL_PATH_CERT} \
        -sha256 \
        -days 365 \
        -subj '/C=MA/ST=BeniMellal/L=Khouribga/O=1337/OU=io/CN=inception/'""")

# system("rm script.py")

# create ngnix conf file
with open(NGNIX_CONF_FILE, "w", encoding="utf-8") as file :
    file.write(NGNIX_CONF)
#launch ngnix deamon
system("nginx -g 'daemon off;'")