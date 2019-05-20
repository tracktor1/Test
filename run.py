#!/usr/bin/env python

import os
from func import *


apt_update = 'update'   # update repository

newhostname = 'host2'   # New hostname

#rename host
host_ren(newhostname)


# run apt-get update
print ("Updating apt...")
install_apt(apt_update)

