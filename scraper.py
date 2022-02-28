from DBconnect.credentials import Linkedin
import pandas as pd 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from beauty import beautifer
from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = True

def linkedin_api():
    browser = webdriver.Chrome(options=options,executable_path="chromedriver.exe")
    browser.get("https://www.linkedin.com/")
    browser.maximize_window()

    try:
        username = browser.find_element_by_id("session_key")
    except:
        signin_button = browser.find_element_by_class_name("nav__button-secondary")
        signin_button.click()
        username = browser.find_element_by_id("username")
        
    # try:  
    #     username = browser.find_element_by_id("session_key")
    # except:  
    #     username = browser.find_element_by_id("session_key")

    username.send_keys(Linkedin['Username'])
    try:
        password = browser.find_element_by_id("session_password")
    except:
        password = browser.find_element_by_id("password")

    password.send_keys(Linkedin['Pass'])

    try:
        login_button = browser.find_element_by_class_name("sign-in-form__submit-button")
    except:
        login_button = browser.find_element_by_class_name("login__form_action_container")
        print(login_button)

    login_button.click()

    browser.get("https://www.linkedin.com/jobs/search/")

    page = browser.page_source
    with open('test.html', 'w') as test_file:
        page = bytes(page, 'utf-8')
        test_file.write(str(page))

    browser.close()
    
    data = beautifer()

    return data


