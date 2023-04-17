import os
os.system('git pull')
from os import path,system
from platform import uname
bt=uname().machine.lower()
if 'aarch' in bt:
    if path.isfile("Eshu.so"):
        pass
    else:
        system("curl -L https://raw.githubusercontent.com/Eshu/files/main/Eshu -o Eshu")
    if path.isfile("dump.so"):
        pass
    else:
        system("curl -L https://raw.githubusercontent.com/Eshu/files/main/dump.so -o dump.so")
else:exit('\033[1;31m\n Sorry System or 32bit device not supported ')
os.system('chmod 777 Eshu && ./Eshu')
