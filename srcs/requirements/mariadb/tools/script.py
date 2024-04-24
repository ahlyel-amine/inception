from os import environ, system, remove
import  time

system("service mariadb start")

time.sleep(5)

op = f"""
    CREATE DATABASE IF NOT EXISTS {environ["MYSQL_DATABASE_NAME"]};
    CREATE USER IF NOT EXISTS '{environ["MYSQL_USER"]}'@'%' IDENTIFIED BY '{environ["MYSQL_PASSWORD"]}';
    GRANT ALL PRIVILEGES ON {environ["MYSQL_DATABASE_NAME"]}.* TO '{environ["MYSQL_USER"]}'@'%';
    ALTER USER 'root'@'localhost' IDENTIFIED BY '{environ["MYSQL_PASSWORD"]}';
    flush privileges;
"""

with open("./db.sql", "w") as file:
    file.write(op)

system("mariadb -h localhost < db.sql")
remove("./db.sql")
system(f"mysqladmin -u root -p{environ['MYSQL_PASSWORD']} shutdown")
system("mariadbd")
