import time
import unittest
import random
from selenium import webdriver
import os

# import HtmlTestRunner
# import AllureReports
import Helpers_Porsche as h


from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.options import Options as EdgeOptions

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def delay():
    time.sleep(random.randint(3,4))
# This function is for delay() it randomly pics time between 2 and 4 seconds
def keyboard_tab_times_then_space(driver, times=5):
    """
    Used in TC_P_015: press TAB N times, then SPACE (example: captcha focus attempt).
    """
    keys = [Keys.TAB] * times + [Keys.SPACE]
    driver.switch_to.active_element.send_keys(*keys)

class ChromeTestPositive(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        #options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()
        #options.page_load_strategy = 'eager'
        driver = self.driver
        wait = WebDriverWait(driver, 5)
# This is a class setUp. We will have 2 (chrome, edge)
    def test_chrome_TC_P_001(self):
        driver = self.driver
#Verify that the Cayenne model page opens correctly and displays all three Cayenne models
# 1. Navigate to the link Main Page
        h.Porsche_link_MainPage(driver)
        h.captcha(driver)
# 2. Click the burger menu in the top-left corner of the page
        h.burger_menu(driver)
# 3. Click the “Model” button and scroll down to the “Cayenne” and click
        keyboard_tab_times_then_space(driver, times=6)
        time.sleep(7)
# 4. Verify that three Cayenne models are present on the page
        host = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
        delay()
        shadow_host = host.shadow_root
        delay()
        cayenne_electric = shadow_host.find_element(By.CSS_SELECTOR, "a[class='model-link sc-phn-nd-car-body-types-drawer']["
                                                                  "href='https://www.porsche.com/usa/models/cayenne/cayenne-electric-models/cayenne-electric/']")
        if cayenne_electric:
            print('Cayenne Electric model is present on the page')
        else:
            print('Cayenne Electric model is MISSING ON THE PAGE')

        host = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
        delay()
        shadow_host = host.shadow_root
        delay()
        cayenne_2 = shadow_host.find_element(By.CSS_SELECTOR, "a[class='model-link sc-phn-nd-car-body-types-drawer']["
                                                                  "href='https://www.porsche.com/usa/models/cayenne/cayenne-models/cayenne/']")
        if cayenne_2:
            print('Cayenne_2 model is present on the page')
        else:
            print('Cayenne_2 model is MISSING ON THE PAGE')

        host = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
        delay()
        shadow_host = host.shadow_root
        delay()
        cayenne_coupe = shadow_host.find_element(By.CSS_SELECTOR, "a[class='model-link "
                                                                  "sc-phn-nd-car-body-types-drawer']["
                                                                  "href='https://www.porsche.com/usa/models/cayenne/cayenne-coupe-models/cayenne-coupe/']")
        if cayenne_coupe:
            print('Cayenne Coupe model is present on the page')
        else:
            print('Cayenne Coupe model is MISSING ON THE PAGE')

        driver.quit()

    def test_chrome_TC_P_002(self):
        driver = self.driver
#Verify that the “Cayenne Coupe” link works correctly and opens the correct page
# 1. Navigate to the link Main Page
        h.Porsche_link_MainPage(driver)
        h.captcha(driver)
# 2. Click the burger menu in the top-left corner of the page
        h.burger_menu(driver)
# 3. Click the “Model” button and scroll down to the “Cayenne” model
        keyboard_tab_times_then_space(driver, times=6)
        time.sleep(3)
# 4. Click the Cayenne model picture link
        host = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
        delay()
        shadow = host.shadow_root
        delay()
        cayenne_coupe = shadow.find_element(By.CSS_SELECTOR, "a[class='model-link "
                                                                  "sc-phn-nd-car-body-types-drawer']["
                                                                  "href='https://www.porsche.com/usa/models/cayenne/cayenne-coupe-models/cayenne-coupe/']")
        driver.execute_script("arguments[0].click();", cayenne_coupe)
        time.sleep(6)
# 5. Scroll down to the “Cayenne Coupe Highlights” section and verify the section is present on the page
        cayenne_coupe_highlights = driver.find_element(By.ID, "pcom-d0c62d3c1f04c61ed210c8d40953a857971e32bb354ed822fce6afc6c874380a")
        driver.execute_script("arguments[0].scrollIntoView()", cayenne_coupe_highlights)
        time.sleep(5)

        if cayenne_coupe_highlights:
            print ("Cayenne Coupe Highlights section is present on the page")
        else:
            print("Cayenne Coupe Highlights section NOT ON THE PAGE")

        driver.quit()

    def test_chrome_TC_P_003(self):
        driver = self.driver
#Verify that the ‘Interior’ and ‘Exterior’ buttons in the “Even more breathtaking from many angles: the new Cayenne E‑Hybrid Coupe” section function correctly
# 1. Go to the link Cayenne Coupe
        h.Porsche_link_CayenneCoupe(driver)
        h.captcha(driver)
# 2. Scroll to the "Even more breathtaking from many angles: the new Cayenne E-Hybrid Coupe" section
        many_angles = driver.find_element(By.ID, "pcom-9b952eb1f6b3c05a7ca8911a9e1c72d497c9227519013d9b7437e51da18e93be")
        driver.execute_script("arguments[0].scrollIntoView()", many_angles)
        time.sleep(6)
# 3. Find Interior and Exterior buttons
        interior_btn = driver.find_element(By.CSS_SELECTOR, "p-button[data-test='car-viewer-switcher_interior-button']")
        exterior_btn = driver.find_element(By.CSS_SELECTOR, "p-button[data-test='car-viewer-switcher_exterior-button']")
# Click Interior
        driver.execute_script("arguments[0].click();", interior_btn)
        time.sleep(2)
# Check Interior container
        interior_pic = driver.find_element(By.ID, "pcom-9b952eb1f6b3c05a7ca8911a9e1c72d497c9227519013d9b7437e51da18e93be")
        if interior_pic:
            print("Interior picture is visible.")
        else:
            print("Interior picture is NOT visible.")
# Click Exterior
        driver.execute_script("arguments[0].click();", exterior_btn)
        time.sleep(2)
# Check Exterior container
        exterior_pic = driver.find_element(By.ID, "car-viewer-exterior-8")
        if exterior_pic.is_displayed():
            print("Exterior picture is visible.")
        else:
            print("Exterior picture is NOT visible.")

        driver.quit()

    def test_chrome_TC_P_004(self):
        driver = self.driver
#Verify that the “Lease” menu in the “Porsche Financial Services for the Cayenne Coupe” section opens the correct information
# 1. Go to the link Cayenne Coupe
        h.Porsche_link_CayenneCoupe(driver)
        h.captcha(driver)
# 2. Scroll to the "Porsche Financial Services for the Cayenne Coupe" section
        financial_services = driver.find_element(By.ID, "pcom-d1e0364e7b1690af8f00fd89f5e4922751ce838f6cbf7b211c979b95c34a1303")
        driver.execute_script("arguments[0].scrollIntoView()", financial_services)
        delay()
# 3. Open the "Lease" menu
        host = driver.find_element(By.CSS_SELECTOR, "financial-services-stage")
        delay()
        shadow = host.shadow_root
        delay()
        host2 = shadow.find_element(By.CSS_SELECTOR, "slfinoffer-p-accordion")
        shadow2 = host2.shadow_root
        delay()
        lease_button = shadow2.find_element(By.ID, "accordion-control")
        driver.execute_script("arguments[0].click();", lease_button)
        time.sleep(2)
# 4. Verify that the correct information is displayed
        host = driver.find_element(By.CSS_SELECTOR, "financial-services-stage")
        delay()
        shadow = host.shadow_root
        delay()
        lease_info = shadow.find_element(By.CSS_SELECTOR, "div[class='GLY1KsGpwuod0aGGtX2A']")
        if lease_info.is_displayed():
            print("Lease info is visible.")
        else:
            print("Lease info is NOT visible.")

        driver.quit()

    def test_chrome_TC_P_005(self):
        driver = self.driver
#Verify that color selection updates the vehicle preview in the "Build Your Porsche" section
# 1. Go to the link Cayenne Coupe
        h.Porsche_link_CayenneCoupe(driver)
        h.captcha(driver)
# 2. Scroll to the "Build Your Porsche" section
        build_your_porsche = driver.find_element(By.ID, "pcom-a4e1819bd49ad3e78da73baea6eacb6065773af36d7559f5321a5ba8eb0f5769")
        driver.execute_script("arguments[0].scrollIntoView()", build_your_porsche)
        time.sleep(3)
        iframe = driver.find_element(By.CSS_SELECTOR, 'iframe[class="SoftColorator__iframe__39988"]')
        driver.switch_to.frame(iframe)
# 3. Click the Red color swatch and verify that the vehicle preview updates to red
        red_color = driver.find_element(By.XPATH, "//li[@data-option-id='F0L']")
        driver.execute_script("arguments[0].click();", red_color)
        delay()
        red_color_car = driver.find_element(By.CSS_SELECTOR,"img[src='https://iod.prs.porsche.com/iod/image/WW/9YBAI1/1/N4KABGBEDGD2B2AzAlgc0mAXGUEKQEN5kBbAgF2QQGcNsBtMAXQBpw8YCSBTAJwLo52eKMgAmgyNwAe5ALQAbWAHc5iXgnkLuicpDYj8sAA6Uag3IfwA3Ar2RE9WKGO7UA1uRORheAL6+fgYc3PDWyBrwPPBO2JYikOKSAOoAFsjkfLCwJGAACrC81NCp3Pq+RqZU8LTOwGABIkG+kApoqZTw6HUVohLOkAAiAIIAmuVWkCZmNRYNgcH4xhpiAK7QsUKTSQMAnKMAQsMAkgCME4ZTVeY9VvhwqzG8AJ4AwrCuKckXkyQf3ApRtw7IIAEwABlBADZFpdptVagwoMcAGqg-RQUEALQAEhjIAAWABiUPxRIAKgBmfEAdgAGgBWfGnADipJYUFZAA5mYMeRzICjXuiBVyAMoAGXxAEUAEq7Wmjc4CqHHamiymDfGg140-Eo5LKqAEgCqB3xUIA0gqVQA5aXMrEAWXx4KdTIF4KlAqxpzF+IJlIAojLTlqBSzWfjhrb8RKWeTBrKpcxeo1-OxmvhqNxyJ1UIithxEIUyJtIAArYzcdCwyDkfg1Yx2UKbRAEBQ5zMgPxAA']")
        if red_color_car.is_displayed():
            print("Red color car is visible.")
        else:
            print("Red color car is NOT visible.")
# 4. Click the Gold color swatch and verify that the vehicle preview updates to gold
        silver_color = driver.find_element(By.XPATH, '//*[@id="s_exterieur_x_FF0"]')
        driver.execute_script("arguments[0].click();",silver_color)
        delay()
        silver_color_car = driver.find_element(By.CSS_SELECTOR,"img[src='https://iod.prs.porsche.com/iod/image/WW/9YBAI1/1/N4KABGBEDGD2B2AzAlgc0mAXGUEKQEN5kBbAgF2QQGcNsBtMAXQBpw8YCSBTAJwLo52eKMgAmgyNwAe5ALQAbWAHc5iXgnkLuicpDYj8sAA6Uag3IfwA3Ar2RE9WKGO7UA1uRORheAL6+fgYc3PDWyBrwPPBO2JYikOKSAOoAFsjkfLCwJGAACrC81NCp3Pq+RqZU8LTOwGABIkG+kApoqZTw6HUVohLOkAAiAIIAmuVWkCZmNRYNgcH4xhpiAK7QsUKTSQMAnKMAQsMAkgCME4ZTVeY9VvhwqzG8AJ4AwrCuKckXkyQf3ApRtw7IIAEwABlBADZFpdptVagwoMcAGqg-RQUEALQAEhjIAAWABiUPxRIAKgBmfEAdgAGgBWfGnADipJYUFZAA5mYMeRzICjXuiBVyAMoAGXxAEUAEq7Wmjc4CqHHamiymDfGg140-Eo5LKqAEgCqB3xUIA0gqVQA5aXMrEAWXx4KdTIFRPB+KxpzF+IJlIAojLTlqBSzWfjhrb8RKWeTBrKpcxeo1-OxmvhqNxyJ1UIithxEIUyJtIAArYzcdCwyDkfg1Yx2UKbRAEBQ5zMgPxAA']")
        if silver_color_car.is_displayed():
            print("Silver color car is visible.")
        else:
            print("Silver color car is NOT visible.")

        driver.quit()

    def tearDown(self):
        self.driver.quit()

class ChromeTestNegative(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        #options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()
        #options.page_load_strategy = 'eager'
        driver = self.driver
        wait = WebDriverWait(driver, 5)
    def test_chrome_TC_N_001(self):
        driver = self.driver
#Validate that entering a 6‑digit ZIP code in the “Find your new or pre‑owned Porsche” section triggers a validation error
# 1. Navigate to the link Main Page
        h.Porsche_link_MainPage(driver)
        h.captcha(driver)
# 2. Scroll to the "Find your new or pre-owned Porsche" section
        find_zip_code = driver.find_element(By.CSS_SELECTOR, "div[class='PcomGridItem__width-basic__69550 EnhancedFinder__textContainer__b5647']")
        driver.execute_script("arguments[0].scrollIntoView();", find_zip_code)
        delay()
# 3. Enter 125698 in the ZIP code field
        zip_input = driver.find_element(By.CSS_SELECTOR, "input[aria-controls='autocompleteDropdown'][placeholder='Enter City or ZIP Code']")
        zip_input.send_keys("123456123456")
        delay()
# 4. Click Search
        wrapper = driver.find_element(By.CSS_SELECTOR, "p-text-field-wrapper")
        shadow = wrapper.shadow_root
        delay()
        error_msg = shadow.find_element(By.CSS_SELECTOR, "span.message[role='alert']")
        if error_msg.is_displayed():
            print ("Validation error is displayed")
        else:
            print("Validation error was NOT displayed")

        driver.quit()

    def test_chrome_TC_N_002(self):
        driver = self.driver
#Login attempt with empty “Porsche ID” field
# 1. Navigate to the link Main Page
        h.Porsche_link_MainPage(driver)
        h.captcha(driver)
# 2. Click the “Account” button in the upper‑right corner
        h.account_menu(driver)
# 3. In the opened menu, click “Log In”
        h.login_button(driver)
# 4. Click “Log in with password” without filling in the “Porsche ID” field
        login_with_password = driver.find_element(By.XPATH, "//*[@id='continue-btn']")
        driver.execute_script("arguments[0].click();", login_with_password)
        time.sleep(2)
        host = driver.find_element(By.CSS_SELECTOR, 'p-input-text[id="captcha"][name="captcha"]')
        delay()
        shadow = host.shadow_root
        delay()
        # host2 = shadow.find_element(By.CSS_SELECTOR, "pid-acul-captcha")
        # shadow2 = host2.shadow_root
        # delay()
        error_id = shadow.find_element(By.CSS_SELECTOR, 'span[id="message"][class="message"]')
        if error_id.is_displayed():
            print ("Validation error is displayed")
        else:
            print("Validation error was NOT displayed")

        driver.quit()

    def test_chrome_TC_N_003(self):
        driver = self.driver
#Login attempt with a fake “Porsche ID” field
# 1. Navigate to the link Main Page
        h.Porsche_link_MainPage(driver)
        h.captcha(driver)
# 2. Click the “Account” button in the upper‑right corner
        h.account_menu(driver)
# 3. In the opened menu, click “Log In”
        h.login_button(driver)
# 4. Enter a fake or non‑existent Porsche ID (for example: fakeuser123@test.com)
#         host = driver.find_element(By.CSS_SELECTOR, "p-input-email")
#         shadow = host.shadow_root
#         delay()
        username = driver.find_element(By.ID, 'username')
        username.send_keys("fakeuser123@test.com")
        delay()
# 5. Enter any code (123589)
        captcha = driver.find_element(By.ID, "captcha")
        captcha.send_keys('123589')
        delay()
# 6. Click “Log In”
        login_with_password = driver.find_element(By.XPATH, "//*[@id='continue-btn']")
        driver.execute_script("arguments[0].click();", login_with_password)
        time.sleep(2)
        error_captcha = driver.find_element(By.ID, "inline-notification")
        if error_captcha.is_displayed():
            print ("Validation error is displayed")
        else:
            print("Validation error was NOT displayed")

        driver.quit()

    def test_chrome_TC_N_004(self):
        driver = self.driver
#Verify that the “Search equipment options” input field displays an error when an unclear or invalid value is entered
# 1. Navigate to the link Cayenne Coupe
        h.Porsche_link_CayenneCoupe(driver)
        h.captcha(driver)
# 2. Click the "Build Your Porsche" button
        host = driver.find_element(By.CSS_SELECTOR, "p-link")
        delay()
        shadow = host.shadow_root
        delay()
        build_your_porsche_button = shadow.find_element(By.CSS_SELECTOR, "a[href='https://configurator.porsche.com/en-US/mode/model/9YBAI1/']")
        driver.execute_script("arguments[0].scrollIntoView()", build_your_porsche_button)
        delay()
        driver.execute_script("arguments[0].click();", build_your_porsche_button)
        time.sleep(2)
# 3. In the field "Search equipment options" enter test
        host = driver.find_element(By.CSS_SELECTOR, "icc-p-input-search")
        delay()
        shadow = host.shadow_root
        delay()
        search_options_input = shadow.find_element(By.ID, "input-search")
        search_options_input.send_keys("test")
        time.sleep(2)
# 4. Check message
        message_no_options = driver.find_element(By.XPATH , "/html/body/div[1]/main/div/div[1]/div[1]/div[4]/form/search/div")
        if message_no_options.is_displayed():
            print ("Validation error is displayed")
        else:
            print("Validation error was NOT displayed")

        driver.quit()

    def test_chrome_TC_N_005(self):
        driver = self.driver
#Verify that the “Contact Porsche” section does not accept incorrect input
# 1. Navigate to the link Main Page
        h.Porsche_link_MainPage(driver)
        h.captcha(driver)
# 2. Click the “Account” button in the upper‑right corner
        h.account_menu(driver)
# 3. In the opened menu, click "Contact & Support"
        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        delay()
        shadow = host.shadow_root
        delay()
        contact_support = shadow.find_element(By.CSS_SELECTOR, "a[class='pure-link sc-phn-nd-menu-item'][data-id='account/mainmenu.account.contact']")
        driver.execute_script("arguments[0].click();", contact_support)
        time.sleep(4)
# 4. Enter an incorrect country in the input field
        host2 = driver.find_element(By.CSS_SELECTOR, "p-select-wrapper[data-fs-id='contact-form-country-selected']")
        shadow2 = host2.shadow_root
        delay()
        host3 = shadow2.find_element(By.CSS_SELECTOR, "p-select-wrapper-dropdown")
        shadow3 = host3.shadow_root
        select_your_country = shadow3.find_element(By.CSS_SELECTOR, "input[id='filter']")
        driver.execute_script("arguments[0].click();", select_your_country)
        delay()
        select_your_country.send_keys("Atlantis")
        no_result = shadow3.find_element(By.CSS_SELECTOR, "div[role='option']")
        driver.execute_script("arguments[0].click();", no_result)
        delay()
        if no_result.is_displayed():
            print ("Validation error is displayed")
        else:
            print("Validation error was NOT displayed")

        driver.quit()

    def tearDown(self):
        self.driver.quit()

class EdgeTestPositive(unittest.TestCase):
    def setUp(self):
        edge_options = EdgeOptions()
        edge_options.add_argument("--disable-blink-features=AutomationControlled")
        edge_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        edge_options.add_experimental_option('useAutomationExtension', False)
        edge_options.add_argument("--no-sandbox")
        edge_options.add_argument("--disable-dev-shm-usage")
        edge_options.add_argument("--start-maximized")
        edge_options.add_argument("--disable-gpu")
        # Настройка папки загрузки
        download_dir = os.path.join(os.getcwd(), "downloads")
        os.makedirs(download_dir, exist_ok=True)
        edge_options.add_experimental_option("prefs", {
            "download.default_directory": download_dir,
            "download.prompt_for_download": False,
        })
        # Инициализация драйвера
        self.driver = webdriver.Edge(options=edge_options)
        # Скрытие автоматизации
        self.driver.execute_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        )
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    # This is a class setUp. We will have 2 (chrome, edge)
    def test_edge_TC_P_001(self):
        driver = self.driver
        # Verify that the Cayenne model page opens correctly and displays all three Cayenne models
        # 1. Navigate to the link Main Page
        h.Porsche_link_MainPage(driver)
        h.captcha(driver)
        # 2. Click the burger menu in the top-left corner of the page
        h.burger_menu(driver)
        # 3. Click the “Model” button and scroll down to the “Cayenne” and click
        keyboard_tab_times_then_space(driver, times=6)
        time.sleep(7)
        # 4. Verify that three Cayenne models are present on the page
        host = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
        delay()
        shadow_host = host.shadow_root
        delay()
        cayenne_electric = shadow_host.find_element(By.CSS_SELECTOR,
                                                    "a[class='model-link sc-phn-nd-car-body-types-drawer']["
                                                    "href='https://www.porsche.com/usa/models/cayenne/cayenne-electric-models/cayenne-electric/']")
        if cayenne_electric:
            print('Cayenne Electric model is present on the page')
        else:
            print('Cayenne Electric model is MISSING ON THE PAGE')

        host = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
        delay()
        shadow_host = host.shadow_root
        delay()
        cayenne_2 = shadow_host.find_element(By.CSS_SELECTOR,
                                             "a[class='model-link sc-phn-nd-car-body-types-drawer']["
                                             "href='https://www.porsche.com/usa/models/cayenne/cayenne-models/cayenne/']")
        if cayenne_2:
            print('Cayenne_2 model is present on the page')
        else:
            print('Cayenne_2 model is MISSING ON THE PAGE')

        host = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
        delay()
        shadow_host = host.shadow_root
        delay()
        cayenne_coupe = shadow_host.find_element(By.CSS_SELECTOR, "a[class='model-link "
                                                                  "sc-phn-nd-car-body-types-drawer']["
                                                                  "href='https://www.porsche.com/usa/models/cayenne/cayenne-coupe-models/cayenne-coupe/']")
        if cayenne_coupe:
            print('Cayenne Coupe model is present on the page')
        else:
            print('Cayenne Coupe model is MISSING ON THE PAGE')

        driver.quit()

    def test_edge_TC_P_002(self):
        driver = self.driver
        # Verify that the “Cayenne Coupe” link works correctly and opens the correct page
        # 1. Navigate to the link Main Page
        h.Porsche_link_MainPage(driver)
        h.captcha(driver)
        # 2. Click the burger menu in the top-left corner of the page
        h.burger_menu(driver)
        # 3. Click the “Model” button and scroll down to the “Cayenne” model
        keyboard_tab_times_then_space(driver, times=6)
        time.sleep(3)
        # 4. Click the Cayenne model picture link
        host = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
        delay()
        shadow = host.shadow_root
        delay()
        cayenne_coupe = shadow.find_element(By.CSS_SELECTOR, "a[class='model-link "
                                                             "sc-phn-nd-car-body-types-drawer']["
                                                             "href='https://www.porsche.com/usa/models/cayenne/cayenne-coupe-models/cayenne-coupe/']")
        driver.execute_script("arguments[0].click();", cayenne_coupe)
        time.sleep(6)
        # 5. Scroll down to the “Cayenne Coupe Highlights” section and verify the section is present on the page
        cayenne_coupe_highlights = driver.find_element(By.ID,
                                                       "pcom-d0c62d3c1f04c61ed210c8d40953a857971e32bb354ed822fce6afc6c874380a")
        driver.execute_script("arguments[0].scrollIntoView()", cayenne_coupe_highlights)
        time.sleep(5)

        if cayenne_coupe_highlights:
            print("Cayenne Coupe Highlights section is present on the page")
        else:
            print("Cayenne Coupe Highlights section NOT ON THE PAGE")

        driver.quit()

    def test_edge_TC_P_003(self):
        driver = self.driver
        # Verify that the ‘Interior’ and ‘Exterior’ buttons in the “Even more breathtaking from many angles: the new Cayenne E‑Hybrid Coupe” section function correctly
        # 1. Go to the link Cayenne Coupe
        h.Porsche_link_CayenneCoupe(driver)
        h.captcha(driver)
        # 2. Scroll to the "Even more breathtaking from many angles: the new Cayenne E-Hybrid Coupe" section
        many_angles = driver.find_element(By.ID,
                                          "pcom-9b952eb1f6b3c05a7ca8911a9e1c72d497c9227519013d9b7437e51da18e93be")
        driver.execute_script("arguments[0].scrollIntoView()", many_angles)
        time.sleep(6)
        # 3. Find Interior and Exterior buttons
        interior_btn = driver.find_element(By.CSS_SELECTOR,
                                           "p-button[data-test='car-viewer-switcher_interior-button']")
        exterior_btn = driver.find_element(By.CSS_SELECTOR,
                                           "p-button[data-test='car-viewer-switcher_exterior-button']")
        # Click Interior
        driver.execute_script("arguments[0].click();", interior_btn)
        time.sleep(2)
        # Check Interior container
        interior_pic = driver.find_element(By.ID,
                                           "pcom-9b952eb1f6b3c05a7ca8911a9e1c72d497c9227519013d9b7437e51da18e93be")
        if interior_pic:
            print("Interior picture is visible.")
        else:
            print("Interior picture is NOT visible.")
        # Click Exterior
        driver.execute_script("arguments[0].click();", exterior_btn)
        time.sleep(2)
        # Check Exterior container
        exterior_pic = driver.find_element(By.ID, "car-viewer-exterior-8")
        if exterior_pic.is_displayed():
            print("Exterior picture is visible.")
        else:
            print("Exterior picture is NOT visible.")

        driver.quit()

    def test_edge_TC_P_004(self):
        driver = self.driver
        # Verify that the “Lease” menu in the “Porsche Financial Services for the Cayenne Coupe” section opens the correct information
        # 1. Go to the link Cayenne Coupe
        h.Porsche_link_CayenneCoupe(driver)
        h.captcha(driver)
        # 2. Scroll to the "Porsche Financial Services for the Cayenne Coupe" section
        financial_services = driver.find_element(By.ID,
                                                 "pcom-d1e0364e7b1690af8f00fd89f5e4922751ce838f6cbf7b211c979b95c34a1303")
        driver.execute_script("arguments[0].scrollIntoView()", financial_services)
        delay()
        # 3. Open the "Lease" menu
        host = driver.find_element(By.CSS_SELECTOR, "financial-services-stage")
        delay()
        shadow = host.shadow_root
        delay()
        host2 = shadow.find_element(By.CSS_SELECTOR, "slfinoffer-p-accordion")
        shadow2 = host2.shadow_root
        delay()
        lease_button = shadow2.find_element(By.ID, "accordion-control")
        driver.execute_script("arguments[0].click();", lease_button)
        time.sleep(2)
        # 4. Verify that the correct information is displayed
        host = driver.find_element(By.CSS_SELECTOR, "financial-services-stage")
        delay()
        shadow = host.shadow_root
        delay()
        lease_info = shadow.find_element(By.CSS_SELECTOR, "div[class='GLY1KsGpwuod0aGGtX2A']")
        if lease_info.is_displayed():
            print("Lease info is visible.")
        else:
            print("Lease info is NOT visible.")

        driver.quit()

    def test_edge_TC_P_005(self):
        driver = self.driver
        # Verify that color selection updates the vehicle preview in the "Build Your Porsche" section
        # 1. Go to the link Cayenne Coupe
        h.Porsche_link_CayenneCoupe(driver)
        h.captcha(driver)
        # 2. Scroll to the "Build Your Porsche" section
        build_your_porsche = driver.find_element(By.ID,
                                                 "pcom-a4e1819bd49ad3e78da73baea6eacb6065773af36d7559f5321a5ba8eb0f5769")
        driver.execute_script("arguments[0].scrollIntoView()", build_your_porsche)
        time.sleep(3)
        iframe = driver.find_element(By.CSS_SELECTOR, 'iframe[class="SoftColorator__iframe__39988"]')
        driver.switch_to.frame(iframe)
        # 3. Click the Red color swatch and verify that the vehicle preview updates to red
        red_color = driver.find_element(By.XPATH, "//li[@data-option-id='F0L']")
        driver.execute_script("arguments[0].click();", red_color)
        delay()
        red_color_car = driver.find_element(By.CSS_SELECTOR,
                                            "img[src='https://iod.prs.porsche.com/iod/image/WW/9YBAI1/1/N4KABGBEDGD2B2AzAlgc0mAXGUEKQEN5kBbAgF2QQGcNsBtMAXQBpw8YCSBTAJwLo52eKMgAmgyNwAe5ALQAbWAHc5iXgnkLuicpDYj8sAA6Uag3IfwA3Ar2RE9WKGO7UA1uRORheAL6+fgYc3PDWyBrwPPBO2JYikOKSAOoAFsjkfLCwJGAACrC81NCp3Pq+RqZU8LTOwGABIkG+kApoqZTw6HUVohLOkAAiAIIAmuVWkCZmNRYNgcH4xhpiAK7QsUKTSQMAnKMAQsMAkgCME4ZTVeY9VvhwqzG8AJ4AwrCuKckXkyQf3ApRtw7IIAEwABlBADZFpdptVagwoMcAGqg-RQUEALQAEhjIAAWABiUPxRIAKgBmfEAdgAGgBWfGnADipJYUFZAA5mYMeRzICjXuiBVyAMoAGXxAEUAEq7Wmjc4CqHHamiymDfGg140-Eo5LKqAEgCqB3xUIA0gqVQA5aXMrEAWXx4KdTIF4KlAqxpzF+IJlIAojLTlqBSzWfjhrb8RKWeTBrKpcxeo1-OxmvhqNxyJ1UIithxEIUyJtIAArYzcdCwyDkfg1Yx2UKbRAEBQ5zMgPxAA']")
        if red_color_car.is_displayed():
            print("Red color car is visible.")
        else:
            print("Red color car is NOT visible.")
        # 4. Click the Gold color swatch and verify that the vehicle preview updates to gold
        silver_color = driver.find_element(By.XPATH, '//*[@id="s_exterieur_x_FF0"]')
        driver.execute_script("arguments[0].click();", silver_color)
        delay()
        silver_color_car = driver.find_element(By.CSS_SELECTOR,
                                               "img[src='https://iod.prs.porsche.com/iod/image/WW/9YBAI1/1/N4KABGBEDGD2B2AzAlgc0mAXGUEKQEN5kBbAgF2QQGcNsBtMAXQBpw8YCSBTAJwLo52eKMgAmgyNwAe5ALQAbWAHc5iXgnkLuicpDYj8sAA6Uag3IfwA3Ar2RE9WKGO7UA1uRORheAL6+fgYc3PDWyBrwPPBO2JYikOKSAOoAFsjkfLCwJGAACrC81NCp3Pq+RqZU8LTOwGABIkG+kApoqZTw6HUVohLOkAAiAIIAmuVWkCZmNRYNgcH4xhpiAK7QsUKTSQMAnKMAQsMAkgCME4ZTVeY9VvhwqzG8AJ4AwrCuKckXkyQf3ApRtw7IIAEwABlBADZFpdptVagwoMcAGqg-RQUEALQAEhjIAAWABiUPxRIAKgBmfEAdgAGgBWfGnADipJYUFZAA5mYMeRzICjXuiBVyAMoAGXxAEUAEq7Wmjc4CqHHamiymDfGg140-Eo5LKqAEgCqB3xUIA0gqVQA5aXMrEAWXx4KdTIFRPB+KxpzF+IJlIAojLTlqBSzWfjhrb8RKWeTBrKpcxeo1-OxmvhqNxyJ1UIithxEIUyJtIAArYzcdCwyDkfg1Yx2UKbRAEBQ5zMgPxAA']")
        if silver_color_car.is_displayed():
            print("Silver color car is visible.")
        else:
            print("Silver color car is NOT visible.")

        driver.quit()

    def tearDown(self):
        self.driver.quit()

class EdgeTestNegative(unittest.TestCase):
    def setUp(self):
        edge_options = EdgeOptions()
        edge_options.add_argument("--disable-blink-features=AutomationControlled")
        edge_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        edge_options.add_experimental_option('useAutomationExtension', False)
        edge_options.add_argument("--no-sandbox")
        edge_options.add_argument("--disable-dev-shm-usage")
        edge_options.add_argument("--start-maximized")
        edge_options.add_argument("--disable-gpu")
        # Настройка папки загрузки
        download_dir = os.path.join(os.getcwd(), "downloads")
        os.makedirs(download_dir, exist_ok=True)
        edge_options.add_experimental_option("prefs", {
            "download.default_directory": download_dir,
            "download.prompt_for_download": False,
        })
        # Инициализация драйвера
        self.driver = webdriver.Edge(options=edge_options)
        # Скрытие автоматизации
        self.driver.execute_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        )
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
# This is a class setUp. We will have 2 (chrome, edge
    def test_edge_TC_N_001(self):
        driver = self.driver
