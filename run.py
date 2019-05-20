#!/usr/bin/env python

import os
from func import *
import json

apt_update = 'update'   # update repository
apt_nodejs = 'nodejs'
apt_docker = 'docker-ce'

newhostname = 'host2'   # New hostname

#rename host
host_ren(newhostname)

# Add nodejs repo to APT sources
os.system('curl -sL https://deb.nodesource.com/setup_9.x | sudo -E bash -')

# Install nodeJS
install_apt(apt_nodejs)


# add PGP key
os.system('curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -')
#Add the Docker repo to APT sources
os.system('sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"')

# run apt-get update
print ("Updating apt...")
install_apt(apt_update)

# Install docker
install_apt(apt_docker)

# Json dump
jdate = { "year": "2000", "month": "12", "day": "1" }
jdict = { "content": "hello world", "date": jdate }

print (json.dumps(jdict))




