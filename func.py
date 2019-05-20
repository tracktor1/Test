import os
import socket


# apt install function
def install_apt(pkg_name):
    aptget = 'sudo apt-get ' + pkg_name
    os.system(aptget)


# Rename machine
def host_ren(h_name):
    gethost = socket.gethostname()
    if gethost != h_name:
        print("hostname is: ", gethost)
        print("New host will be: ", h_name)
        hname = 'sudo hostnamectl set-hostname ' + h_name
        os.system(hname)
    else:
        print ("Rename is not needed")

