from os import environ, system, remove
import  time

# constants
MARIADB_CONF = "socket                  = /run/mysqld/mysqld.sock\nport                    = 3306\n"
MARIADB_CONF_FILE = "/etc/mysql/mariadb.conf.d/50-server.cnf"
MYSQL_DATABASE_NAME = environ["MYSQL_DATABASE_NAME"]
MYSQL_USER = environ["MYSQL_USER"]
MYSQL_PASSWORD = environ["MYSQL_PASSWORD"]
SQL_QUERIES = f"""
    CREATE DATABASE IF NOT EXISTS {MYSQL_DATABASE_NAME};
    CREATE USER IF NOT EXISTS '{MYSQL_USER}'@'%' IDENTIFIED BY '{MYSQL_PASSWORD}';
    GRANT ALL PRIVILEGES ON {MYSQL_DATABASE_NAME}.* TO '{MYSQL_USER}'@'%';
    ALTER USER 'root'@'localhost' IDENTIFIED BY '{MYSQL_PASSWORD}';
    flush privileges;
"""
SQL_QUERIES_FILE = "./db.sql"


# configure mariaddb server config file
with open(MARIADB_CONF_FILE, "r", encoding="utf-8") as fl:
    contents = fl.readlines()
contents[29] = "bind-address            = 0.0.0.0\n"
contents.insert(18, MARIADB_CONF)
with open(MARIADB_CONF_FILE, "w", encoding="utf-8") as fl:
    fl.writelines(contents)

#create sql queries file
with open(SQL_QUERIES_FILE, "w", encoding="utf-8") as file:
    file.write(SQL_QUERIES)

# launch mariadb service
system("service mariadb start")


# execute sql queries
system(f"mariadb -h localhost < {SQL_QUERIES_FILE}")
remove(SQL_QUERIES_FILE)

#remove script
# remove("/script.py")

# run mariadb deamon
system(f"mysqladmin -u root -p{MYSQL_PASSWORD} shutdown")
system("mariadbd")
