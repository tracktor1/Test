#!/usr/bin/env python
"""
    Please note: this script works with python 3 only
    All backup are saved in the users home dir under backup dir:
        /home/username/backup/device_serial
    run it as:
        python3 ./1.py
"""


import os
import socket
from func import *

if os.geteuid()==0:
  print ("Running as root.")
else:
  print ("User is not root.")

nodeinstall = 'node'
docinstall = 'docker'


gethost = socket.gethostname()
print(gethost)

#install_apt('update')

