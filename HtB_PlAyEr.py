import requests
from bs4 import BeautifulSoup
from selenium import webdriver



def Cli():
    print("hi")

def BrowserAutomation():
    PlayerMail="votake6916@zevars.com"
    PlayerPass="HtB0PlAyEr"

    Id_mail_in="email"
    Id_password_in="password"

    browser=webdriver.Firefox()
    browser.get("https://www.hackthebox.eu/login")

    idget1=browser.find_element_by_id(Id_mail_in)
    idget1.send_keys(PlayerMail)
    idget2=browser.find_element_by_id(Id_password_in)
    idget2.send_keys(PlayerPass)
    btn_name="pull-right"
    login_btn=browser.find_element_by_class_name(btn_name)
    login_btn.click()


BrowserAutomation()
