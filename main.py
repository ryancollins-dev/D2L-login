# Program: D2L Login
# Author: Ryan
# Original creation date: 2021-08-19
# Version: Final
# Updated: 2021-08-19

#!/usr/bin/env python3
import time
import yaml
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

emailfield = (By.ID, "i0116")
passwordfield = (By.ID, "i0118")
nextbutton = (By.ID, "idSIButton9")
no = (By.ID, "idBtn_Back")

# login credentials
credentials = yaml.load(open('./login.yml'), Loader=yaml.FullLoader)
usernameStr = credentials['user']['email']
passwordStr = credentials['user']['password']
url = credentials['user']['url']

# Incognito mode add following argument
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--incognito")
browser = webdriver.Chrome('./chromedriver')
browser.get(url)

# Fill username and click
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(emailfield)).send_keys(usernameStr)
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(nextbutton)).click()

# Fill password
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(passwordfield)).send_keys(passwordStr)

# Sign in click
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(nextbutton)).click()

# Click NO
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(no)).click()
