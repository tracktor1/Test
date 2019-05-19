

import os

newhost = 'host1'


def host_ren(h_name):
    hname = 'sudo hostnamectl set-hostname ' + h_name
    os.system(hname)

host_ren(newhost)