#Validate that entering a 6‑digit ZIP code in the “Find your new or pre‑owned Porsche” section triggers a validation error
# 1. Navigate to the link Main Page
        h.Porsche_link_MainPage(driver)
        h.captcha(driver)
# 2. Scroll to the "Find your new or pre-owned Porsche" section
        find_zip_code = driver.find_element(By.CSS_SELECTOR, "div[class='PcomGridItem__width-basic__69550 EnhancedFinder__textContainer__b5647']")
        driver.execute_script("arguments[0].scrollIntoView();", find_zip_code)
        delay()
# 3. Enter 125698 in the ZIP code field
        zip_input = driver.find_element(By.CSS_SELECTOR, "input[aria-controls='autocompleteDropdown'][placeholder='Enter City or ZIP Code']")
        zip_input.send_keys("123456123456")
        delay()
# 4. Click Search
        wrapper = driver.find_element(By.CSS_SELECTOR, "p-text-field-wrapper")
        shadow = wrapper.shadow_root
        delay()
        error_msg = shadow.find_element(By.CSS_SELECTOR, "span.message[role='alert']")
        if error_msg.is_displayed():
            print ("Validation error is displayed")
        else:
            print("Validation error was NOT displayed")

        driver.quit()

    def test_edge_TC_N_002(self):
        driver = self.driver
        # Login attempt with empty “Porsche ID” field
        # 1. Navigate to the link Main Page
        h.Porsche_link_MainPage(driver)
        h.captcha(driver)
        # 2. Click the “Account” button in the upper‑right corner
        h.account_menu(driver)
        # 3. In the opened menu, click “Log In”
        h.login_button(driver)
        # 4. Click “Log in with password” without filling in the “Porsche ID” field
        login_with_password = driver.find_element(By.XPATH, "//*[@id='continue-btn']")
        driver.execute_script("arguments[0].click();", login_with_password)
        time.sleep(2)
        host = driver.find_element(By.CSS_SELECTOR, 'p-input-text[id="captcha"][name="captcha"]')
        delay()
        shadow = host.shadow_root
        delay()
        # host2 = shadow.find_element(By.CSS_SELECTOR, "pid-acul-captcha")
        # shadow2 = host2.shadow_root
        # delay()
        error_id = shadow.find_element(By.CSS_SELECTOR, 'span[id="message"][class="message"]')
        if error_id.is_displayed():
            print("Validation error is displayed")
        else:
            print("Validation error was NOT displayed")

        driver.quit()

    def test_edge_TC_N_003(self):
        driver = self.driver
        # Login attempt with a fake “Porsche ID” field
        # 1. Navigate to the link Main Page
        h.Porsche_link_MainPage(driver)
        h.captcha(driver)
        # 2. Click the “Account” button in the upper‑right corner
        h.account_menu(driver)
        # 3. In the opened menu, click “Log In”
        h.login_button(driver)
        # 4. Enter a fake or non‑existent Porsche ID (for example: fakeuser123@test.com)
        #         host = driver.find_element(By.CSS_SELECTOR, "p-input-email")
        #         shadow = host.shadow_root
        #         delay()
        username = driver.find_element(By.ID, 'username')
        username.send_keys("fakeuser123@test.com")
        delay()
        # 5. Enter any code (123589)
        captcha = driver.find_element(By.ID, "captcha")
        captcha.send_keys('123589')
        delay()
        # 6. Click “Log In”
        login_with_password = driver.find_element(By.XPATH, "//*[@id='continue-btn']")
        driver.execute_script("arguments[0].click();", login_with_password)
        time.sleep(2)
        error_captcha = driver.find_element(By.ID, "inline-notification")
        if error_captcha.is_displayed():
            print("Validation error is displayed")
        else:
            print("Validation error was NOT displayed")

        driver.quit()

    def test_edge_TC_N_004(self):
        driver = self.driver
