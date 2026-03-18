import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random

def delay():
    time.sleep(random.randint(3,4))

def Porsche_link_MainPage(driver):
    driver.get("https://www.porsche.com/")
    time.sleep(4)

def Porsche_link_CayenneCoupe(driver):
    driver.get("https://www.porsche.com/usa/models/cayenne/cayenne-coupe-models/cayenne-coupe/")
    time.sleep(4)

def captcha(driver):
    actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
    driver.switch_to.active_element.send_keys(actions)
    time.sleep(3)

def burger_menu(driver):
    header = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
    delay()
    shadow = header.shadow_root
    delay()
    burger = shadow.find_element(By.CSS_SELECTOR, ".phn-burger-button.sc-phn-burger-button.hydrated")
    driver.execute_script("arguments[0].click();", burger)
    time.sleep(4)

def account_menu(driver):
    host = driver.find_element(By.CSS_SELECTOR, "phn-header")
    delay()
    shadow = host.shadow_root
    delay()
    account_button = shadow.find_element(By.CSS_SELECTOR,
                                         "phn-p-button-pure[data-id='account-contextual-button'][data-test-id='account-button']")
    driver.execute_script("arguments[0].click();", account_button)
    time.sleep(2)

def login_button(driver):
    host = driver.find_element(By.CSS_SELECTOR, "phn-header")
    delay()
    shadow = host.shadow_root
    delay()
    host2 = shadow.find_element(By.CSS_SELECTOR, "phn-p-button")
    shadow2 = host2.shadow_root
    delay()
    log_in_button = shadow2.find_element(By.CSS_SELECTOR, "button[class='root'][type='submit']")
    driver.execute_script("arguments[0].click();", log_in_button)
    time.sleep(2)

