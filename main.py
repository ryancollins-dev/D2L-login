# Program: D2L Login
# Author: Ryan
# Original creation date: 2021-08-19
# Version: Update
# Updated: 10-14-2021

import yaml
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

# login credentials
credentials = yaml.load(open('./login.yml'), Loader=yaml.FullLoader)
usernameStr = credentials['user']['email']
passwordStr = credentials['user']['password']
url = credentials['user']['url']
url2 = credentials['user']['url2']
# Incognito mode add following argument
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--incognito")
browser = webdriver.Chrome('./chromedriver')
browser.get(url)
emailfield = (By.ID, "i0116")
passwordfield = (By.ID, "i0118")
nextbutton = (By.ID, "idSIButton9")
no = (By.ID, "idBtn_Back")
# Fill username and click
WebDriverWait(browser, 10).until(ec.element_to_be_clickable(emailfield)).send_keys(usernameStr)
WebDriverWait(browser, 10).until(ec.element_to_be_clickable(nextbutton)).click()
# Fill password
WebDriverWait(browser, 10).until(ec.element_to_be_clickable(passwordfield)).send_keys(passwordStr)
# Sign in click
WebDriverWait(browser, 10).until(ec.element_to_be_clickable(nextbutton)).click()
# Click NO
WebDriverWait(browser, 10).until(ec.element_to_be_clickable(no)).click()
# Open Teams Meeting
webbrowser.open(url2)
