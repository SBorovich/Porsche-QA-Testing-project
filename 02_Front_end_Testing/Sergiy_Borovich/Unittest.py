import unittest
import os
from datetime import datetime
import time
import random
#import AllureReports
import HtmlTestRunner
import Helpers as H
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.options import Options as Edge_Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as FirefoxService


def tearDown(self):
    self.driver.quit()

def delay():
    time.sleep(random.randint(1, 3))

# This function how to get inside the shadow DOM. Can be moved to helpers.
def get_shadow(driver, element):
    return driver.execute_script("return arguments[0].shadowRoot", element)

# ── Screenshot directory setup ────────────────────────────────────────────────
SCREENSHOT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def save_screenshot(driver, name: str) -> str:
    """Save a screenshot and return its path."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{name}_{timestamp}.png"
    path = os.path.join(SCREENSHOT_DIR, filename)
    driver.save_screenshot(path)
    print(f"  📸 Screenshot saved: {path}")
    return path

class ChromePorschePositiveTests(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'eager'
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--headless")

        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()

    def test_TC_P_36(self):
        driver = self.driver
        print("Positive TC-036")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the button Menu and click

        H.finding_menu_button(driver)
        delay()

        # Finding Shopping Tools button and click

        H.shopping_tools_button(driver)
        delay()

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Positive TC-036 PASS")

    def test_TC_P_37(self):
        driver = self.driver
        print("Positive TC-037")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the button Menu and click

        H.finding_menu_button(driver)
        delay()

        # Finding the button Shopping Tools and click

        H.shopping_tools_button(driver)
        delay()

        # Finding Build Your Own button and click

        H.build_your_own_button(driver)
        delay()

        # Check Build Your Own Url

        H.check_build_your_own_url(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Positive TC-037 PASS")

    def test_TC_P_38(self):
        driver = self.driver
        print("Positive TC-038")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the button Menu and click

        H.finding_menu_button(driver)
        delay()

        # Finding the button Shopping Tools and click

        H.shopping_tools_button(driver)
        delay()

        # Finding Compare Models button and click

        H.compare_models_button(driver)
        delay()

        # Check Compare Models Url

        H.check_compare_models_url(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Positive TC-038 PASS")

    def test_TC_P_39(self):
        driver = self.driver
        print("Positive TC-039")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the button Menu and click

        H.finding_menu_button(driver)
        delay()

        # Finding the button Shopping Tools and click

        H.shopping_tools_button(driver)
        delay()

        # Finding New & Used Inventory button and click

        H.new_and_used_button(driver)
        delay()

        # Check New & Used Inventory Url

        H.check_new_and_used_url(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Positive TC-039 PASS")

    def test_TC_P_40(self):
        driver = self.driver
        print("Positive TC-040")
        driver.get("https://www.porsche.com/usa/")
        time.sleep(3)
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the button Menu and click

        H.finding_menu_button(driver)
        delay()

        # Finding the button Shopping Tools and click

        H.shopping_tools_button(driver)
        delay()

        # Finding Current Vehicle Offers button and click

        H.current_vehicle_offers_button(driver)
        delay()

        # Check Current Vehicle Offers Url

        H.check_current_vehicle_offers_url(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Positive TC-040 PASS")

    def test_TC_P_41(self):
        driver = self.driver
        print("Positive TC-041")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the button Menu and click

        H.finding_menu_button(driver)
        delay()

        # Finding the button Shopping Tools and click

        H.shopping_tools_button(driver)
        delay()

        # Finding Certified Pre-Owned & Warranty button and click

        H.certified_button(driver)
        delay()

        # Check Certified Pre-Owned & Warranty Url

        H.check_certified_url(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Positive TC-041 PASS")

    def test_TC_P_42(self):
        driver = self.driver
        print("Positive TC-042")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the button Menu and click

        H.finding_menu_button(driver)
        delay()

        # Finding the button Shopping Tools and click

        H.shopping_tools_button(driver)
        delay()

        # Finding Porsche Financial Services button and click

        H.porsche_financial_button(driver)
        delay()

        # Check Porsche Financial Services Url

        H.check_porsche_financial_url(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Positive TC-042 PASS")

    def test_TC_P_43(self):
        driver = self.driver
        print("Positive TC-043")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the button Menu and click

        H.finding_menu_button(driver)
        delay()

        # Finding the button Shopping Tools and click

        H.shopping_tools_button(driver)
        delay()

        # Finding E-Mobility & E-Performance button and click

        H.e_mobility_button(driver)
        delay()

        # Check E-Mobility & E-Performance Url

        H.check_e_mobility_url(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Positive TC-043 PASS")

    def test_TC_P_44(self):
        driver = self.driver
        print("Positive TC-044")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the button Menu and click

        H.finding_menu_button(driver)
        delay()

        # Finding Account button and click

        H.account_button(driver)
        delay()

        # Finding Log In button and click

        H.log_in_button(driver)
        delay()

        # Check Log In Url

        H.check_log_in_url(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Positive TC-044 PASS")

    def test_TC_P_45(self):
        driver = self.driver
        print("Positive TC-045")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the button Menu and click

        H.finding_menu_button(driver)
        delay()

        # Finding Account button and click

        H.account_button(driver)
        delay()

        # Finding Saved Searches button and click

        H.saved_searches_button(driver)
        delay()

        # Check Saved Searches Url

        H.check_saved_searches_url(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Positive TC-045 PASS")

    def test_TC_P_46(self):
        driver = self.driver
        print("Positive TC-046")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the button Menu and click

        H.finding_menu_button(driver)
        delay()

        # Finding Account button and click

        H.account_button(driver)
        delay()

        # Finding Saved Cars button and click

        H.saved_cars_button(driver)
        delay()

        # Check Saved Cars Url

        H.check_saved_cars_url(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Positive TC-046 PASS")

    def test_TC_P_47(self):
        driver = self.driver
        print("Positive TC-047")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the button Menu and click

        H.finding_menu_button(driver)
        delay()

        # Finding Account button and click

        H.account_button(driver)
        delay()

        # Finding Find Connect Services button and click

        H.find_connect_services_button(driver)
        delay()

        # Check Find Connect Services Url

        H.check_find_connect_services_url(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Positive TC-047 PASS")

    def test_TC_P_48(self):
        driver = self.driver
        print("Positive TC-048")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the button Menu and click

        H.finding_menu_button(driver)
        delay()

        # Finding Account button and click

        H.account_button(driver)
        delay()

        # Finding Contact & Support button and click

        H.contact_and_support_button(driver)
        delay()
        actions = Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Contact & Support Url

        H.check_contact_and_support_url(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Positive TC-048 PASS")

class ChromePorscheNegativeTests(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'eager'
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--headless")

        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()

    def test_TC_N_36(self):
        driver = self.driver
        print("Negative TC-036")
        driver.get("https://www.porsche.com/usa/4")
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        print("Negative TC-036 PASS")

    def test_TC_N_37(self):
        driver = self.driver
        print("Negative TC-037")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding Menu button and click

        H.finding_menu_button(driver)
        delay()

        # Finding Find Your Porsche Center button and click

        H.find_your_porsche_center(driver)
        delay()

        # Finding Zip Code Search window click and input value "!@#$%^&*()_+"

        H.zip_code1(driver)
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Negative TC-036 PASS")

    def test_TC_N_38(self):
        driver = self.driver
        print("Negative TC-038")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the Menu button and click

        H.finding_menu_button(driver)
        delay()

        # Finding Find Your Porsche Center button and click

        H.find_your_porsche_center(driver)
        delay()

        # Finding Zip Code Search window click and input value "AsDFghjKL"

        H.zip_code2(driver)
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        #Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Negative TC-036 PASS")

    def test_TC_N_39(self):
        driver = self.driver
        print("Negative TC-039")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the Menu button and click

        H.finding_menu_button(driver)
        delay()

        # Finding Find Your Porsche Center button and click

        H.find_your_porsche_center(driver)
        delay()

        # Finding Zip Code Search window click and input value "123456789"

        H.zip_code3(driver)
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Negative TC-036 PASS")

    def test_TC_N_40(self):
        driver = self.driver
        print("Negative TC-040")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Scroll Down page

        career = driver.find_element(By.XPATH, "//pnav-footer[@class='pcom-main-footer hydrated']")
        driver.execute_script("arguments[0].scrollIntoView()", career)
        delay()

        # Finding Career button and click

        H.career_button(driver)
        delay()

        # Check Job Porsche Url

        H.check_job_porsche_url(driver)

        # Scroll Down page

        jobs = driver.find_element(By.XPATH, "//section[@id='pcom-Jobs-at-Porsche']")
        driver.execute_script("arguments[0].scrollIntoView()", jobs)
        delay()

        # Finding Search window, click and put value "!@#$%^&*()_+" for job search

        H.find_search_window1(driver)
        delay()
        actions = Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Switch to new tab

        driver.switch_to.window(driver.window_handles[-1])
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Get the title

        title = driver.title

        # Check the title
        if title == "Our vacancies | Career-Portal | Dr. Ing. h.c. F. Porsche AG":
            print("Title matches")
        else:
            print("Title does NOT match")

         # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

    def test_TC_N_41(self):
        driver = self.driver
        print("Negative TC-040")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Scroll Down page

        career = driver.find_element(By.XPATH, "//pnav-footer[@class='pcom-main-footer hydrated']")
        driver.execute_script("arguments[0].scrollIntoView()", career)
        delay()

        # Finding Career button and click

        H.career_button(driver)
        delay()

        # Check Job Porsche Url

        H.check_job_porsche_url(driver)

        # Scroll Down page

        jobs = driver.find_element(By.XPATH, "//section[@id='pcom-Jobs-at-Porsche']")
        driver.execute_script("arguments[0].scrollIntoView()", jobs)
        delay()

        # Finding Search window, click and put value "AsDFghjKL" for job search

        H.find_search_window2(driver)
        delay()
        actions = Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Switch to new tab

        driver.switch_to.window(driver.window_handles[-1])
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Get the title

        title = driver.title

        # Check the title
        if title == "Our vacancies | Career-Portal | Dr. Ing. h.c. F. Porsche AG":
            print("Title matches")
        else:
            print("Title does NOT match")

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

    def test_TC_N_42(self):
        driver = self.driver
        print("Negative TC-041")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Scroll Down page

        career = driver.find_element(By.XPATH, "//pnav-footer[@class='pcom-main-footer hydrated']")
        driver.execute_script("arguments[0].scrollIntoView()", career)
        delay()

        # Finding Career button and click

        H.career_button(driver)
        delay()

        # Check Job Porsche Url

        H.check_job_porsche_url(driver)

        # Scroll Down page

        jobs = driver.find_element(By.XPATH, "//section[@id='pcom-Jobs-at-Porsche']")
        driver.execute_script("arguments[0].scrollIntoView()", jobs)
        delay()

        # Finding Search window, click and put value "123456789" for job search

        H.find_search_window3(driver)
        delay()
        actions = Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Switch to new tab

        driver.switch_to.window(driver.window_handles[-1])
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Get the title

        title = driver.title

        # Check the title
        if title == "Our vacancies | Career-Portal | Dr. Ing. h.c. F. Porsche AG":
            print("Title matches")
        else:
            print("Title does NOT match")

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

    def test_TC_N_43(self):
        driver = self.driver
        print("Negative TC-042")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding Menu button and click

        H.finding_menu_button(driver)
        delay()

        # Finding Account button and click

        H.account_button(driver)
        delay()

        # Finding Contact & Support button and click

        H.contact_and_support_button(driver)
        delay()
        actions = Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Ask Porsche Url

        H.check_ask_porsche_url(driver)

        # Finding Search window, click and put value "!@#$%^&*()_+" for Question search

        H.find_ask_search_window1(driver)
        delay()
        actions = Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Result Ask Porsche Url

        H.check_result_ask_porsche_url1(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Negative TC-036 PASS")

    def test_TC_N_44(self):
        driver = self.driver
        print("Negative TC-043")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding Menu button and click

        H.finding_menu_button(driver)
        delay()

        # Finding Account button and click

        H.account_button(driver)
        delay()

        # Finding Contact & Support button and click

        H.contact_and_support_button(driver)
        delay()
        actions = Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Ask Porsche Url

        H.check_ask_porsche_url(driver)

        # Finding Search window, click and put value "AsDFghjKL" for Question search

        H.find_ask_search_window2(driver)
        delay()
        actions = Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Result Ask Porsche Url

        H.check_result_ask_porsche_url2(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Negative TC-036 PASS")

    def test_TC_N_45(self):
        driver = self.driver
        print("Negative TC-044")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding Menu button and click

        H.finding_menu_button(driver)
        delay()

        # Finding Account button and click

        H.account_button(driver)
        delay()

        # Finding Contact & Support button and click

        H.contact_and_support_button(driver)
        delay()
        actions = Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Ask Porsche Url

        H.check_ask_porsche_url(driver)

        # Finding Search window, click and put value "123456789" for Question search

        H.find_ask_search_window3(driver)
        delay()
        actions = Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Result Ask Porsche Url

        H.check_result_ask_porsche_url3(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Negative TC-036 PASS")

    def test_TC_N_46(self):
        driver = self.driver
        print("Negative TC-045")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding Menu button and click

        H.finding_menu_button(driver)
        delay()

        # Finding Account button and click

        H.account_button(driver)
        delay()

        # Finding Contact & Support button and click

        H.contact_and_support_button(driver)
        delay()
        actions = Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Ask Porsche Url

        H.check_ask_porsche_url(driver)

        # Scroll Down to  Owner Manual button

        manual = driver.find_element(By.XPATH, "//article[@id='help']")
        driver.execute_script("arguments[0].scrollIntoView()", manual)
        delay()

        # Finding Owner Manual button and click

        host = driver.find_element(By.CSS_SELECTOR, "p-link[class='hydrated']")
        shadow = host.shadow_root
        owner_manual = shadow.find_element(By.CSS_SELECTOR, ".root")
        driver.execute_script("arguments[0].click();", owner_manual)
        delay()

        # Switch to new tab

        driver.switch_to.window(driver.window_handles[-1])
        delay()

        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Finding Search window, click and put "A12345H6789QWE001" search

        H.find_vin_search_window_button1(driver)
        delay()
        actions = Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Negative TC-036 PASS")

    def test_TC_N_47(self):
        driver = self.driver
        print("Negative TC-046")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding Menu button and click

        H.finding_menu_button(driver)
        delay()

        # Finding Account button and click

        H.account_button(driver)
        delay()

        # Finding Contact & Support button and click

        H.contact_and_support_button(driver)
        delay()
        actions = Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Ask Porsche Url

        H.check_ask_porsche_url(driver)

        # Scroll Down to  Owner Manual button

        manual = driver.find_element(By.XPATH, "//article[@id='help']")
        driver.execute_script("arguments[0].scrollIntoView()", manual)
        delay()

        # Finding Owner Manual button and click

        host = driver.find_element(By.CSS_SELECTOR, "p-link[class='hydrated']")
        shadow = host.shadow_root
        owner_manual = shadow.find_element(By.CSS_SELECTOR, ".root")
        driver.execute_script("arguments[0].click();", owner_manual)
        delay()

        # Switch to new tab

        driver.switch_to.window(driver.window_handles[-1])
        delay()

        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Finding Search window, click and put "!@#$%^&*()_+{}-=+" search

        H.find_vin_search_window_button2(driver)
        delay()
        actions = Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Negative TC-036 PASS")

    def test_TC_N_48(self):
        driver = self.driver
        print("Negative TC-047")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding Menu button and click

        H.finding_menu_button(driver)
        delay()

        # Finding Account button and click

        H.account_button(driver)
        delay()

        # Finding Contact & Support button and click

        H.contact_and_support_button(driver)
        delay()
        actions = Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Ask Porsche Url

        H.check_ask_porsche_url(driver)

        # Scroll Down to  Owner Manual button

        manual = driver.find_element(By.XPATH, "//article[@id='help']")
        driver.execute_script("arguments[0].scrollIntoView()", manual)
        delay()

        # Finding Owner Manual button and click

        host = driver.find_element(By.CSS_SELECTOR, "p-link[class='hydrated']")
        shadow = host.shadow_root
        owner_manual = shadow.find_element(By.CSS_SELECTOR, ".root")
        driver.execute_script("arguments[0].click();", owner_manual)
        delay()

        # Switch to new tab

        driver.switch_to.window(driver.window_handles[-1])
        delay()

        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Finding Search window, click and put "12345678912345678" search

        H.find_vin_search_window_button3(driver)
        delay()
        actions = Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Negative TC-036 PASS")

class EdgePorschePositiveTests(unittest.TestCase):

    def setUp(self):
        os.environ["SE_DRIVER_MIRROR_URL"] = "https://msedgedriver.microsoft.com"
        options = Edge_Options()
        options.add_argument('--headless')
        options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = webdriver.Edge(options=options)
        self.driver.maximize_window()

    def test_TC_P_36(self):
        driver = self.driver
        print("Positive TC-036")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the button Menu and click

        H.finding_menu_button(driver)
        delay()

        # Finding Shopping Tools button and click

        H.shopping_tools_button(driver)
        delay()

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Positive TC-036 PASS")

    def test_TC_P_37(self):
        driver = self.driver
        print("Positive TC-037")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the button Menu and click

        H.finding_menu_button(driver)
        delay()

        # Finding the button Shopping Tools and click

        H.shopping_tools_button(driver)
        delay()

        # Finding Build Your Own button and click

        H.build_your_own_button(driver)
        delay()

        # Check Build Your Own Url

        H.check_build_your_own_url(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Positive TC-037 PASS")

    def test_TC_P_38(self):
        driver = self.driver
        print("Positive TC-038")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the button Menu and click

        H.finding_menu_button(driver)
        delay()

        # Finding the button Shopping Tools and click

        H.shopping_tools_button(driver)
        delay()

        # Finding Compare Models button and click

        H.compare_models_button(driver)
        delay()

        # Check Compare Models Url

        H.check_compare_models_url(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Positive TC-038 PASS")

    def test_TC_P_39(self):
        driver = self.driver
        print("Positive TC-039")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the button Menu and click

        H.finding_menu_button(driver)
        delay()

        # Finding the button Shopping Tools and click

        H.shopping_tools_button(driver)
        delay()

        # Finding New & Used Inventory button and click

        H.new_and_used_button(driver)
        delay()

        # Check New & Used Inventory Url

        H.check_new_and_used_url(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Positive TC-039 PASS")

    def test_TC_P_40(self):
        driver = self.driver
        print("Positive TC-040")
        driver.get("https://www.porsche.com/usa/")
        time.sleep(3)
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the button Menu and click

        H.finding_menu_button(driver)
        delay()

        # Finding the button Shopping Tools and click

        H.shopping_tools_button(driver)
        delay()

        # Finding Current Vehicle Offers button and click

        H.current_vehicle_offers_button(driver)
        delay()

        # Check Current Vehicle Offers Url

        H.check_current_vehicle_offers_url(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Positive TC-040 PASS")

    def test_TC_P_41(self):
        driver = self.driver
        print("Positive TC-041")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the button Menu and click

        H.finding_menu_button(driver)
        delay()

        # Finding the button Shopping Tools and click

        H.shopping_tools_button(driver)
        delay()

        # Finding Certified Pre-Owned & Warranty button and click

        H.certified_button(driver)
        delay()

        # Check Certified Pre-Owned & Warranty Url

        H.check_certified_url(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Positive TC-041 PASS")

    def test_TC_P_42(self):
        driver = self.driver
        print("Positive TC-042")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the button Menu and click

        H.finding_menu_button(driver)
        delay()

        # Finding the button Shopping Tools and click

        H.shopping_tools_button(driver)
        delay()

        # Finding Porsche Financial Services button and click

        H.porsche_financial_button(driver)
        delay()

        # Check Porsche Financial Services Url

        H.check_porsche_financial_url(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Positive TC-042 PASS")

    def test_TC_P_43(self):
        driver = self.driver
        print("Positive TC-043")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the button Menu and click

        H.finding_menu_button(driver)
        delay()

        # Finding the button Shopping Tools and click

        H.shopping_tools_button(driver)
        delay()

        # Finding E-Mobility & E-Performance button and click

        H.e_mobility_button(driver)
        delay()

        # Check E-Mobility & E-Performance Url

        H.check_e_mobility_url(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Positive TC-043 PASS")

    def test_TC_P_44(self):
        driver = self.driver
        print("Positive TC-044")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the button Menu and click

        H.finding_menu_button(driver)
        delay()

        # Finding Account button and click

        H.account_button(driver)
        delay()

        # Finding Log In button and click

        H.log_in_button(driver)
        delay()

        # Check Log In Url

        H.check_log_in_url(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Positive TC-044 PASS")

    def test_TC_P_45(self):
        driver = self.driver
        print("Positive TC-045")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the button Menu and click

        H.finding_menu_button(driver)
        delay()

        # Finding Account button and click

        H.account_button(driver)
        delay()

        # Finding Saved Searches button and click

        H.saved_searches_button(driver)
        delay()

        # Check Saved Searches Url

        H.check_saved_searches_url(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Positive TC-045 PASS")

    def test_TC_P_46(self):
        driver = self.driver
        print("Positive TC-046")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the button Menu and click

        H.finding_menu_button(driver)
        delay()

        # Finding Account button and click

        H.account_button(driver)
        delay()

        # Finding Saved Cars button and click

        H.saved_cars_button(driver)
        delay()

        # Check Saved Cars Url

        H.check_saved_cars_url(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Positive TC-046 PASS")

    def test_TC_P_47(self):
        driver = self.driver
        print("Positive TC-047")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the button Menu and click

        H.finding_menu_button(driver)
        delay()

        # Finding Account button and click

        H.account_button(driver)
        delay()

        # Finding Find Connect Services button and click

        H.find_connect_services_button(driver)
        delay()

        # Check Find Connect Services Url

        H.check_find_connect_services_url(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Positive TC-047 PASS")

    def test_TC_P_48(self):
        driver = self.driver
        print("Positive TC-048")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the button Menu and click

        H.finding_menu_button(driver)
        delay()

        # Finding Account button and click

        H.account_button(driver)
        delay()

        # Finding Contact & Support button and click

        H.contact_and_support_button(driver)
        delay()
        actions = Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Contact & Support Url

        H.check_contact_and_support_url(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Positive TC-048 PASS")

class EdgePorscheNegativeTests(unittest.TestCase):

    def setUp(self):
        os.environ["SE_DRIVER_MIRROR_URL"] = "https://msedgedriver.microsoft.com"
        options = Edge_Options()
        options.add_argument('--headless')
        options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = webdriver.Edge(options=options)
        self.driver.maximize_window()

    def test_TC_N_36(self):
        driver = self.driver
        print("Negative TC-036")
        driver.get("https://www.porsche.com/usa/4")
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        print("Negative TC-036 PASS")

    def test_TC_N_37(self):
        driver = self.driver
        print("Negative TC-037")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding Menu button and click

        H.finding_menu_button(driver)
        delay()

        # Finding Find Your Porsche Center button and click

        H.find_your_porsche_center(driver)
        delay()

        # Finding Zip Code Search window click and input value "!@#$%^&*()_+"

        H.zip_code1(driver)
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Negative TC-036 PASS")

    def test_TC_N_38(self):
        driver = self.driver
        print("Negative TC-038")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the Menu button and click

        H.finding_menu_button(driver)
        delay()

        # Finding Find Your Porsche Center button and click

        H.find_your_porsche_center(driver)
        delay()

        # Finding Zip Code Search window click and input value "AsDFghjKL"

        H.zip_code2(driver)
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        #Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Negative TC-036 PASS")

    def test_TC_N_39(self):
        driver = self.driver
        print("Negative TC-039")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the Menu button and click

        H.finding_menu_button(driver)
        delay()

        # Finding Find Your Porsche Center button and click

        H.find_your_porsche_center(driver)
        delay()

        # Finding Zip Code Search window click and input value "123456789"

        H.zip_code3(driver)
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Negative TC-036 PASS")

    def test_TC_N_40(self):
        driver = self.driver
        print("Negative TC-040")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Scroll Down page

        career = driver.find_element(By.XPATH, "//pnav-footer[@class='pcom-main-footer hydrated']")
        driver.execute_script("arguments[0].scrollIntoView()", career)
        delay()

        # Finding Career button and click

        H.career_button(driver)
        delay()

        # Check Job Porsche Url

        H.check_job_porsche_url(driver)

        # Scroll Down page

        jobs = driver.find_element(By.XPATH, "//section[@id='pcom-Jobs-at-Porsche']")
        driver.execute_script("arguments[0].scrollIntoView()", jobs)
        delay()

        # Finding Search window, click and put value "!@#$%^&*()_+" for job search

        H.find_search_window1(driver)
        delay()
        actions = Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Switch to new tab

        driver.switch_to.window(driver.window_handles[-1])
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Get the title

        title = driver.title

        # Check the title
        if title == "Our vacancies | Career-Portal | Dr. Ing. h.c. F. Porsche AG":
            print("Title matches")
        else:
            print("Title does NOT match")

         # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

    def test_TC_N_41(self):
        driver = self.driver
        print("Negative TC-040")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Scroll Down page

        career = driver.find_element(By.XPATH, "//pnav-footer[@class='pcom-main-footer hydrated']")
        driver.execute_script("arguments[0].scrollIntoView()", career)
        delay()

        # Finding Career button and click

        H.career_button(driver)
        delay()

        # Check Job Porsche Url

        H.check_job_porsche_url(driver)

        # Scroll Down page

        jobs = driver.find_element(By.XPATH, "//section[@id='pcom-Jobs-at-Porsche']")
        driver.execute_script("arguments[0].scrollIntoView()", jobs)
        delay()

        # Finding Search window, click and put value "AsDFghjKL" for job search

        H.find_search_window2(driver)
        delay()
        actions = Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Switch to new tab

        driver.switch_to.window(driver.window_handles[-1])
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Get the title

        title = driver.title

        # Check the title
        if title == "Our vacancies | Career-Portal | Dr. Ing. h.c. F. Porsche AG":
            print("Title matches")
        else:
            print("Title does NOT match")

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

    def test_TC_N_42(self):
        driver = self.driver
        print("Negative TC-041")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Scroll Down page

        career = driver.find_element(By.XPATH, "//pnav-footer[@class='pcom-main-footer hydrated']")
        driver.execute_script("arguments[0].scrollIntoView()", career)
        delay()

        # Finding Career button and click

        H.career_button(driver)
        delay()

        # Check Job Porsche Url

        H.check_job_porsche_url(driver)

        # Scroll Down page

        jobs = driver.find_element(By.XPATH, "//section[@id='pcom-Jobs-at-Porsche']")
        driver.execute_script("arguments[0].scrollIntoView()", jobs)
        delay()

        # Finding Search window, click and put value "123456789" for job search

        H.find_search_window3(driver)
        delay()
        actions = Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Switch to new tab

        driver.switch_to.window(driver.window_handles[-1])
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Get the title

        title = driver.title

        # Check the title
        if title == "Our vacancies | Career-Portal | Dr. Ing. h.c. F. Porsche AG":
            print("Title matches")
        else:
            print("Title does NOT match")

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

    def test_TC_N_43(self):
        driver = self.driver
        print("Negative TC-042")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding Menu button and click

        H.finding_menu_button(driver)
        delay()

        # Finding Account button and click

        H.account_button(driver)
        delay()

        # Finding Contact & Support button and click

        H.contact_and_support_button(driver)
        delay()
        actions = Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Ask Porsche Url

        H.check_ask_porsche_url(driver)

        # Finding Search window, click and put value "!@#$%^&*()_+" for Question search

        H.find_ask_search_window1(driver)
        delay()
        actions = Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Result Ask Porsche Url

        H.check_result_ask_porsche_url1(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Negative TC-036 PASS")

    def test_TC_N_44(self):
        driver = self.driver
        print("Negative TC-043")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding Menu button and click

        H.finding_menu_button(driver)
        delay()

        # Finding Account button and click

        H.account_button(driver)
        delay()

        # Finding Contact & Support button and click

        H.contact_and_support_button(driver)
        delay()
        actions = Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Ask Porsche Url

        H.check_ask_porsche_url(driver)

        # Finding Search window, click and put value "AsDFghjKL" for Question search

        H.find_ask_search_window2(driver)
        delay()
        actions = Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Result Ask Porsche Url

        H.check_result_ask_porsche_url2(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Negative TC-036 PASS")

    def test_TC_N_45(self):
        driver = self.driver
        print("Negative TC-044")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding Menu button and click

        H.finding_menu_button(driver)
        delay()

        # Finding Account button and click

        H.account_button(driver)
        delay()

        # Finding Contact & Support button and click

        H.contact_and_support_button(driver)
        delay()
        actions = Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Ask Porsche Url

        H.check_ask_porsche_url(driver)

        # Finding Search window, click and put value "123456789" for Question search

        H.find_ask_search_window3(driver)
        delay()
        actions = Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Result Ask Porsche Url

        H.check_result_ask_porsche_url3(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Negative TC-036 PASS")

    def test_TC_N_46(self):
        driver = self.driver
        print("Negative TC-045")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding Menu button and click

        H.finding_menu_button(driver)
        delay()

        # Finding Account button and click

        H.account_button(driver)
        delay()

        # Finding Contact & Support button and click

        H.contact_and_support_button(driver)
        delay()
        actions = Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Ask Porsche Url

        H.check_ask_porsche_url(driver)

        # Scroll Down to  Owner Manual button

        manual = driver.find_element(By.XPATH, "//article[@id='help']")
        driver.execute_script("arguments[0].scrollIntoView()", manual)
        delay()

        # Finding Owner Manual button and click

        host = driver.find_element(By.CSS_SELECTOR, "p-link[class='hydrated']")
        shadow = host.shadow_root
        owner_manual = shadow.find_element(By.CSS_SELECTOR, ".root")
        driver.execute_script("arguments[0].click();", owner_manual)
        delay()

        # Switch to new tab

        driver.switch_to.window(driver.window_handles[-1])
        delay()

        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Finding Search window, click and put "A12345H6789QWE001" search

        H.find_vin_search_window_button1(driver)
        delay()
        actions = Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Negative TC-036 PASS")

    def test_TC_N_47(self):
        driver = self.driver
        print("Negative TC-046")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding Menu button and click

        H.finding_menu_button(driver)
        delay()

        # Finding Account button and click

        H.account_button(driver)
        delay()

        # Finding Contact & Support button and click

        H.contact_and_support_button(driver)
        delay()
        actions = Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Ask Porsche Url

        H.check_ask_porsche_url(driver)

        # Scroll Down to  Owner Manual button

        manual = driver.find_element(By.XPATH, "//article[@id='help']")
        driver.execute_script("arguments[0].scrollIntoView()", manual)
        delay()

        # Finding Owner Manual button and click

        host = driver.find_element(By.CSS_SELECTOR, "p-link[class='hydrated']")
        shadow = host.shadow_root
        owner_manual = shadow.find_element(By.CSS_SELECTOR, ".root")
        driver.execute_script("arguments[0].click();", owner_manual)
        delay()

        # Switch to new tab

        driver.switch_to.window(driver.window_handles[-1])
        delay()

        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Finding Search window, click and put "!@#$%^&*()_+{}-=+" search

        H.find_vin_search_window_button2(driver)
        delay()
        actions = Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Negative TC-036 PASS")

    def test_TC_N_48(self):
        driver = self.driver
        print("Negative TC-047")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding Menu button and click

        H.finding_menu_button(driver)
        delay()

        # Finding Account button and click

        H.account_button(driver)
        delay()

        # Finding Contact & Support button and click

        H.contact_and_support_button(driver)
        delay()
        actions = Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Check Ask Porsche Url

        H.check_ask_porsche_url(driver)

        # Scroll Down to  Owner Manual button

        manual = driver.find_element(By.XPATH, "//article[@id='help']")
        driver.execute_script("arguments[0].scrollIntoView()", manual)
        delay()

        # Finding Owner Manual button and click

        host = driver.find_element(By.CSS_SELECTOR, "p-link[class='hydrated']")
        shadow = host.shadow_root
        owner_manual = shadow.find_element(By.CSS_SELECTOR, ".root")
        driver.execute_script("arguments[0].click();", owner_manual)
        delay()

        # Switch to new tab

        driver.switch_to.window(driver.window_handles[-1])
        delay()

        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Finding Search window, click and put "12345678912345678" search

        H.find_vin_search_window_button3(driver)
        delay()
        actions = Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        delay()

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Negative TC-036 PASS")

class FirefoxPorschePositiveTests(unittest.TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.page_load_strategy = 'eager'
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.set_preference("dom.webdriver.enabled", False)
        options.set_preference("useAutomationExtension", False)
        options.add_argument('--headless')
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        self.driver.maximize_window()

    def test_TC_P_36(self):
        driver = self.driver
        print("Positive TC-036")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the button Menu and click

        H.finding_menu_button(driver)
        delay()

        # Finding Shopping Tools button and click

        H.shopping_tools_button(driver)
        delay()

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        driver.quit()

        print("Positive TC-036 PASS")

    def test_TC_P_37(self):
        driver = self.driver
        print("Positive TC-037")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the button Menu and click

        H.finding_menu_button(driver)
        delay()

        # Finding the button Shopping Tools and click

        H.shopping_tools_button(driver)
        delay()

        # Finding Build Your Own button and click

        H.build_your_own_button(driver)
        delay()

        # Check Build Your Own Url

        H.check_build_your_own_url(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        driver.quit()

        print("Positive TC-037 PASS")

    def test_TC_P_38(self):
        driver = self.driver
        print("Positive TC-038")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the button Menu and click

        H.finding_menu_button(driver)
        delay()

        # Finding the button Shopping Tools and click

        H.shopping_tools_button(driver)
        delay()

        # Finding Compare Models button and click

        H.compare_models_button(driver)
        delay()

        # Check Compare Models Url

        H.check_compare_models_url(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        driver.quit()

        print("Positive TC-038 PASS")

    def test_TC_P_39(self):
        driver = self.driver
        print("Positive TC-039")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the button Menu and click

        H.finding_menu_button(driver)
        delay()

        # Finding the button Shopping Tools and click

        H.shopping_tools_button(driver)
        delay()

        # Finding New & Used Inventory button and click

        H.new_and_used_button(driver)
        delay()

        # Check New & Used Inventory Url

        H.check_new_and_used_url(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        driver.quit()

        print("Positive TC-039 PASS")

    def test_TC_P_40(self):
        driver = self.driver
        print("Positive TC-040")
        driver.get("https://www.porsche.com/usa/")
        time.sleep(3)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the button Menu and click

        H.finding_menu_button(driver)
        delay()

        # Finding the button Shopping Tools and click

        H.shopping_tools_button(driver)
        delay()

        # Finding Current Vehicle Offers button and click

        H.current_vehicle_offers_button(driver)
        delay()

        # Check Current Vehicle Offers Url

        H.check_current_vehicle_offers_url(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        driver.quit()

        print("Positive TC-040 PASS")

    def test_TC_P_41(self):
        driver = self.driver
        print("Positive TC-041")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the button Menu and click

        H.finding_menu_button(driver)
        delay()

        # Finding the button Shopping Tools and click

        H.shopping_tools_button(driver)
        delay()

        # Finding Certified Pre-Owned & Warranty button and click

        H.certified_button(driver)
        delay()

        # Check Certified Pre-Owned & Warranty Url

        H.check_certified_url(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        driver.quit()

        print("Positive TC-041 PASS")

    def test_TC_P_42(self):
        driver = self.driver
        print("Positive TC-042")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the button Menu and click

        H.finding_menu_button(driver)
        delay()

        # Finding the button Shopping Tools and click

        H.shopping_tools_button(driver)
        delay()

        # Finding Porsche Financial Services button and click

        H.porsche_financial_button(driver)
        delay()

        # Check Porsche Financial Services Url

        H.check_porsche_financial_url(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        driver.quit()

        print("Positive TC-042 PASS")

    def test_TC_P_43(self):
        driver = self.driver
        print("Positive TC-043")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the button Menu and click

        H.finding_menu_button(driver)
        delay()

        # Finding the button Shopping Tools and click

        H.shopping_tools_button(driver)
        delay()

        # Finding E-Mobility & E-Performance button and click

        H.e_mobility_button(driver)
        delay()

        # Check E-Mobility & E-Performance Url

        H.check_e_mobility_url(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        driver.quit()

        print("Positive TC-043 PASS")

    def test_TC_P_44(self):
        driver = self.driver
        print("Positive TC-044")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the button Menu and click

        H.finding_menu_button(driver)
        delay()

        # Finding Account button and click

        H.account_button(driver)
        delay()

        # Finding Log In button and click

        H.log_in_button(driver)
        delay()

        # Check Log In Url

        H.check_log_in_url(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        driver.quit()

        print("Positive TC-044 PASS")

    def test_TC_P_45(self):
        driver = self.driver
        print("Positive TC-045")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the button Menu and click

        H.finding_menu_button(driver)
        delay()

        # Finding Account button and click

        H.account_button(driver)
        delay()

        # Finding Saved Searches button and click

        H.saved_searches_button(driver)
        delay()

        # Check Saved Searches Url

        H.check_saved_searches_url(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        driver.quit()

        print("Positive TC-045 PASS")

    def test_TC_P_46(self):
        driver = self.driver
        print("Positive TC-046")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the button Menu and click

        H.finding_menu_button(driver)
        delay()

        # Finding Account button and click

        H.account_button(driver)
        delay()

        # Finding Saved Cars button and click

        H.saved_cars_button(driver)
        delay()

        # Check Saved Cars Url

        H.check_saved_cars_url(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        driver.quit()

        print("Positive TC-046 PASS")

    def test_TC_P_47(self):
        driver = self.driver
        print("Positive TC-047")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the button Menu and click

        H.finding_menu_button(driver)
        delay()

        # Finding Account button and click

        H.account_button(driver)
        delay()

        # Finding Find Connect Services button and click

        H.find_connect_services_button(driver)
        delay()

        # Check Find Connect Services Url

        H.check_find_connect_services_url(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        driver.quit()

        print("Positive TC-047 PASS")

    def test_TC_P_48(self):
        driver = self.driver
        print("Positive TC-048")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the button Menu and click

        H.finding_menu_button(driver)
        delay()

        # Finding Account button and click

        H.account_button(driver)
        delay()

        # Finding Contact & Support button and click

        H.contact_and_support_button(driver)
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Check Contact & Support Url

        H.check_contact_and_support_url(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        driver.quit()

        print("Positive TC-048 PASS")

class FirefoxPorscheNegativeTests(unittest.TestCase):

    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.page_load_strategy = 'eager'
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.set_preference("dom.webdriver.enabled", False)
        options.set_preference("useAutomationExtension", False)
        options.add_argument('--headless')
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=options)
        self.driver.maximize_window()

    def test_TC_N_36(self):
        driver = self.driver
        print("Negative TC-036")
        driver.get("https://www.porsche.com/usa/4")
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        driver.quit()

        print("Negative TC-036 PASS")

    def test_TC_N_37(self):
        driver = self.driver
        print("Negative TC-037")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding Menu button and click

        H.finding_menu_button(driver)
        delay()

        # Finding Find Your Porsche Center button and click

        H.find_your_porsche_center(driver)
        delay()

        # Finding Zip Code Search window click and input value "!@#$%^&*()_+"

        H.zip_code1(driver)
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        driver.quit()

        print("Negative TC-037 PASS")

    def test_TC_N_38(self):
        driver = self.driver
        print("Negative TC-038")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the Menu button and click

        H.finding_menu_button(driver)
        delay()

        # Finding Find Your Porsche Center button and click

        H.find_your_porsche_center(driver)
        delay()

        # Finding Zip Code Search window click and input value "AsDFghjKL"

        H.zip_code2(driver)
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        #Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        driver.quit()

        print("Negative TC-038 PASS")

    def test_TC_N_39(self):
        driver = self.driver
        print("Negative TC-039")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding the Menu button and click

        H.finding_menu_button(driver)
        delay()

        # Finding Find Your Porsche Center button and click

        H.find_your_porsche_center(driver)
        delay()

        # Finding Zip Code Search window click and input value "123456789"

        H.zip_code3(driver)
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        driver.quit()

        print("Negative TC-039 PASS")

    def test_TC_N_40(self):
        driver = self.driver
        print("Negative TC-040")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Scroll Down page

        career = driver.find_element(By.XPATH, "//pnav-footer[@class='pcom-main-footer hydrated']")
        driver.execute_script("arguments[0].scrollIntoView()", career)
        delay()

        # Finding Career button and click

        H.career_button(driver)
        delay()

        # Check Job Porsche Url

        H.check_job_porsche_url(driver)

        # Scroll Down page

        jobs = driver.find_element(By.XPATH, "//section[@id='pcom-Jobs-at-Porsche']")
        driver.execute_script("arguments[0].scrollIntoView()", jobs)
        delay()

        # Finding Search window, click and put value "!@#$%^&*()_+" for job search

        H.find_search_window1(driver)
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Switch to new tab

        driver.switch_to.window(driver.window_handles[-1])
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Get the title

        title = driver.title

        # Check the title
        if title == "Our vacancies | Career-Portal | Dr. Ing. h.c. F. Porsche AG":
            print("Title matches")
        else:
            print("Title does NOT match")

         # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        driver.quit()

        print("Negative TC-040 PASS")

    def test_TC_N_41(self):
        driver = self.driver
        print("Negative TC-041")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Scroll Down page

        career = driver.find_element(By.XPATH, "//pnav-footer[@class='pcom-main-footer hydrated']")
        driver.execute_script("arguments[0].scrollIntoView()", career)
        delay()

        # Finding Career button and click

        H.career_button(driver)
        delay()

        # Check Job Porsche Url

        H.check_job_porsche_url(driver)

        # Scroll Down page

        jobs = driver.find_element(By.XPATH, "//section[@id='pcom-Jobs-at-Porsche']")
        driver.execute_script("arguments[0].scrollIntoView()", jobs)
        delay()

        # Finding Search window, click and put value "AsDFghjKL" for job search

        H.find_search_window2(driver)
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Switch to new tab

        driver.switch_to.window(driver.window_handles[-1])
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Get the title

        title = driver.title

        # Check the title
        if title == "Our vacancies | Career-Portal | Dr. Ing. h.c. F. Porsche AG":
            print("Title matches")
        else:
            print("Title does NOT match")

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        driver.quit()

        print("Negative TC-041 PASS")

    def test_TC_N_42(self):
        driver = self.driver
        print("Negative TC-042")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Scroll Down page

        career = driver.find_element(By.XPATH, "//pnav-footer[@class='pcom-main-footer hydrated']")
        driver.execute_script("arguments[0].scrollIntoView()", career)
        delay()

        # Finding Career button and click

        H.career_button(driver)
        delay()

        # Check Job Porsche Url

        H.check_job_porsche_url(driver)

        # Scroll Down page

        jobs = driver.find_element(By.XPATH, "//section[@id='pcom-Jobs-at-Porsche']")
        driver.execute_script("arguments[0].scrollIntoView()", jobs)
        delay()

        # Finding Search window, click and put value "123456789" for job search

        H.find_search_window3(driver)
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Switch to new tab

        driver.switch_to.window(driver.window_handles[-1])
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Get the title

        title = driver.title

        # Check the title
        if title == "Our vacancies | Career-Portal | Dr. Ing. h.c. F. Porsche AG":
            print("Title matches")
        else:
            print("Title does NOT match")

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        driver.quit()

        print("Negative TC-042 PASS")

    def test_TC_N_43(self):
        driver = self.driver
        print("Negative TC-043")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding Menu button and click

        H.finding_menu_button(driver)
        delay()

        # Finding Account button and click

        H.account_button(driver)
        delay()

        # Finding Contact & Support button and click

        H.contact_and_support_button(driver)
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Check Ask Porsche Url

        H.check_ask_porsche_url(driver)

        # Finding Search window, click and put value "!@#$%^&*()_+" for Question search

        H.find_ask_search_window1(driver)
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Check Result Ask Porsche Url

        H.check_result_ask_porsche_url1(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Negative TC-036 PASS")

        driver.quit()

        print("Negative TC-043 PASS")

    def test_TC_N_44(self):
        driver = self.driver
        print("Negative TC-044")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding Menu button and click

        H.finding_menu_button(driver)
        delay()

        # Finding Account button and click

        H.account_button(driver)
        delay()

        # Finding Contact & Support button and click

        H.contact_and_support_button(driver)
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Check Ask Porsche Url

        H.check_ask_porsche_url(driver)

        # Finding Search window, click and put value "AsDFghjKL" for Question search

        H.find_ask_search_window2(driver)
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Check Result Ask Porsche Url

        H.check_result_ask_porsche_url2(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Negative TC-036 PASS")

        driver.quit()

        print("Negative TC-044 PASS")

    def test_TC_N_45(self):
        driver = self.driver
        print("Negative TC-045")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding Menu button and click

        H.finding_menu_button(driver)
        delay()

        # Finding Account button and click

        H.account_button(driver)
        delay()

        # Finding Contact & Support button and click

        H.contact_and_support_button(driver)
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Check Ask Porsche Url

        H.check_ask_porsche_url(driver)

        # Finding Search window, click and put value "123456789" for Question search

        H.find_ask_search_window3(driver)
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Check Result Ask Porsche Url

        H.check_result_ask_porsche_url3(driver)

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        print("Negative TC-036 PASS")

        driver.quit()

        print("Negative TC-045 PASS")

    def test_TC_N_46(self):
        driver = self.driver
        print("Negative TC-046")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding Menu button and click

        H.finding_menu_button(driver)
        delay()

        # Finding Account button and click

        H.account_button(driver)
        delay()

        # Finding Contact & Support button and click

        H.contact_and_support_button(driver)
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Check Ask Porsche Url

        H.check_ask_porsche_url(driver)

        # Scroll Down to  Owner Manual button

        manual = driver.find_element(By.XPATH, "//article[@id='help']")
        driver.execute_script("arguments[0].scrollIntoView()", manual)
        delay()

        # Finding Owner Manual button and click

        host = driver.find_element(By.CSS_SELECTOR, "p-link[class='hydrated']")
        shadow = host.shadow_root
        owner_manual = shadow.find_element(By.CSS_SELECTOR, ".root")
        driver.execute_script("arguments[0].click();", owner_manual)
        delay()

        # Switch to new tab

        driver.switch_to.window(driver.window_handles[-1])
        delay()

        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Finding Search window, click and put "A12345H6789QWE001" search

        H.find_vin_search_window_button1(driver)
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        driver.quit()

        print("Negative TC-046 PASS")

    def test_TC_N_47(self):
        driver = self.driver
        print("Negative TC-047")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding Menu button and click

        H.finding_menu_button(driver)
        delay()

        # Finding Account button and click

        H.account_button(driver)
        delay()

        # Finding Contact & Support button and click

        H.contact_and_support_button(driver)
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Check Ask Porsche Url

        H.check_ask_porsche_url(driver)

        # Scroll Down to  Owner Manual button

        manual = driver.find_element(By.XPATH, "//article[@id='help']")
        driver.execute_script("arguments[0].scrollIntoView()", manual)
        delay()

        # Finding Owner Manual button and click

        host = driver.find_element(By.CSS_SELECTOR, "p-link[class='hydrated']")
        shadow = host.shadow_root
        owner_manual = shadow.find_element(By.CSS_SELECTOR, ".root")
        driver.execute_script("arguments[0].click();", owner_manual)
        delay()

        # Switch to new tab

        driver.switch_to.window(driver.window_handles[-1])
        delay()

        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Finding Search window, click and put "!@#$%^&*()_+{}-=+" search

        H.find_vin_search_window_button2(driver)
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        driver.quit()

        print("Negative TC-047 PASS")

    def test_TC_N_48(self):
        driver = self.driver
        print("Negative TC-048")
        driver.get("https://www.porsche.com/usa/")
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Check Porsche Url

        H.check_porsche_url(driver)

        # Finding Menu button and click

        H.finding_menu_button(driver)
        delay()

        # Finding Account button and click

        H.account_button(driver)
        delay()

        # Finding Contact & Support button and click

        H.contact_and_support_button(driver)
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Check Ask Porsche Url

        H.check_ask_porsche_url(driver)

        # Scroll Down to  Owner Manual button

        manual = driver.find_element(By.XPATH, "//article[@id='help']")
        driver.execute_script("arguments[0].scrollIntoView()", manual)
        delay()

        # Finding Owner Manual button and click

        host = driver.find_element(By.CSS_SELECTOR, "p-link[class='hydrated']")
        shadow = host.shadow_root
        owner_manual = shadow.find_element(By.CSS_SELECTOR, ".root")
        driver.execute_script("arguments[0].click();", owner_manual)
        delay()

        # Switch to new tab

        driver.switch_to.window(driver.window_handles[-1])
        delay()

        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.TAB)
        actions.pause(0.3)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Finding Search window, click and put "12345678912345678" search

        H.find_vin_search_window_button3(driver)
        delay()
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        delay()

        # Screenshot of result

        save_screenshot(driver, "05_after_submit")

        print(f"\nAll screenshots saved to: {SCREENSHOT_DIR}")

        driver.quit()

        print("Negative TC-048 PASS")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports'))
#if __name__ == "__main__":
 #   unittest.main(AllureReports)