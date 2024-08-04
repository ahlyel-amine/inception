from os import system, environ
import subprocess

PORTAINER_PASSWORD = environ.get('PORTAINER_PASSWORD')

system("echo $PORTAINER_PASSWORD > /tmp/portianer_ps")
system("(sleep 1 ; rm /tmp/portianer_ps) &")
system("/portainer/portainer --bind=:2307 --admin-password-file=/tmp/portianer_ps")
