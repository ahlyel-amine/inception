from os import system, environ, makedirs
import subprocess
# system("service vsftpd start")
from time import sleep

sleep(15)
makedirs("/var/run/vsftpd/empty", exist_ok=True)
makedirs("/var/www/html/", exist_ok=True)
makedirs("/etc/ssl/certs/", exist_ok=True)
FTP_USER = environ.get('FTP_USER')
FTP_PASSWORD = environ.get('FTP_PASSWORD')
ADDUSER = f"""
adduser --home /var/www/html/ {environ['FTP_USER']} --disabled-password << EOF





y
EOF
"""
if not system(f"id -u {FTP_USER} > /dev/null 2>&1"):
    print(f"User '{FTP_USER}' already exists.")
else:
    subprocess.run(ADDUSER, shell=True, check=False)
subprocess.run(f"echo {FTP_USER}:{FTP_PASSWORD} | /usr/sbin/chpasswd", shell=True, check=False)
subprocess.run(f"chown -R {FTP_USER}:{FTP_USER} /var/www/html/", shell=True, check=False)
subprocess.run(f"echo {FTP_USER} | tee -a /etc/vsftpd.userlist &> /dev/null", shell=True, check=False)
subprocess.run(f"adduser {FTP_USER} root", shell=True, check=False)

subprocess.run(f"chmod a-w /var/www/html/", shell=True, check=False)
system("""openssl req -x509 -newkey rsa:4096 -nodes \
        -keyout /etc/ssl/certs/inception.key\
        -out /etc/ssl/certs/inception.crt \
        -sha256 \
        -days 365 \
        -subj '/C=MA/ST=BeniMellal/L=Khouribga/O=1337/OU=io/CN=inception/'""")
system("vsftpd /etc/vsftpd.conf")
