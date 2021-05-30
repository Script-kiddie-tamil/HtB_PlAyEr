from selenium import webdriver
import subprocess
from credential import credential
from credential import BruteforceInfo
import os
import colored
import pyautogui
import time
import re




# def ColoredVariables():
#     "ColoredVariables() function is used to Adding colors to the text ,I'm Functional Loving programmer Thus only I'm creating this function"

red=colored.fg("red_1")
green=colored.fg("chartreuse_2a")
orange=colored.fg("orange_1")
yellow=colored.fg("yellow_1")
reset=colored.attr("reset")

def Intro():
    "Intro for htB_PlAyEr,And some Kind of Adayalam"
    print(red+'''
 _   _ _   ____     ____  _    _         _____
| | | | |_| __ )   |  _ \| |  / \  _   _| ____|_ __
| |_| | __|  _ \   | |_) | | / _ \| | | |  _| | '__|
|  _  | |_| |_) |  |  __/| |/ ___ \ |_| | |___| |
|_| |_|\__|____/___|_|   |_/_/   \_\__, |_____|_|
              |_____|              |___/            '''+green+'''V1.Dc to '''+orange+'''0xAjay('''+yellow+'''Tamilhackz'''+orange+''')'''+reset)

def FlagSubmitViaBrowser():
    "FlagSubmitViaBrowser function is  used to Sumbit the flag via"

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
    "ActivatingOpenvpn() function is used to Activate The Player OpenVpn"

    time.sleep(2)
    pyautogui.hotkey('ctrl','shift','t')
    pyautogui.typewrite("sudo -v",interval=0.2)
    pyautogui.press("enter")
    pyautogui.typewrite(credential.AdminPass,interval=0.1)
    pyautogui.press("enter")
    pyautogui.typewrite("sudo openvpn ~/HTB/HtB0PlAyEr.ovpn ",interval=0.1)
    pyautogui.press("enter")
    time.sleep(4)
    pyautogui.hotkey('shift','left')
    time.sleep(7)
    # os.system("sudo xterm -hold -e 'openvpn HtB0PlAyEr.ovpn &' -S ")

def CheckingBoxesCli():
    "CheckingBoxesCli() function is used to Check The Live Boxes Via CommandLine "

    os.system("htb list")
    # pyautogui.typewrite("sudo htb list",interval=0.1)
    # pyautogui.press('enter')
    # time.sleep(3)
    # pyautogui.typewrite(credential.AdminPass,interval=0.1)
    # pyautogui.press('enter')

def AccessingBoxes(boxname):
    "AccessingBoxes() function is used to Access the Player wanted Box Via Cli With Detail Info"

    os.system("htb info -a "+boxname)
    # input("Press enter")
    for_ip=subprocess.check_output("htb info -a "+boxname+"|grep 10.10.10",shell=True)
    global ip
    ip_with=re.findall(r"10.10.10.* ",str(for_ip))
    ip_withoo=str(ip_with[0])
    ip=ip_withoo.strip()
    for_id=subprocess.check_output("htb info -a "+boxname+"|grep 'id             │'",shell=True)
    global idd
    idd=re.findall(r"\d\d\d",str(for_id))

def IpChecking():
    "IpChecking() function is used to Check the Tunel Ip"

    global tun_ip
    tun_ip=str(subprocess.call('''echo "$(ip addr show tun0 | awk '/inet / {print $2}' | cut -d/ -f 1) " ''',shell=True))

def MakingDir(boxn):
    "MakingDir() function is used to creating a specific Directory For the box ,It makes a setup like Backup For YouTube "

    os.chdir("/home/"+credential.AdminDefaultUser+"/HTB")
    def CheckingDirExist():
        if os.path.exists(boxn)==True:
            return 1
        else:
            return 0
    if CheckingDirExist()==1:
        os.chdir(boxn)
        os.system("pwd")
    else:
        os.mkdir(boxn)
        os.chdir(boxn)
        os.system("pwd")

def Bruteforce(boxname):
    "Bruteforce() function is used to Bruteforce the Box on 80 port "

    os.system("gobuster dir -u "+ip+":"+port+" -t "+BruteforceInfo.threads+" -e -w "+BruteforceInfo.wordlist+" -o ~/HTB/"+boxname+"/"+boxname+"Wordlist.txt")

