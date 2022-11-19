from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

driver.get("https://learn.upes.ac.in/ultra/calendar")
print(driver.title)

# Logs in to the account
def login():
    username = "500082592"
    password = "brihad1692"

    # Agrees to cookies
    driver.find_element("id", "agree_button").click()

    # Inputs username and password
    uname = driver.find_element("id", "user_id") 
    uname.send_keys(username)

    pword = driver.find_element("id", "password") 
    pword.send_keys(password)

    # Submits the entries
    driver.find_element("id", "entry-login").click()

login()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "bb-calendar1-month")))
time.sleep(2)
driver.find_element("id", "bb-calendar1-month").click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "bb-calendar1-deadline")))
time.sleep(2)
driver.find_element("id", "bb-calendar1-deadline").click()
time.sleep(10)

driver.quit()