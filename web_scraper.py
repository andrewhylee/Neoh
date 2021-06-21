import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import time
import os

def log_in(browser):
    username = browser.find_element_by_id("UserName")
    password = browser.find_element_by_id("Password")

    username.send_keys(os.getenv('username_mat'))
    password.send_keys(os.getenv('pw_mat'))

    browser.find_element_by_xpath("/html/body/div/div/div/div/section/form/button").click()
    browser.find_element_by_xpath("/html/body/nav/div/ul/li[2]/a").click()

def go_to_campus_schedule(browser):
    try: 
        campusSched = WebDriverWait(browser, 8).until(
            EC.presence_of_element_located( (By.CSS_SELECTOR , '#app > div > div:nth-child(2) > div > div.one-col-page-layout.no-print > div.accordion.panel-group > div:nth-child(2) > div.panel-heading > div > a') )
        )
        campusSched.click()
    finally:
        pass

def go_to_next_weeks_scheudele(browser):
    try: 
        nextbtn = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located( (By.XPATH , '/html/body/div/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div/a[2]') )
        )
        nextbtn.click()
    finally:
        pass

def get_all_teachers(browser, number_of_teachers):
    # -- GO TO TEACHERS --
    try: 
        teachers = WebDriverWait(browser, 8).until(
            EC.presence_of_element_located( (By.XPATH , '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/div/button') )
        )
        teachers.click()
    finally:
        pass

    # -- GET ALL TEACHERS --
    time.sleep(3)
    for i in range(1, number_of_teachers):
        teach = browser.find_element_by_xpath(f'//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/div/div/ul/li[{i}]/div/label')
        teach.click()
        time.sleep(3)


def get_a_specific_student(browser, specific_student):
    # -- GO TO SPECIFIC STUDENT --
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/div[2]/div/button').click()
    browser.find_element_by_xpath(f'//*[contains(text(), "{specific_student}")]').click()


def main():
    number_of_teachers = 65 # actually 59
    specific_student = ""

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--auto-open-devtools-for-tabs")

    url = 'https://matrix.fusionacademy.com/'
    br = webdriver.Chrome(executable_path='C:\\Users\\Andrew\\Documents\\automatic-enrollment-project\\chromedriver.exe',options=options)
    br.get(url)

    log_in(br)
    go_to_campus_schedule(br)
    go_to_next_weeks_scheudele(br)
    
    if specific_student != "":
        get_a_specific_student(br, specific_student)
    else:
        get_all_teachers(br, number_of_teachers)


if __name__ == "__main__":
    main()