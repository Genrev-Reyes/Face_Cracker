import sys
from os import system
from os.path import isfile

red = '\033[1;31m'



try:
    if isfile("face_crack.py"):
        pass
    else:
        sleep(1)
        print(f'{red}[!] Somethings Error')
except Exception as C:
    sys.exit()