def NmapScan(boxname):
    "NmapScan() function is used to Scan the Box for version of the port runing And this code was @JoPraveen's HTBScan with Little Customization"
    # get IP
    os.system('nmap '+str(ip)+' -oA normalscan')
    # seperating opened ports
    os.system("cat normalscan.nmap | grep open | awk -F/ '{print $1}' ORS=',' | rev | cut -c 2- | rev > opened-ports.txt")
    # opening ports file
    f=open("opened-ports.txt", "r")
    ports = f.read()
    print("\nOPENED PORTS:")
    print(ports)
    os.system('rm normalscan.gnmap normalscan.xml normalscan.nmap')
    # scanning only the opened ports
    os.system('nmap -sC -sV '+ip+' -oA '+boxname+'Nmap'+' -p'+ports)
    # deleting extra files ( I used -oN flag but it took more time than -oA. So, I used -oA and deleting the extra stuffs here )
    os.system('rm opened-ports.txt '+boxname+'Nmap.gnmap '+boxname+'Nmap.xml ')

def OpeningBoxIpOnBrowser():
    browser=webdriver.Firefox()
    browser.get('http://'+ip+':'+port)
    pyautogui.hotkey('ctrl','shift','c')
    time.sleep(2)
    pyautogui.hotkey('alt','tab')


# def CatBruteForceResult():
#     "hi"
#     # f = open(box_id.capitalize()+"Wordlist.txt", "r")
#     # print(f.read())
#     os.system("cat "+box_id.capitalize()+"Wordlist.txt")
# def CatNmapResult():
#     "hi"
#     # f = open(box_id.capitalize()+"Nmap.Nmap", "r")
#     # print(f.read())
#     os.system("cat "+box_id.capitalize()+"Nmap.Nmap")

def FinishingTouch():
    "FinishingTouch Holds oveerall Information "
    os.system('clear')
    os.system('figlet -f slant "Bella Ciao"')
    os.system("htb info -a "+box_id)
    print(yellow+'''SomeInfo:'''+reset+'''

         BoxName          : '''+orange+box_id.capitalize()+reset+'''

         Box Ip           : '''+red+ip+reset+'''

         OpenVpn Status   : '''+green+'''Connected'''+reset+'''

         OpenVpn          : '''+red+tun_ip[0]+reset+'''

         BruteForceResult : 
                            ===============================================================
                            Gobuster v3.0.1
                            ===============================================================
                            [+] Url:            http://'''+str(ip)+''':'''+port+'''
                            [+] Threads:        '''+str(BruteforceInfo.threads)+'''
                            [+] Wordlist:       '''+str(BruteforceInfo.wordlist)+'''
                            [+] Status codes:   200,204,301,302,307,401,403
                            [+] User Agent:     gobuster/3.0.1
                            [+] Expanded:       true
                            [+] Timeout:        Not Mentioned
                            ===============================================================
                            Starting gobuster
                            ===============================================================
    ''')
    f = open(box_id.capitalize()+"Wordlist.txt", "r")
    file=str(f.read())
    print(str("                            ")+file)

    print('''

         Nmap Result      : ''')

    f1 = open(box_id.capitalize()+"Nmap.nmap", "r")
    filen=str(f1.read())
    print(str("                            ")+filen)
        # print(str("                            ")+f.read())
    print(str('''

         Browser Status   : ''')+green+'''ON'''+reset)

# ColoredVariables()
Intro()
CheckingBoxesCli()
global box_id
box_id=str(input("Enter the box name: "))
AccessingBoxes(box_id.capitalize())
ActivatingOpenvpn()
IpChecking()
MakingDir(box_id.capitalize())
NmapScan(box_id.capitalize())
global port
port=str(input("Enter The Http port Number: "))
OpeningBoxIpOnBrowser()
Bruteforce(box_id.capitalize())
FlagSubmitViaBrowser()
FinishingTouch()



# print(type(box_id.capitalize()))
# print(type(CatBruteForceResult()))
# print(type(yellow))

# hi=str(os.system("cat "+box_id.capitalize()+"Nmap.nmap"))