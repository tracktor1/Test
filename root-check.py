
import os

#Check if root
if os.geteuid()==0:
  print ("Running as root.")
else:
  print ("User is not root.")