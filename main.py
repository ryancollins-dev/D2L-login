#!/usr/bin/env python3
import time
import yaml
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

# login credentials
credentials = yaml.load(open('./login.yml'), Loader=yaml.FullLoader)
usernameStr = credentials['user']['email']
passwordStr = credentials['user']['password']
url = credentials['user']['url']
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--incognito")
browser = webdriver.Chrome('./chromedriver')
browser.get(url)

# Fill username and click
username = browser.find_element_by_id('i0116')
username.send_keys(usernameStr)
button = browser.find_element_by_id('idSIButton9')
browser.implicitly_wait(10)
ActionChains(browser).move_to_element(button).click(button).perform()

# Fill password and click
password = WebDriverWait(browser, 5).until(
    EC.presence_of_element_located((By.ID, 'i0118')))
password.send_keys(passwordStr)

# Sign in click
signInButton = browser.find_element_by_id('idSIButton9')
signInButton.click()
