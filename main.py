import sys
from os import system
from os.path import isfile
from time import sleep
red = '\033[1;31m'


print(" ")
print(" ")
sleep(2)

FILE = "face_cracker.py"
def protect():

    if not isfile(FILE):
        print(f'{red}[!] Somethings Error...!')
        sleep(2)
        sys.exit()

def is_banner():
    try:
        from face_cracker import Banner, banner
    except ImportError as f:
        print(" ")
        print(f'{red}[!] Somthings Error')
        sys.exit()
if __name__ == "__main__":
    protect()
    is_banner()