#Verify that the “Search equipment options” input field displays an error when an unclear or invalid value is entered
# 1. Navigate to the link Cayenne Coupe
        h.Porsche_link_CayenneCoupe(driver)
        h.captcha(driver)
# 2. Click the "Build Your Porsche" button
        host = driver.find_element(By.CSS_SELECTOR, "p-link")
        delay()
        shadow = host.shadow_root
        delay()
        build_your_porsche_button = shadow.find_element(By.CSS_SELECTOR, "a[href='https://configurator.porsche.com/en-US/mode/model/9YBAI1/']")
        driver.execute_script("arguments[0].scrollIntoView()", build_your_porsche_button)
        delay()
        driver.execute_script("arguments[0].click();", build_your_porsche_button)
        time.sleep(2)
# 3. In the field "Search equipment options" enter test
        host = driver.find_element(By.CSS_SELECTOR, "icc-p-input-search")
        delay()
        shadow = host.shadow_root
        delay()
        search_options_input = shadow.find_element(By.ID, "input-search")
        search_options_input.send_keys("test")
        time.sleep(2)
# 4. Check message
        message_no_options = driver.find_element(By.XPATH , "/html/body/div[1]/main/div/div[1]/div[1]/div[4]/form/search/div")
        if message_no_options.is_displayed():
            print ("Validation error is displayed")
        else:
            print("Validation error was NOT displayed")

        driver.quit()

    def test_edge_TC_N_005(self):
        driver = self.driver
