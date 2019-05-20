#!/usr/bin/env python

import os
from func import *


apt_update = 'update'   # update repository
apt_nodejs = 'nodejs'
newhostname = 'host2'   # New hostname

#rename host
host_ren(newhostname)

# Add nodejs repo
os.system('curl -sL https://deb.nodesource.com/setup_9.x | sudo -E bash -')

# Install nodeJS
install_apt(apt_nodejs)

# run apt-get update
#print ("Updating apt...")
#install_apt(apt_update)

