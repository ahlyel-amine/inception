from os import system

system("mkdir -p /var/run/vsftpd/empty /etc/ssl/certs/")
system("useradd saba")
system("""passwd saba << EOF
saba
saba
""")
system("echo saba >> /etc/vsftpd.userlist")
system("vsftpd /etc/vsftpd.conf")
