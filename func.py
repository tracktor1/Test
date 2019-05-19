import os



# apt install function
def install_apt(pkg_name):
    aptget = 'sudo apt-get ' + pkg_name
    os.system(aptget)