from selenium import webdriver
import subprocess
from credential import credential
from credential import BruteforceInfo
import os
import colored
import pyautogui
import time
import re





red=colored.fg("red_1")
green=colored.fg("chartreuse_2a")
orange=colored.fg("orange_1")
yellow=colored.fg("yellow_1")
reset=colored.attr("reset")
def Intro():
    "Intro for htB_PlAyEr"
    print(red+'''
 _   _ _   ____     ____  _    _         _____
| | | | |_| __ )   |  _ \| |  / \  _   _| ____|_ __
| |_| | __|  _ \   | |_) | | / _ \| | | |  _| | '__|
|  _  | |_| |_) |  |  __/| |/ ___ \ |_| | |___| |
|_| |_|\__|____/___|_|   |_/_/   \_\__, |_____|_|
              |_____|              |___/            '''+green+'''V1.Dc to '''+orange+'''0xAjay('''+yellow+'''Tamilhackz'''+orange+''')'''+reset+'''''')




def FlagSubmitViaBrowser():
    ""
    Id_mail_in="email"
    Id_password_in="password"

    browser=webdriver.Firefox()
    browser.get("https://www.hackthebox.eu/login")

    idget1=browser.find_element_by_id(Id_mail_in)
    idget1.send_keys(credential.PlayerMail)
    idget2=browser.find_element_by_id(Id_password_in)
    idget2.send_keys(credential.PlayerPass)
    btn_name="pull-right"
    login_btn=browser.find_element_by_class_name(btn_name)
    login_btn.click()
    login_btn=browser.find_element_by_class_name("pull-left")
    login_btn.click()
    browser.get("https://www.hackthebox.eu/home/machines/profile/"+idd[0])
    time.sleep(5)
    pyautogui.hotkey('alt','tab')

def ActivatingOpenvpn():
    time.sleep(2)
    pyautogui.hotkey('ctrl','shift','t')
    pyautogui.typewrite("sudo -v",interval=0.2)
    pyautogui.press("enter")
    pyautogui.typewrite(credential.AdminPass,interval=0.1)
    pyautogui.press("enter")
    pyautogui.typewrite("sudo openvpn HtB0PlAyEr.ovpn ",interval=0.1)
    pyautogui.press("enter")
    time.sleep(4)
    pyautogui.hotkey('shift','left')
    time.sleep(5)
    # os.system("sudo xterm -hold -e 'openvpn HtB0PlAyEr.ovpn &' -S ")

def CheckingBoxesCli():
    os.system("htb list")
    # pyautogui.typewrite("sudo htb list",interval=0.1)
    # pyautogui.press('enter')
    # time.sleep(3)
    # pyautogui.typewrite(credential.AdminPass,interval=0.1)
    # pyautogui.press('enter')

def AccessingBoxes(boxname):
    "hi"
    os.system("htb info -a "+boxname)
    input("Press enter")
    for_ip=subprocess.check_output("htb info -a "+boxname+"|grep 10.10.10",shell=True)
    global ip
    ip=re.findall(r"10.10.10.* ",str(for_ip))
    for_id=subprocess.check_output("htb info -a "+boxname+"|grep 'id             │'",shell=True)
    global idd
    idd=re.findall(r"\d\d\d",str(for_id))


def IpChecking():
    "hi"
    global tun_ip
    tun_ip=str(subprocess.call('''echo "$(ip addr show tun0 | awk '/inet / {print $2}' | cut -d/ -f 1) " ''',shell=True))


def MakingDir(boxn):
    "hi"
    os.chdir("/home/"+credential.AdminDefaultUser+"/HTB")
    def CheckingDirExist():
        if os.path.exists(boxn)==True:
            return 1
        else:
            return 0
    if CheckingDirExist()==1:
        pass
    else:
        os.mkdir(boxn)
        os.chdir(boxn)
        os.system("pwd")

def Bruteforce(boxname):
    "hi"
    os.system("gobuster dir -u "+ip[0]+" -t "+BruteforceInfo.threads+" -e -w "+BruteforceInfo.wordlist+" -o ~/HTB/"+boxname+"/"+boxname+"Wordlist.txt")

def NmapScan(boxname):
    # get IP
    os.system('nmap '+str(ip[0])+' -oA normalscan')
    # seperating opened ports
    os.system("cat normalscan.nmap | grep open | awk -F/ '{print $1}' ORS=',' | rev | cut -c 2- | rev > opened-ports.txt")
    # opening ports file
    f=open("opened-ports.txt", "r")
    ports = f.read()
    print("\nOPENED PORTS:")
    print(ports)
    # scanning only the opened ports
    os.system('nmap -sC -sV '+ip[0]+' -p'+ports+' -oN '+boxname+'Nmap.txt')
    # deleting extra files ( I used -oN flag but it took more time than -oA. So, I used -oA and deleting the extra stuffs here )
    os.system('rm opened-ports.txt normalscan.gnmap normalscan.xml normalscan.nmap')

def FinishingTouch():
    os.system('figlet -f slant "Bella Ciao"')

Intro()
CheckingBoxesCli()
box_id=str(input("Enter the box name: "))
AccessingBoxes(box_id.capitalize())
ActivatingOpenvpn()
IpChecking()
MakingDir(box_id.capitalize())
Bruteforce(box_id.capitalize())
NmapScan(box_id.capitalize())
FlagSubmitViaBrowser()
FinishingTouch()


