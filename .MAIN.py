from requests import head as Connect
import sys
from time import sleep
red = '\033[0;31m'
green = '\033[0;32m'
yellow = '\033[1;33m'
try:
    Connect("http://google.com")
    if Connect:
        print(f'{yellow}[-] Connection Status: {green}Online')
        sleep(2)
        print(" ")
        sys.exit()
except ConnectionError:
    print(f'{red}[!] No Internet')
    sys.exit()

