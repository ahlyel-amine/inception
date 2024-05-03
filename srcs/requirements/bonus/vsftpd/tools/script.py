from re import sub
from os import system, environ

FTP_USER = environ['FTP_USER']
FTP_U_PSWD = environ['FTP_U_PSWD']
# HOME_DIR = f"/home/{FTP_USER}"
HOME_DIR = f"/var/www/html"
FTP_CONF_FILE = "/etc/vsftpd/vsftpd.conf"
FTP_USER_FILE = "/etc/vsftpd.userlist"
FTP_LOCK_PATH = "/var/run/vsftpd/empty"
FTP_SSL_PATH = "/etc/ssl/certs/"
SSL_SUBJ = "/C=MA/ST=BeniMellal/L=Khouribga/O=1337/OU=io/CN=inception/"
PASSWD_F_PATH = "/usr/sbin/chpasswd"

def replace(file, old_value, new_value):
    """Replace values within a given file"""
    with open(file, 'r', encoding="UTF-8") as f :
        data = f.read()
    data = sub(old_value, new_value, data)
    with open(file, 'w', encoding="UTF-8") as f :
        f.write(data)

# system(f"mkdir -p {HOME_DIR}")

system(f"""adduser --disabled-password --home {HOME_DIR} --shell /usr/sbin/nologin {FTP_USER}  << EOF
{FTP_USER}




Y
EOF
""")

system(f"echo {FTP_USER}:{FTP_U_PSWD} >> {PASSWD_F_PATH}")

system(f"chown -R {FTP_USER}:{FTP_USER} {HOME_DIR}")

system(f"echo {FTP_USER}:{FTP_USER} >> {FTP_USER_FILE}")

replace(FTP_CONF_FILE, "docker_host_ip", "vsftpd")

system(f"mkdir -p {FTP_LOCK_PATH} {FTP_SSL_PATH}")

system(f"openssl req -x509 -newkey rsa:4096 -nodes -keyout {FTP_SSL_PATH}inception.key -out {FTP_SSL_PATH}inception.crt -sha256 -days 365 -subj '{SSL_SUBJ}'")
system(f"chown -R ${FTP_USER}:${FTP_USER} /var/www/html/wp-content")
system(f"vsftpd {FTP_CONF_FILE}")
