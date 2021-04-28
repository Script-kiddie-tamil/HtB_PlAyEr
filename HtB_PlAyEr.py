import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import subprocess
from credential import credential
import getpass
import os
import colored
import pyautogui
import sys
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




def BrowserAutomation():
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
    login_btn.press()
    login_btn=browser.find_element_by_class_name("pull-left")
    login_btn.click()
    browser.get("https://www.hackthebox.eu/home/machines")
    machin_name=browser.find_element_by_class_name("machine-effect")
    # for mach in machin_name:
    title=machin_name.find_element_by_xpath("/html/body/div[2]/section/div[2]/div[4]/div/div[3]/div/div[3]/div[3]/div[2]")
    print(title)

def ActivatingOpenvpn():
    pyautogui.typewrite("sudo -v",interval=0.1)
    pyautogui.press("enter")
    pyautogui.typewrite(credential.AdminPass,interval=0.1)
    pyautogui.press("enter")
    pyautogui.typewrite("sudo xterm -hold -e 'openvpn HtB0PlAyEr.ovpn' &",interval=0.1)
    pyautogui.press("enter")
    pyautogui.hotkey('alt','tab')
    time.sleep(5)
    pyautogui.hotkey('alt','tab')
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
    for_ip=subprocess.check_output("htb info -a "+boxname+"|grep 10.10.10",shell=True)
    global ip
    ip=re.findall(r"10.10.10.* ",str(for_ip))



def IpChecking():
    "hi"
    tun_ip=subprocess.call("$(ip addr show tun0 | awk '/inet / {print $2}' | cut -d/ -f 1)",shell=True)


def MakingDir():
    "hi"

def NmapScan():
        # get IP
        os.system('nmap '+ip+' -oA normalscan')
        # seperating opened ports
        os.system("cat normalscan.nmap | grep open | awk -F/ '{print $1}' ORS=',' | rev | cut -c 2- | rev > opened-ports.txt")
        # opening ports file
        f=open("opened-ports.txt", "r")
        ports = f.read()
        print("\nOPENED PORTS:")
        print(ports)
        # scanning only the opened ports
        os.system('nmap -sC -sV '+ip+' -p'+ports)
        # deleting extra files ( I used -oN flag but it took more time than -oA. So, I used -oA and deleting the extra stuffs here )
        os.system('rm opened-ports.txt normalscan.gnmap normalscan.xml normalscan.nmap')



Intro()
ActivatingOpenvpn()

BrowserAutomation()
NmapScan()
# CheckingBoxesCli()
# box_id=str(input("Enter the box name: "))
# AccessingBoxes(box_id)
# IpChecking()