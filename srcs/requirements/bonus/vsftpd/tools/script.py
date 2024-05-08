from os import system, environ

system("service vsftpd start")
system("mkdir -p /var/run/vsftpd/empty /etc/ssl/certs/")
system(f"""adduser --disabled-password --home /home/saba --shell /usr/sbin/nologin saba << EOF
{environ['FTP_USER']}




Y
EOF
""")

system(f"echo {environ['FTP_USER']}:{environ['FTP_U_PSWD']} | chpasswd ")
system(f"chown -R {environ['FTP_USER']}:{environ['FTP_USER']} /var/www/html")
system("echo saba >> /etc/vsftpd.userlist")
system(f"adduser {environ['FTP_USER']}:{environ['FTP_USER']} root")
system("""openssl req -x509 -newkey rsa:4096 -nodes \
        -keyout /etc/ssl/certs/inception.key\
        -out /etc/ssl/certs/inception.crt \
        -sha256 \
        -days 365 \
        -subj '/C=MA/ST=BeniMellal/L=Khouribga/O=1337/OU=io/CN=inception/'""")
system("service vsftpd stop")
system("vsftpd")