#Verify that the “Contact Porsche” section does not accept incorrect input
# 1. Navigate to the link Main Page
        h.Porsche_link_MainPage(driver)
        h.captcha(driver)
# 2. Click the “Account” button in the upper‑right corner
        h.account_menu(driver)
# 3. In the opened menu, click "Contact & Support"
        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        delay()
        shadow = host.shadow_root
        delay()
        contact_support = shadow.find_element(By.CSS_SELECTOR, "a[class='pure-link sc-phn-nd-menu-item'][data-id='account/mainmenu.account.contact']")
        driver.execute_script("arguments[0].click();", contact_support)
        time.sleep(4)
# 4. Enter an incorrect country in the input field
        host2 = driver.find_element(By.CSS_SELECTOR, "p-select-wrapper[data-fs-id='contact-form-country-selected']")
        shadow2 = host2.shadow_root
        delay()
        host3 = shadow2.find_element(By.CSS_SELECTOR, "p-select-wrapper-dropdown")
        shadow3 = host3.shadow_root
        select_your_country = shadow3.find_element(By.CSS_SELECTOR, "input[id='filter']")
        driver.execute_script("arguments[0].click();", select_your_country)
        delay()
        select_your_country.send_keys("Atlantis")
        no_result = shadow3.find_element(By.CSS_SELECTOR, "div[role='option']")
        driver.execute_script("arguments[0].click();", no_result)
        delay()
        if no_result.is_displayed():
            print ("Validation error is displayed")
        else:
            print("Validation error was NOT displayed")

        driver.quit()

    def tearDown(self):
        self.driver.quit()

# if __name__ == '__main__':
#   unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports'))

# if __name__ == "__main__":
#   unittest.main(AllureReports)