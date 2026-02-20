import unittest
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


def delay():
    time.sleep(random.randint(1,5))

# This function how to get inside the shadow DOM. Can be moved to helpers.
def get_shadow(driver, element):
    return driver.execute_script("return arguments[0].shadowRoot", element)


class ChromePorscheTests(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'eager'
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--window-size=1920,1080")
        #options.add_argument("--headless")

        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()

    # This test is just closing banner "Accept cookies" though accessibility

    def test_TC_P_01(self):
        driver = self.driver
        driver.get("https://www.porsche.com/usa/")
        time.sleep(3)
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        time.sleep(3)

        # Finding the button Menu and click

        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root
        models = shadow.find_element(By.CSS_SELECTOR, "phn-p-button-pure")
        driver.execute_script("arguments[0].click();", models)
        time.sleep(5)

        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root
        shopping_tools = shadow.find_element(By.CSS_SELECTOR, "phn-p-button-pure[class='sc-phn-nd-side-drawer-item hydrated'][data-id='vehicle_purchase']")
        driver.execute_script("arguments[0].click();", shopping_tools)
        time.sleep(5)

        driver.quit()

    def test_TC_P_02(self):
        driver = self.driver
        driver.get("https://www.porsche.com/usa/")
        time.sleep(3)
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        time.sleep(3)

        # Finding the button Menu and click

        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root
        models = shadow.find_element(By.CSS_SELECTOR, "phn-p-button-pure")
        driver.execute_script("arguments[0].click();", models)
        time.sleep(3)

        # Finding the button Shopping Tools and click

        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root
        shopping_tools = shadow.find_element(By.CSS_SELECTOR, "phn-p-button-pure[class='sc-phn-nd-side-drawer-item hydrated'][data-id='vehicle_purchase']")
        driver.execute_script("arguments[0].click();", shopping_tools)
        time.sleep(3)

        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root
        build_your_own = shadow.find_element(By.CSS_SELECTOR,"a[class='pure-link sc-phn-nd-menu-item'][data-id='vehicle_purchase/mainmenu.vehiclepurchase.configure']")
        driver.execute_script("arguments[0].click();", build_your_own)
        time.sleep(3)

        driver.quit()

