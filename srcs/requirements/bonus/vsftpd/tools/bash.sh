#!/bin/bash

FTP_CONFIG_FILE="/etc/vsftpd.conf"
SSL_CERT="/etc/ssl/${SSL_CERT}"
SSL_CRT_KEY="/etc/ssl/${SSL_KEY}"

service vsftpd start
sleep 5

cat<<EOF > cr





y
EOF

#SET UP FTP USER
adduser --home /var/www/html $FTP_USER --disabled-password < cr
# rm cr
echo "${FTP_USER}:${FTP_PASSWORD}" | /usr/sbin/chpasswd
# chown -R $FTP_USER:$FTP_USER /var/www/html
echo $FTP_USER | tee -a /etc/vsftpd.userlist &> /dev/null
adduser ${FTP_USER} root

#CREATE SSL CERTIFICATE FOR FTP
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout $SSL_CRT_KEY -out $SSL_CERT -subj "/C=XX/ST=Morocco/L=Khoribga/O=42/OU=1337/CN=localhost"

#ADD&MODIFIE CUSTOM FTP CONFIGURATION
sed -i "s|#chroot_local_user=YES|chroot_local_user=YES|g"  $FTP_CONFIG_FILE && \
sed -i "s|#local_enable=YES|local_enable=YES|g"  $FTP_CONFIG_FILE && \
sed -i "s|#write_enable=YES|write_enable=YES|g"  $FTP_CONFIG_FILE && \
sed -i "s|#local_umask=022|local_umask=007|g"  $FTP_CONFIG_FILE 
# sed -i "s|ssl_enable=NO|ssl_enable=YES|g"  $FTP_CONFIG_FILE && \

#SSL CONFIG FOR FTP
# sed -i "s|rsa_cert_file=/etc/ssl/certs/ssl-cert-snakeoil.pem|rsa_cert_file=$SSL_CERT|g"  $FTP_CONFIG_FILE && \
# sed -i "s|rsa_private_key_file=/etc/ssl/private/ssl-cert-snakeoil.key|rsa_private_key_file=$SSL_CRT_KEY|g"  $FTP_CONFIG_FILE

# echo "allow_anon_ssl=YES" >> $FTP_CONFIG_FILE && \
# echo "force_local_data_ssl=YES" >> $FTP_CONFIG_FILE && \
# echo "force_local_logins_ssl=YES" >> $FTP_CONFIG_FILE && \
# echo "force_local_logins_ssl=YES" >> $FTP_CONFIG_FILE && \
# echo "ssl_tlsv1=YES" >> $FTP_CONFIG_FILE && \
# echo "ssl_sslv2=NO" >> $FTP_CONFIG_FILE && \
# echo "ssl_sslv3=NO" >> $FTP_CONFIG_FILE && \
# echo "require_ssl_reuse=NO" >> $FTP_CONFIG_FILE && \
# echo "ssl_ciphers=HIGH" >> $FTP_CONFIG_FILE && \

# echo "allow_writeable_chroot=YES" >> $FTP_CONFIG_FILE && \
# echo 'seccomp_sandbox=NO' >> $FTP_CONFIG_FILE && \
# echo 'pasv_enable=YES' >> $FTP_CONFIG_FILE

service vsftpd stop
# sleep 1000000000000
#LAUNCH FTP DAEMON
vsftpd
