from os import system, environ
from re import sub
import time

time.sleep(10) # waiting for mariadb

fpm_config_file = "/etc/php/7.4/fpm/pool.d/www.conf"
wp_config_file = f"{environ['CERTS_']}/wp-config.php"

system("service	php7.4-fpm start")

with open(fpm_config_file, "r") as file:
    data = file.read()

data = sub('listen = /run/php/php7.4-fpm.sock', 'listen = 9000', data)

with open(fpm_config_file, "w") as file:
    file.write(data)

with open(wp_config_file, "r") as file:
    data = file.read()

data = sub('database_name_here', environ['MYSQL_DATABASE_NAME'], data)
data = sub('username_here', environ['MYSQL_USER'], data)
data = sub('password_here', environ['MYSQL_PASSWORD'], data)
data = sub('localhost', environ['MYSQL_HOST'], data)

with open(wp_config_file, "w") as file:
    file.write(data)

system(f"wp core install --path={environ['CERTS_']} --url={environ['WP_URL']} --title={environ['WP_TITLE']} --admin_user={environ['WP_ADMIN']} --admin_password={environ['WP_ADMIN_PSWD']} --admin_email={environ['WP_ADMIN_MAIL']} --allow-root")
system(f"wp plugin update --all --path={environ['CERTS_']} --allow-root")
system("service php7.4-fpm stop")
system("/usr/sbin/php-fpm7.4 -F")
