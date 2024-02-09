from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

usernameStr = 'student'
passwordStr = 'Password123'

browser = webdriver.Chrome()
browser.get((r"https://practicetestautomation.com/practice-test-login/"))

# search for the presence of username field and then send the username
username = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.ID, 'username')))
username.send_keys(usernameStr)

# search for the presence of password field and then send the password
password = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.ID, 'password')))
password.send_keys(passwordStr)

# search for the persence of the submit button and then click it
signInButton = WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.ID,'submit')))
signInButton.click()

# this is for keeping the browser open for longer 
time.sleep(5)
browser.quit()