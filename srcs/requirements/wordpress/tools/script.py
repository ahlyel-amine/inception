from os import system, environ
import subprocess
from re import sub
import time

# waiting for mariadb
time.sleep(10)

#constants
FPM_CONG_FILE = "/etc/php/7.4/fpm/pool.d/www.conf"
WP_CONF_FILE = f"{environ['CERTS_']}/wp-config.php"
MYSQL_DB_NAME = environ['MYSQL_DATABASE_NAME']
MYSQL_USER = environ['MYSQL_USER']
MYSQL_PASSWORD = environ['MYSQL_PASSWORD']
MYSQL_HOST = "mariadb"
WP_CERT = environ['CERTS_']
WP_URL = environ['WP_URL']
WP_TITLE = environ['WP_TITLE']
WP_ADMIN = environ['WP_ADMIN']
WP_ADMIN_PSWD = environ['WP_ADMIN_PSWD']
WP_ADMIN_MAIL = environ['WP_ADMIN_MAIL']

def replace(targetfile:str, old_values:list[str], new_values:list[str]):
    """replace old values by new one's in the target file"""
    with open(targetfile, "r", encoding="utf-8") as f:
        lol = f.read()
    for i, value in enumerate(old_values):
        lol = sub(value, new_values[i], lol)
    with open(targetfile, "w", encoding="utf-8") as f:
        f.write(lol)

# start fast-cgi process manager so wordpress can run the php based configuration
system("service	php7.4-fpm start")

# configure fast-cgi process manager config file
replace(FPM_CONG_FILE, ["listen = /run/php/php7.4-fpm.sock"], ["listen = 9000"])


# configure wordpress config file
default_values = ["database_name_here", "username_here", "password_here", "localhost"]
wp_conf_values = [MYSQL_DB_NAME, MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST]

replace(WP_CONF_FILE, default_values, wp_conf_values)

#install wordpress
system(f"""wp core install \
        --path={WP_CERT} \
        --url={WP_URL} \
        --title={WP_TITLE} \
        --admin_user={WP_ADMIN} \
        --admin_password={WP_ADMIN_PSWD} \
        --admin_email={WP_ADMIN_MAIL} \
        --allow-root""")
system(f"wp plugin install redis-cache --activate --path={WP_CERT} --allow-root")
system(f"wp plugin update --all --path={WP_CERT} --allow-root")
#install redis plugin
system(f"wp redis enable --path={WP_CERT}  --allow-root")
#install a theme
system(f"wp theme install blockstarter --activate --path={WP_CERT} --allow-root")

subprocess.run(f"chown -R www-data:www-data /var/www/html", shell=True, check=False)

system("service php7.4-fpm stop")

# stop the fpm service so we can run it as a main process in the foreground
system("php-fpm7.4 -F")
