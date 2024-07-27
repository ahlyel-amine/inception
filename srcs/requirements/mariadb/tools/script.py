from os import environ, system, remove
import subprocess
from time import sleep
# constants
system("service mariadb start")
sleep(5)

MYSQL_DATABASE_NAME = environ["MYSQL_DATABASE_NAME"]
MYSQL_USER = environ["MYSQL_USER"]
MYSQL_PASSWORD = environ["MYSQL_PASSWORD"]

SQL_QUERIES = f"""
    CREATE DATABASE IF NOT EXISTS {MYSQL_DATABASE_NAME};
    CREATE USER IF NOT EXISTS '{MYSQL_USER}'@'%' IDENTIFIED BY '{MYSQL_PASSWORD}';
    GRANT ALL PRIVILEGES ON {MYSQL_DATABASE_NAME}.* TO '{MYSQL_USER}'@'%';
    FLUSH PRIVILEGES;
"""

SQL_QUERIES_FILE = "./db.sql"
shell_script = f"""
mysql_secure_installation << EOF 1>&2
n
{MYSQL_PASSWORD}
{MYSQL_PASSWORD}
y
n
n
n
n
EOF
"""
subprocess.run(shell_script, shell=True, check=False)

# create sql queries file
with open(SQL_QUERIES_FILE, "w", encoding="utf-8") as file:
    file.write(SQL_QUERIES)

# launch mariadb service
# execute sql queries
system(f"mariadb -u root -p{MYSQL_PASSWORD} < {SQL_QUERIES_FILE}")
remove(SQL_QUERIES_FILE)

# run mariadb deamon
system(f"mysqladmin -u root -p{ MYSQL_PASSWORD} shutdown")
system("mariadbd")
