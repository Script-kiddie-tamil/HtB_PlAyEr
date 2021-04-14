import requests
from bs4 import BeautifulSoup
from selenium import webdriver

PlayerMail="karthikrajaofficial143@gmail.com"
PlayerPass="KARTHIK raja 143"

driver=webdriver.Firefox()
driver.get("https://www.hackthebox.eu/login")

Id_mail_in="loginEmail"
Id_password_in="loginPassword"

