FROM debian:bullseye-slim

RUN apt update
RUN --home {HOME_DIR} --shell /usr/sbin/nologin {FTP_USER} "" << EOF\
{FTP_U_PSWD}\
{FTP_U_PSWD}\
{FTP_USER}\
\
\
\
\
Y\
EOF\
"