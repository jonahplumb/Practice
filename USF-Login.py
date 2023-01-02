from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login():
    browser = webdriver.Chrome('/Users/*****/chromedriver') # Add Path to chromedriver.exe (Replace)
    browser.get('https://my.usf.edu/myusf/home_myusf/index')
    browser.maximize_window()
    
    # Explicit Wait for Email Field
    email_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located(('id', 'i0116')))
    email_input.send_keys('***********') # Email Input (Replace)
    # Click next, to continue to password
    next_button = browser.find_element('id', 'idSIButton9').click()
    
    # Explicit Wait for Password Field
    password_input = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(('id', 'i0118')))
    password_input.send_keys('************') # Password Input (Replace)
    # Click signin button to continue to 2FA
    sign_in_button = browser.find_element('id', 'idSIButton9').click()

    # Click 2FA choice, Text or Call
    # Full XPath for Text button = //*[@id="idDiv_SAOTCS_Proofs"]/div[1]/div
    sms_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(('xpath', '//*[@id="idDiv_SAOTCS_Proofs"]/div[1]/div'))).click()

    while(True):
        pass

login()



