from selenium import webdriver
from credential import credential
import os

os.system("figlet 'Copy The API Key from HTB Web ,It is On the Last'")

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
browser.get("https://www.hackthebox.eu/home/settings")