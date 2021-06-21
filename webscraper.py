from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import time
import os

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

d = DesiredCapabilities.CHROME
d['goog:loggingPrefs'] = { 'browser':'ALL' }

url = 'https://matrix.fusionacademy.com/'
browser = webdriver.Chrome(executable_path='C:\\Users\\Andrew\\Documents\\automatic-enrollment-project\\chromedriver.exe',options=options, desired_capabilities=d)
# browser = webdriver.Chrome(executable_path='/home/drew/automatic-enrollment-project/chromedriver.exe')
browser.get(url)

username = browser.find_element_by_id("UserName")
password = browser.find_element_by_id("Password")

username.send_keys(os.getenv('username_mat'))
password.send_keys(os.getenv('pw_mat'))

browser.find_element_by_xpath("/html/body/div/div/div/div/section/form/button").click()
browser.find_element_by_xpath("/html/body/nav/div/ul/li[2]/a").click()

# time.sleep(5)
# browser.find_element_by_css_selector("#app > div > div:nth-child(2) > div > div.one-col-page-layout.no-print > div.accordion.panel-group > div:nth-child(2) > div.panel-heading > div > a").click()

# -- GO TO CAMPUS SCHEDULE --
try: 
    campusSched = WebDriverWait(browser, 8).until(
        EC.presence_of_element_located( (By.CSS_SELECTOR , '#app > div > div:nth-child(2) > div > div.one-col-page-layout.no-print > div.accordion.panel-group > div:nth-child(2) > div.panel-heading > div > a') )
    )
    campusSched.click()
finally:
    pass

# # -- GO TO NEXT WEEK (NOW SPRING BREAK) --
# try: 
#     nextbtn = WebDriverWait(browser, 10).until(
#         EC.presence_of_element_located( (By.XPATH , '/html/body/div/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div/a[2]') )
#     )
#     nextbtn.click()
# finally:
#     pass

# -- GO TO TEACHERS --
try: 
    teachers = WebDriverWait(browser, 8).until(
        EC.presence_of_element_located( (By.XPATH , '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/div/button') )
    )
    teachers.click()
finally:
    pass

# ================================================
time.sleep(5)
for i in range(1, 65):
    teach = browser.find_element_by_xpath(f'//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/div/div/ul/li[{i}]/div/label')
    teach.click()
    time.sleep(3)

