from os import system

system("mkdir -p /var/run/vsftpd/empty /etc/ssl/certs/")
system("useradd saba")
system("""passwd saba << EOF
saba
saba
""")
system("mkdir -p /home/saba/ftp")
system("chown -R saba:saba /home/saba")
system("echo saba:saba >> /etc/vsftpd.userlist")
system("vsftpd /etc/vsftpd.conf")
