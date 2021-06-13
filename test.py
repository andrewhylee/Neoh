from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

import time
import os

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# # To print Console.log Messages
# d = DesiredCapabilities.CHROME
# d['goog:loggingPrefs'] = { 'browser':'ALL' }
# # print messages
# for entry in browser.get_log('browser'):
#     print(entry)
# browser = webdriver.Chrome(executable_path='C:\\Users\\Andrew\\Documents\\automatic-enrollment-project\\chromedriver.exe',options=options, desired_capabilities=d)

url = 'https://fusion.geniussis.com/PublicWelcome.aspx'
browser = webdriver.Chrome(executable_path='C:\\Users\\Andrew\\Documents\\automatic-enrollment-project\\chromedriver.exe',options=options)
# browser = webdriver.Chrome(executable_path='/home/drew/automatic-enrollment-project/chromedriver.exe')
browser.get(url)

username = browser.find_element_by_id("ctl00_centerLoginContent_tbLogin")
password = browser.find_element_by_id("ctl00_centerLoginContent_tbPassword")

username.send_keys(os.getenv('username_mat'))
password.send_keys(os.getenv('pw_mat'))

browser.find_element_by_id("ctl00_centerLoginContent_btnSignMeIn").click()


browser.find_element_by_id("ctl00_ddChangeRole_chosen").click() # Roles Dropdown
browser.find_element_by_xpath('//*[@id="ctl00_ddChangeRole_chosen"]/div/ul/li[1]').click() # Super User Role
browser.get("https://fusion.geniussis.com/ActiveStudents.aspx") # Students Page
browser.find_element_by_link_text('Practice, Student').click() # Desired Student
browser.find_element_by_link_text('Enroll in Section').click() # Enroll in Section Page


browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_ddTerm_chosen"]/a/span').click()
browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_ddTerm_chosen"]/div/ul/li[2]').click()


time.sleep(1)
browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_tbCourse"]').click()
browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_tbCourse"]').send_keys("Algebra 1 A") # 
# time.sleep(2)
browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_tbCourse"]').send_keys("\ue015") # 
