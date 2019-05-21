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

###Set the relative file location to the script location
def relative_path(file_name):
    script_path = os.path.abspath(os.path.dirname(__file__))
    joint_path = os.path.join(script_path, file_name)
    return joint_path