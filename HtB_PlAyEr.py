import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import subprocess
from credential import credential
import getpass
import os
import colored
import pyautogui

red=colored.fg("red_1")
green=colored.fg("chartreuse_2a")
orange=colored.fg("orange_1")
yellow=colored.fg("yellow_1")
reset=colored.attr("reset")
def Intro():
    print(red+'''
 _   _ _   ____     ____  _    _         _____
| | | | |_| __ )   |  _ \| |  / \  _   _| ____|_ __
| |_| | __|  _ \   | |_) | | / _ \| | | |  _| | '__|
|  _  | |_| |_) |  |  __/| |/ ___ \ |_| | |___| |
|_| |_|\__|____/___|_|   |_/_/   \_\__, |_____|_|
              |_____|              |___/            '''+green+'''V1.Dc to '''+orange+'''0xAjay('''+yellow+'''Tamilhackz'''+orange+''')'''+reset+'''''')




def BrowserAutomation():

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

def ActivatingOpenvpn():
    # subprocess.call(["xterm","-hold","-e","openvpn","HtB0PlAyEr.ovpn"])
    os.system("xterm -hold -e 'openvpn HtB0PlAyEr.ovpn' &")
def IpChecking():
    "hi"



if os.geteuid() != 0:
    exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")
else:
    Intro()
    ActivatingOpenvpn()