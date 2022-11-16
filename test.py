from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://learn.upes.ac.in/?new_loc=%2Fultra%2Fcourse")
print(driver.title)

username = "500082592"
password = "##########"

# Agrees to cookies
driver.find_element("id", "agree_button").click()

# Inputs username and password
uname = driver.find_element("id", "user_id") 
uname.send_keys(username)

pword = driver.find_element("id", "password") 
pword.send_keys(password)

# Submits the entries
driver.find_element("id", "entry-login").click()

# Wait for login process to complete. 
WebDriverWait(driver=driver, timeout=10).until(lambda x: x.execute_script("return document.readyState === 'complete'"))

# Verify that the login was successful.
error_message = "Incorrect username or password."

# Retrieve any errors found. 
errors = driver.find_elements(By.CLASS_NAME, "flash-error")

# When errors are found, the login will fail. 
if any(error_message in e.text for e in errors): 
    print("[!] Login failed")
else:
    print("[+] Login successful")

driver.quit()