# apk update 
# apk add vsftpd
# adduser -D -h /home/$FTP_USER -s /sbin/nologin $FTP_USER
# echo "$FTP_USER:$FTP_PASSWD" | chpasswd
# mkdir -p /home/$FTP_USER/ftp
# chown -R $FTP_USER:$FTP_USER /home/$FTP_USER
# chmod a-w /home/$FTP_USER
# mv /tmp/vsftpd.conf /etc/vsftpd/
# sed -i "s/docker_host_ip/$DOCKER_HOST_IP/g" /etc/vsftpd/vsftpd.conf
# mkdir -p /var/run/vsftpd/empty
# vsftpd /etc/vsftpd/vsftpd.conf
from os import system, environ
system(f"""adduser --disabled-password --home /home/saba --shell /usr/sbin/nologin saba << EOF
{environ['FTP_USER']}




Y
EOF
""")
system(f"echo {environ['FTP_USER']}:{environ['FTP_PASSWORD']} | chpasswd ")
system(f"mkdir -p /home/{environ['FTP_USER']}/ftp")
system(f"chown -R {environ['FTP_USER']}:{environ['FTP_USER']} /home/{environ['FTP_USER']}")
system(f"chmod -w /home/{environ['FTP_USER']}")
system("mkdir -p /var/run/vsftpd/empty")
system("vsftpd /etc/vsftpd.conf")
