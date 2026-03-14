import unittest
import time
import random

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FF_Options
from selenium.webdriver.edge.options import Options as Edge_Options

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
import os
import HtmlTestRunner

def delay():
    time.sleep(random.randint(3, 5))


def get_shadow(driver, element):
    return driver.execute_script("return arguments[0].shadowRoot", element)


class ChromePorscheTests(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--disable-blink-features=AutomationControlled")

        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
        self.driver.maximize_window()

    def test_TC_N_021_porsche(self):
        driver = self.driver

        # 1. Open Porsche
        driver.get("https://www.porsche.com/usa/")
        WebDriverWait(driver, 5).until(EC.url_contains("porsche.com"))
        delay()

        # 2. Accept Cookies (Shadow DOM)
        host = driver.find_element(By.CSS_SELECTOR, "uc-layer2")
        host_shadow = get_shadow(driver, host)
        modal = host_shadow.find_element(By.CSS_SELECTOR, "uc-p-modal.modal")
        footer = modal.find_element(By.CSS_SELECTOR, "uc-footer.footer")
        footer_shadow = get_shadow(driver, footer)
        accept_host = footer_shadow.find_element(By.CSS_SELECTOR, "uc-p-button.accept")
        accept_shadow = get_shadow(driver, accept_host)
        accept_button = accept_shadow.find_element(By.CSS_SELECTOR, "button.root")
        driver.execute_script("arguments[0].click()", accept_button)
        print(" Accept All clicked")
        delay()

        # 3. Open Burger Menu
        header = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
        shadow = header.shadow_root
        burger = shadow.find_element(By.CSS_SELECTOR, ".phn-burger-button.sc-phn-burger-button.hydrated")
        driver.execute_script("arguments[0].click()", burger)
        print(" Burger opened")
        delay()

        # 4. Click Porsche Shop
        header = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
        shadow = header.shadow_root

        porsche_shop = shadow.find_element(
            By.CSS_SELECTOR,
            "phn-p-button-pure[data-id='shop']"
        )

        driver.execute_script("arguments[0].click()", porsche_shop)
        print(" Porsche Shop clicked")
        delay()

        # 5. Sport & Fitness
        try:
            driver.find_element(By.XPATH, "//*[@id='6eIx5mVTCBDXX9l1gN0INy']/span").is_displayed()
            print(" Sport & Fitness button is displayed")
        except:
            print("Sport & Fitness button NOT displayed")
        el = driver.find_element(By.ID, "6eIx5mVTCBDXX9l1gN0INy")

        # JSON
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
        driver.execute_script("arguments[0].click()", el)

        print(" Sport & Fitness clicked")
        delay()
        print(driver.current_url)
        #filter
        driver.find_element(By.XPATH, '//*[@id="main-content"]/div[4]/div[2]/div[1]/sl-p-button').click()

        time.sleep(3)

        #Price
        main1 = driver.find_element(By.CSS_SELECTOR, "main[id='main-content']")

        accordion = main1.find_element(By.CSS_SELECTOR, "sl-p-accordion[id='accordion-grossPriceFacetValue.amount']")
        shadow1 = accordion.shadow_root
        price_btn = shadow1.find_element(By.CSS_SELECTOR, "button[id='accordion-control']")


        driver.execute_script("arguments[0].click()", price_btn)
        time.sleep(3)

        search = driver.find_element(By.XPATH, "//input[@id='visible-price-min']")
        search.clear()
        search.send_keys("123abc")
        print("No _abc_ printable")
        time.sleep(4)

    def test_TC_N_022_porsche(self):
        driver = self.driver

        # 1. Open Porsche
        driver.get("https://www.porsche.com/usa/")
        WebDriverWait(driver, 5).until(EC.url_contains("porsche.com"))
        delay()

        # 2. Accept Cookies (Shadow DOM)
        host = driver.find_element(By.CSS_SELECTOR, "uc-layer2")
        host_shadow = get_shadow(driver, host)
        modal = host_shadow.find_element(By.CSS_SELECTOR, "uc-p-modal.modal")
        footer = modal.find_element(By.CSS_SELECTOR, "uc-footer.footer")
        footer_shadow = get_shadow(driver, footer)
        accept_host = footer_shadow.find_element(By.CSS_SELECTOR, "uc-p-button.accept")
        accept_shadow = get_shadow(driver, accept_host)
        accept_button = accept_shadow.find_element(By.CSS_SELECTOR, "button.root")
        driver.execute_script("arguments[0].click()", accept_button)
        print(" Accept All clicked")
        delay()

        # 3. Open Burger Menu
        header = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
        shadow = header.shadow_root
        burger = shadow.find_element(By.CSS_SELECTOR, ".phn-burger-button.sc-phn-burger-button.hydrated")
        driver.execute_script("arguments[0].click()", burger)
        print(" Burger opened")
        delay()

        # 4. Click Porsche Shop
        header = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
        shadow = header.shadow_root

        porsche_shop = shadow.find_element(
            By.CSS_SELECTOR,
            "phn-p-button-pure[data-id='shop']"
        )

        driver.execute_script("arguments[0].click()", porsche_shop)
        print(" Porsche Shop clicked")
        delay()

        # 5. Sport & Fitness
        try:
            driver.find_element(By.XPATH, "//*[@id='6eIx5mVTCBDXX9l1gN0INy']/span").is_displayed()
            print(" Sport & Fitness button is displayed")
        except:
            print("Sport & Fitness button NOT displayed")
        el = driver.find_element(By.ID, "6eIx5mVTCBDXX9l1gN0INy")

        # JSON
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
        driver.execute_script("arguments[0].click()", el)

        print(" Sport & Fitness clicked")
        delay()
        print(driver.current_url)
        print("----------------------------------------------------------")

        apparel2 = driver.find_element(By.ID, "3sPh7Q3xNIMDVgMJ0ebWww")
        driver.execute_script("arguments[0].click()", apparel2)
        time.sleep(2)

        fil_but = driver.find_element(By.XPATH, '//*[@id="main-content"]/div[4]/div[2]/div[1]/sl-p-button')
        driver.execute_script("arguments[0].click()", fil_but)
        time.sleep(2)

        main2 = driver.find_element(By.CSS_SELECTOR, "main[id='main-content']")

        accordion = main2.find_element(By.CSS_SELECTOR, "sl-p-accordion[id='accordion-grossPriceFacetValue.amount']")
        shadow2 = accordion.shadow_root
        price_btn2 = shadow2.find_element(By.CSS_SELECTOR, "button[id='accordion-control']")


        driver.execute_script("arguments[0].click()", price_btn2)
        time.sleep(3)

        search = driver.find_element(By.XPATH, "//input[@id='visible-price-min']")
        search.clear()
        search.send_keys("123abc")
        print("No _abc_ printable")
        time.sleep(4)

    def test_TC_N_023_porsche(self):
        driver = self.driver

        # 1. Open Porsche
        driver.get("https://www.porsche.com/usa/")
        WebDriverWait(driver, 5).until(EC.url_contains("porsche.com"))
        delay()

        # 2. Accept Cookies (Shadow DOM)
        host = driver.find_element(By.CSS_SELECTOR, "uc-layer2")
        host_shadow = get_shadow(driver, host)
        modal = host_shadow.find_element(By.CSS_SELECTOR, "uc-p-modal.modal")
        footer = modal.find_element(By.CSS_SELECTOR, "uc-footer.footer")
        footer_shadow = get_shadow(driver, footer)
        accept_host = footer_shadow.find_element(By.CSS_SELECTOR, "uc-p-button.accept")
        accept_shadow = get_shadow(driver, accept_host)
        accept_button = accept_shadow.find_element(By.CSS_SELECTOR, "button.root")
        driver.execute_script("arguments[0].click()", accept_button)
        print(" Accept All clicked")
        delay()

        # 3. Open Burger Menu
        header = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
        shadow = header.shadow_root
        burger = shadow.find_element(By.CSS_SELECTOR, ".phn-burger-button.sc-phn-burger-button.hydrated")
        driver.execute_script("arguments[0].click()", burger)
        print(" Burger opened")
        delay()

        # 4. Click Porsche Shop
        header = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
        shadow = header.shadow_root

        porsche_shop = shadow.find_element(
            By.CSS_SELECTOR,
            "phn-p-button-pure[data-id='shop']"
        )

        driver.execute_script("arguments[0].click()", porsche_shop)
        print(" Porsche Shop clicked")
        delay()

        # 5. Sport & Fitness
        try:
            driver.find_element(By.XPATH, "//*[@id='6eIx5mVTCBDXX9l1gN0INy']/span").is_displayed()
            print(" Sport & Fitness button is displayed")
        except:
            print("Sport & Fitness button NOT displayed")
        el = driver.find_element(By.ID, "6eIx5mVTCBDXX9l1gN0INy")

        # JSON
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
        driver.execute_script("arguments[0].click()", el)

        print(" Sport & Fitness clicked")
        delay()
        print(driver.current_url)
        print("----------------------------------------------------------")

        header3= driver.find_element(By.CSS_SELECTOR, 'header[class="_54nhml2"]')
        accessories = header3.find_element(By.CSS_SELECTOR, 'li[class="jxyldu7 jxyldu6 jxyldu4"][data-node-id="16vl2X4FPGuTZTGZv9CBxV"]')
        asc_btn = accessories.find_element(By.CSS_SELECTOR, 'a[class="_1m67wz30 _1m67wz32 _1m67wz33 _1m67wz36 jxylduj"][id="18SjaMTcwsLqjOwsIuNp6e"]')
        driver.execute_script("arguments[0].click()", asc_btn)
        time.sleep(2)
        print("______________________________________________________________")

        main3 = driver.find_element(By.CSS_SELECTOR, 'main[id="main-content"]')
        slp_button = main3.find_element(By.CSS_SELECTOR, 'sl-p-button[class="hydrated"][data-testid="search-filter-open-button"]')
        shadow3 = slp_button.shadow_root
        filter3 = shadow3.find_element(By.CSS_SELECTOR, 'button[aria-haspopup="dialog"][class="root"][type="button"]')
        driver.execute_script("arguments[0].click()", filter3)
        time.sleep(2)

        main3 = driver.find_element(By.CSS_SELECTOR, "main[id='main-content']")

        accordion3 = main3.find_element(By.CSS_SELECTOR, "sl-p-accordion[id='accordion-grossPriceFacetValue.amount']")
        shadow3 = accordion3.shadow_root
        price_btn3 = shadow3.find_element(By.CSS_SELECTOR, "button[id='accordion-control']")


        driver.execute_script("arguments[0].click()", price_btn3)
        time.sleep(3)

        search = driver.find_element(By.XPATH, "//input[@id='visible-price-min']")
        search.clear()
        search.send_keys("$$&&##")
        print("No _$$&&##_ printable")
        time.sleep(4)

    def test_TC_N_024_porsche(self):
        driver = self.driver

        # 1. Open Porsche
        driver.get("https://www.porsche.com/usa/")
        WebDriverWait(driver, 5).until(EC.url_contains("porsche.com"))
        delay()

        # 2. Accept Cookies (Shadow DOM)
        host = driver.find_element(By.CSS_SELECTOR, "uc-layer2")
        host_shadow = get_shadow(driver, host)
        modal = host_shadow.find_element(By.CSS_SELECTOR, "uc-p-modal.modal")
        footer = modal.find_element(By.CSS_SELECTOR, "uc-footer.footer")
        footer_shadow = get_shadow(driver, footer)
        accept_host = footer_shadow.find_element(By.CSS_SELECTOR, "uc-p-button.accept")
        accept_shadow = get_shadow(driver, accept_host)
        accept_button = accept_shadow.find_element(By.CSS_SELECTOR, "button.root")
        driver.execute_script("arguments[0].click()", accept_button)
        print(" Accept All clicked")
        delay()

        # 3. Open Burger Menu
        header = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
        shadow = header.shadow_root
        burger = shadow.find_element(By.CSS_SELECTOR, ".phn-burger-button.sc-phn-burger-button.hydrated")
        driver.execute_script("arguments[0].click()", burger)
        print(" Burger opened")
        delay()

        # 4. Click Porsche Shop
        header = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
        shadow = header.shadow_root

        porsche_shop = shadow.find_element(
            By.CSS_SELECTOR,
            "phn-p-button-pure[data-id='shop']"
        )

        driver.execute_script("arguments[0].click()", porsche_shop)
        print(" Porsche Shop clicked")
        delay()

        # 5. Sport & Fitness
        try:
            driver.find_element(By.XPATH, "//*[@id='6eIx5mVTCBDXX9l1gN0INy']/span").is_displayed()
            print(" Sport & Fitness button is displayed")
        except:
            print("Sport & Fitness button NOT displayed")
        el = driver.find_element(By.ID, "6eIx5mVTCBDXX9l1gN0INy")

        # JSON
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
        driver.execute_script("arguments[0].click()", el)

        print(" Sport & Fitness clicked")
        delay()
        print(driver.current_url)
        print("----------------------------------------------------------")
        #Watches
        header4 = driver.find_element(By.CSS_SELECTOR, 'header[class="_54nhml2"]')
        watches4 = header4.find_element(By.CSS_SELECTOR, 'a[id="75b4AeyrMgIKwKd6SGdNUH"]')
        driver.execute_script("arguments[0].click()", watches4)
        time.sleep(3)

        main4 = driver.find_element(By.CSS_SELECTOR, 'main[id="main-content"]')
        slp_button = main4.find_element(By.CSS_SELECTOR, 'sl-p-button[class="hydrated"][data-testid="search-filter-open-button"]')
        shadow4 = slp_button.shadow_root
        filter4 = shadow4.find_element(By.CSS_SELECTOR, 'button[aria-haspopup="dialog"][class="root"][type="button"]')
        driver.execute_script("arguments[0].click()", filter4)
        time.sleep(2)

        main4 = driver.find_element(By.CSS_SELECTOR, "main[id='main-content']")

        accordion4 = main4.find_element(By.CSS_SELECTOR, "sl-p-accordion[id='accordion-grossPriceFacetValue.amount']")
        shadow4 = accordion4.shadow_root
        price_btn4 = shadow4.find_element(By.CSS_SELECTOR, "button[id='accordion-control']")


        driver.execute_script("arguments[0].click()", price_btn4)
        time.sleep(3)

        search = driver.find_element(By.XPATH, "//input[@id='visible-price-min']")
        search.clear()
        search.send_keys("$$&&##")
        print("No _$$&&##_ printable")
        time.sleep(4)

    def test_TC_N_025_porsche(self):
        driver = self.driver

        # 1. Open Porsche
        driver.get("https://www.porsche.com/usa/")
        WebDriverWait(driver, 5).until(EC.url_contains("porsche.com"))
        delay()

        # 2. Accept Cookies (Shadow DOM)
        host = driver.find_element(By.CSS_SELECTOR, "uc-layer2")
        host_shadow = get_shadow(driver, host)
        modal = host_shadow.find_element(By.CSS_SELECTOR, "uc-p-modal.modal")
        footer = modal.find_element(By.CSS_SELECTOR, "uc-footer.footer")
        footer_shadow = get_shadow(driver, footer)
        accept_host = footer_shadow.find_element(By.CSS_SELECTOR, "uc-p-button.accept")
        accept_shadow = get_shadow(driver, accept_host)
        accept_button = accept_shadow.find_element(By.CSS_SELECTOR, "button.root")
        driver.execute_script("arguments[0].click()", accept_button)
        print(" Accept All clicked")
        delay()

        # 3. Open Burger Menu
        header = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
        shadow = header.shadow_root
        burger = shadow.find_element(By.CSS_SELECTOR, ".phn-burger-button.sc-phn-burger-button.hydrated")
        driver.execute_script("arguments[0].click()", burger)
        print(" Burger opened")
        delay()

        # 4. Click Porsche Shop
        header = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
        shadow = header.shadow_root

        porsche_shop = shadow.find_element(
            By.CSS_SELECTOR,
            "phn-p-button-pure[data-id='shop']"
        )

        driver.execute_script("arguments[0].click()", porsche_shop)
        print(" Porsche Shop clicked")
        delay()

        # 5. Sport & Fitness
        try:
            driver.find_element(By.XPATH, "//*[@id='6eIx5mVTCBDXX9l1gN0INy']/span").is_displayed()
            print(" Sport & Fitness button is displayed")
        except:
            print("Sport & Fitness button NOT displayed")
        el = driver.find_element(By.ID, "6eIx5mVTCBDXX9l1gN0INy")

        # JSON
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
        driver.execute_script("arguments[0].click()", el)

        print(" Sport & Fitness clicked")
        delay()
        print(driver.current_url)
        print("----------------------------------------------------------")

        header5 = driver.find_element(By.CSS_SELECTOR, 'header[class="_54nhml2"]')
        bags5 = header5.find_element(By.CSS_SELECTOR, 'a[class="_1m67wz30 _1m67wz32 _1m67wz33 _1m67wz36 jxylduj"][id="2PfwsCxbcfT9UvGeTcVmTK"]')
        driver.execute_script("arguments[0].click()", bags5)
        time.sleep(2)

        main5 = driver.find_element(By.CSS_SELECTOR, 'main[id="main-content"]')
        slp5 = main5.find_element(By.CSS_SELECTOR, 'sl-p-button[data-testid="search-filter-open-button"][class="hydrated"]')
        shadow5 = slp5.shadow_root
        filter5 = shadow5.find_element(By.CSS_SELECTOR, 'button[aria-haspopup="dialog"][class="root"]')
        driver.execute_script("arguments[0].click()", filter5)
        time.sleep(2)

        main5 = driver.find_element(By.CSS_SELECTOR, "main[id='main-content']")

        accordion5 = main5.find_element(By.CSS_SELECTOR, "sl-p-accordion[id='accordion-grossPriceFacetValue.amount']")
        shadow5 = accordion5.shadow_root
        price_btn5 = shadow5.find_element(By.CSS_SELECTOR, "button[id='accordion-control']")


        driver.execute_script("arguments[0].click()", price_btn5)
        time.sleep(3)

        search = driver.find_element(By.XPATH, "//input[@id='visible-price-min']")
        search.clear()
        search.send_keys("ASDzxc")
        print("No _ASDzxc_ printable")
        time.sleep(4)

class EdgeDriverManager(unittest.TestCase):
    def setUp(self):
            os.environ["SE_DRIVER_MIRROR_URL"] = "https://msedgedriver.microsoft.com"
            options = Edge_Options()
            options.add_argument("--disable-blink-features=AutomationControlled")
            self.driver = webdriver.Edge(options=options)
            self.driver.maximize_window()

    def test_TC_N_021_porsche(self):
            driver = self.driver

            # 1. Open Porsche
            driver.get("https://www.porsche.com/usa/")
            WebDriverWait(driver, 5).until(EC.url_contains("porsche.com"))
            delay()

            # 2. Accept Cookies (Shadow DOM)
            host = driver.find_element(By.CSS_SELECTOR, "uc-layer2")
            host_shadow = get_shadow(driver, host)
            modal = host_shadow.find_element(By.CSS_SELECTOR, "uc-p-modal.modal")
            footer = modal.find_element(By.CSS_SELECTOR, "uc-footer.footer")
            footer_shadow = get_shadow(driver, footer)
            accept_host = footer_shadow.find_element(By.CSS_SELECTOR, "uc-p-button.accept")
            accept_shadow = get_shadow(driver, accept_host)
            accept_button = accept_shadow.find_element(By.CSS_SELECTOR, "button.root")
            driver.execute_script("arguments[0].click()", accept_button)
            print(" Accept All clicked")
            delay()

            # 3. Open Burger Menu
            header = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
            shadow = header.shadow_root
            burger = shadow.find_element(By.CSS_SELECTOR, ".phn-burger-button.sc-phn-burger-button.hydrated")
            driver.execute_script("arguments[0].click()", burger)
            print(" Burger opened")
            delay()

            # 4. Click Porsche Shop
            header = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
            shadow = header.shadow_root

            porsche_shop = shadow.find_element(
                By.CSS_SELECTOR,
                "phn-p-button-pure[data-id='shop']"
            )

            driver.execute_script("arguments[0].click()", porsche_shop)
            print(" Porsche Shop clicked")
            delay()

            # 5. Sport & Fitness
            try:
                driver.find_element(By.XPATH, "//*[@id='6eIx5mVTCBDXX9l1gN0INy']/span").is_displayed()
                print(" Sport & Fitness button is displayed")
            except:
                print("Sport & Fitness button NOT displayed")
            el = driver.find_element(By.ID, "6eIx5mVTCBDXX9l1gN0INy")

            # JSON
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
            driver.execute_script("arguments[0].click()", el)

            print(" Sport & Fitness clicked")
            delay()
            print(driver.current_url)
            # filter
            driver.find_element(By.XPATH, '//*[@id="main-content"]/div[4]/div[2]/div[1]/sl-p-button').click()

            time.sleep(3)

            # Price
            main1 = driver.find_element(By.CSS_SELECTOR, "main[id='main-content']")

            accordion = main1.find_element(By.CSS_SELECTOR,
                                           "sl-p-accordion[id='accordion-grossPriceFacetValue.amount']")
            shadow1 = accordion.shadow_root
            price_btn = shadow1.find_element(By.CSS_SELECTOR, "button[id='accordion-control']")

            driver.execute_script("arguments[0].click()", price_btn)
            time.sleep(3)

            search = driver.find_element(By.XPATH, "//input[@id='visible-price-min']")
            search.clear()
            search.send_keys("123abc")
            print("No _abc_ printable")
            time.sleep(4)

    def test_TC_N_022_porsche(self):
            driver = self.driver

            # 1. Open Porsche
            driver.get("https://www.porsche.com/usa/")
            WebDriverWait(driver, 5).until(EC.url_contains("porsche.com"))
            delay()

            # 2. Accept Cookies (Shadow DOM)
            host = driver.find_element(By.CSS_SELECTOR, "uc-layer2")
            host_shadow = get_shadow(driver, host)
            modal = host_shadow.find_element(By.CSS_SELECTOR, "uc-p-modal.modal")
            footer = modal.find_element(By.CSS_SELECTOR, "uc-footer.footer")
            footer_shadow = get_shadow(driver, footer)
            accept_host = footer_shadow.find_element(By.CSS_SELECTOR, "uc-p-button.accept")
            accept_shadow = get_shadow(driver, accept_host)
            accept_button = accept_shadow.find_element(By.CSS_SELECTOR, "button.root")
            driver.execute_script("arguments[0].click()", accept_button)
            print(" Accept All clicked")
            delay()

            # 3. Open Burger Menu
            header = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
            shadow = header.shadow_root
            burger = shadow.find_element(By.CSS_SELECTOR, ".phn-burger-button.sc-phn-burger-button.hydrated")
            driver.execute_script("arguments[0].click()", burger)
            print(" Burger opened")
            delay()

            # 4. Click Porsche Shop
            header = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
            shadow = header.shadow_root

            porsche_shop = shadow.find_element(
                By.CSS_SELECTOR,
                "phn-p-button-pure[data-id='shop']"
            )

            driver.execute_script("arguments[0].click()", porsche_shop)
            print(" Porsche Shop clicked")
            delay()

            # 5. Sport & Fitness
            try:
                driver.find_element(By.XPATH, "//*[@id='6eIx5mVTCBDXX9l1gN0INy']/span").is_displayed()
                print(" Sport & Fitness button is displayed")
            except:
                print("Sport & Fitness button NOT displayed")
            el = driver.find_element(By.ID, "6eIx5mVTCBDXX9l1gN0INy")

            # JSON
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
            driver.execute_script("arguments[0].click()", el)

            print(" Sport & Fitness clicked")
            delay()
            print(driver.current_url)
            print("----------------------------------------------------------")

            apparel2 = driver.find_element(By.ID, "3sPh7Q3xNIMDVgMJ0ebWww")
            driver.execute_script("arguments[0].click()", apparel2)
            time.sleep(2)

            fil_but = driver.find_element(By.XPATH, '//*[@id="main-content"]/div[4]/div[2]/div[1]/sl-p-button')
            driver.execute_script("arguments[0].click()", fil_but)
            time.sleep(2)

            main2 = driver.find_element(By.CSS_SELECTOR, "main[id='main-content']")

            accordion = main2.find_element(By.CSS_SELECTOR,
                                           "sl-p-accordion[id='accordion-grossPriceFacetValue.amount']")
            shadow2 = accordion.shadow_root
            price_btn2 = shadow2.find_element(By.CSS_SELECTOR, "button[id='accordion-control']")

            driver.execute_script("arguments[0].click()", price_btn2)
            time.sleep(3)

            search = driver.find_element(By.XPATH, "//input[@id='visible-price-min']")
            search.clear()
            search.send_keys("123abc")
            print("No _abc_ printable")
            time.sleep(4)

    def test_TC_N_023_porsche(self):
            driver = self.driver

            # 1. Open Porsche
            driver.get("https://www.porsche.com/usa/")
            WebDriverWait(driver, 5).until(EC.url_contains("porsche.com"))
            delay()

            # 2. Accept Cookies (Shadow DOM)
            host = driver.find_element(By.CSS_SELECTOR, "uc-layer2")
            host_shadow = get_shadow(driver, host)
            modal = host_shadow.find_element(By.CSS_SELECTOR, "uc-p-modal.modal")
            footer = modal.find_element(By.CSS_SELECTOR, "uc-footer.footer")
            footer_shadow = get_shadow(driver, footer)
            accept_host = footer_shadow.find_element(By.CSS_SELECTOR, "uc-p-button.accept")
            accept_shadow = get_shadow(driver, accept_host)
            accept_button = accept_shadow.find_element(By.CSS_SELECTOR, "button.root")
            driver.execute_script("arguments[0].click()", accept_button)
            print(" Accept All clicked")
            delay()

            # 3. Open Burger Menu
            header = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
            shadow = header.shadow_root
            burger = shadow.find_element(By.CSS_SELECTOR, ".phn-burger-button.sc-phn-burger-button.hydrated")
            driver.execute_script("arguments[0].click()", burger)
            print(" Burger opened")
            delay()

            # 4. Click Porsche Shop
            header = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
            shadow = header.shadow_root

            porsche_shop = shadow.find_element(
                By.CSS_SELECTOR,
                "phn-p-button-pure[data-id='shop']"
            )

            driver.execute_script("arguments[0].click()", porsche_shop)
            print(" Porsche Shop clicked")
            delay()

            # 5. Sport & Fitness
            try:
                driver.find_element(By.XPATH, "//*[@id='6eIx5mVTCBDXX9l1gN0INy']/span").is_displayed()
                print(" Sport & Fitness button is displayed")
            except:
                print("Sport & Fitness button NOT displayed")
            el = driver.find_element(By.ID, "6eIx5mVTCBDXX9l1gN0INy")

            # JSON
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
            driver.execute_script("arguments[0].click()", el)

            print(" Sport & Fitness clicked")
            delay()
            print(driver.current_url)
            print("----------------------------------------------------------")

            header3 = driver.find_element(By.CSS_SELECTOR, 'header[class="_54nhml2"]')
            accessories = header3.find_element(By.CSS_SELECTOR,
                                               'li[class="jxyldu7 jxyldu6 jxyldu4"][data-node-id="16vl2X4FPGuTZTGZv9CBxV"]')
            asc_btn = accessories.find_element(By.CSS_SELECTOR,
                                               'a[class="_1m67wz30 _1m67wz32 _1m67wz33 _1m67wz36 jxylduj"][id="18SjaMTcwsLqjOwsIuNp6e"]')
            driver.execute_script("arguments[0].click()", asc_btn)
            time.sleep(2)
            print("______________________________________________________________")

            main3 = driver.find_element(By.CSS_SELECTOR, 'main[id="main-content"]')
            slp_button = main3.find_element(By.CSS_SELECTOR,
                                            'sl-p-button[class="hydrated"][data-testid="search-filter-open-button"]')
            shadow3 = slp_button.shadow_root
            filter3 = shadow3.find_element(By.CSS_SELECTOR,
                                           'button[aria-haspopup="dialog"][class="root"][type="button"]')
            driver.execute_script("arguments[0].click()", filter3)
            time.sleep(2)

            main3 = driver.find_element(By.CSS_SELECTOR, "main[id='main-content']")

            accordion3 = main3.find_element(By.CSS_SELECTOR,
                                            "sl-p-accordion[id='accordion-grossPriceFacetValue.amount']")
            shadow3 = accordion3.shadow_root
            price_btn3 = shadow3.find_element(By.CSS_SELECTOR, "button[id='accordion-control']")

            driver.execute_script("arguments[0].click()", price_btn3)
            time.sleep(3)

            search = driver.find_element(By.XPATH, "//input[@id='visible-price-min']")
            search.clear()
            search.send_keys("$$&&##")
            print("No _$$&&##_ printable")
            time.sleep(4)

    def test_TC_N_024_porsche(self):
            driver = self.driver

            # 1. Open Porsche
            driver.get("https://www.porsche.com/usa/")
            WebDriverWait(driver, 5).until(EC.url_contains("porsche.com"))
            delay()

            # 2. Accept Cookies (Shadow DOM)
            host = driver.find_element(By.CSS_SELECTOR, "uc-layer2")
            host_shadow = get_shadow(driver, host)
            modal = host_shadow.find_element(By.CSS_SELECTOR, "uc-p-modal.modal")
            footer = modal.find_element(By.CSS_SELECTOR, "uc-footer.footer")
            footer_shadow = get_shadow(driver, footer)
            accept_host = footer_shadow.find_element(By.CSS_SELECTOR, "uc-p-button.accept")
            accept_shadow = get_shadow(driver, accept_host)
            accept_button = accept_shadow.find_element(By.CSS_SELECTOR, "button.root")
            driver.execute_script("arguments[0].click()", accept_button)
            print(" Accept All clicked")
            delay()

            # 3. Open Burger Menu
            header = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
            shadow = header.shadow_root
            burger = shadow.find_element(By.CSS_SELECTOR, ".phn-burger-button.sc-phn-burger-button.hydrated")
            driver.execute_script("arguments[0].click()", burger)
            print(" Burger opened")
            delay()

            # 4. Click Porsche Shop
            header = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
            shadow = header.shadow_root

            porsche_shop = shadow.find_element(
                By.CSS_SELECTOR,
                "phn-p-button-pure[data-id='shop']"
            )

            driver.execute_script("arguments[0].click()", porsche_shop)
            print(" Porsche Shop clicked")
            delay()

            # 5. Sport & Fitness
            try:
                driver.find_element(By.XPATH, "//*[@id='6eIx5mVTCBDXX9l1gN0INy']/span").is_displayed()
                print(" Sport & Fitness button is displayed")
            except:
                print("Sport & Fitness button NOT displayed")
            el = driver.find_element(By.ID, "6eIx5mVTCBDXX9l1gN0INy")

            # JSON
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
            driver.execute_script("arguments[0].click()", el)

            print(" Sport & Fitness clicked")
            delay()
            print(driver.current_url)
            print("----------------------------------------------------------")
            # Watches
            header4 = driver.find_element(By.CSS_SELECTOR, 'header[class="_54nhml2"]')
            watches4 = header4.find_element(By.CSS_SELECTOR, 'a[id="75b4AeyrMgIKwKd6SGdNUH"]')
            driver.execute_script("arguments[0].click()", watches4)
            time.sleep(3)

            main4 = driver.find_element(By.CSS_SELECTOR, 'main[id="main-content"]')
            slp_button = main4.find_element(By.CSS_SELECTOR,
                                            'sl-p-button[class="hydrated"][data-testid="search-filter-open-button"]')
            shadow4 = slp_button.shadow_root
            filter4 = shadow4.find_element(By.CSS_SELECTOR,
                                           'button[aria-haspopup="dialog"][class="root"][type="button"]')
            driver.execute_script("arguments[0].click()", filter4)
            time.sleep(2)

            main4 = driver.find_element(By.CSS_SELECTOR, "main[id='main-content']")

            accordion4 = main4.find_element(By.CSS_SELECTOR,
                                            "sl-p-accordion[id='accordion-grossPriceFacetValue.amount']")
            shadow4 = accordion4.shadow_root
            price_btn4 = shadow4.find_element(By.CSS_SELECTOR, "button[id='accordion-control']")

            driver.execute_script("arguments[0].click()", price_btn4)
            time.sleep(3)

            search = driver.find_element(By.XPATH, "//input[@id='visible-price-min']")
            search.clear()
            search.send_keys("$$&&##")
            print("No _$$&&##_ printable")
            time.sleep(4)

    def test_TC_N_025_porsche(self):
            driver = self.driver

            # 1. Open Porsche
            driver.get("https://www.porsche.com/usa/")
            WebDriverWait(driver, 5).until(EC.url_contains("porsche.com"))
            delay()

            # 2. Accept Cookies (Shadow DOM)
            host = driver.find_element(By.CSS_SELECTOR, "uc-layer2")
            host_shadow = get_shadow(driver, host)
            modal = host_shadow.find_element(By.CSS_SELECTOR, "uc-p-modal.modal")
            footer = modal.find_element(By.CSS_SELECTOR, "uc-footer.footer")
            footer_shadow = get_shadow(driver, footer)
            accept_host = footer_shadow.find_element(By.CSS_SELECTOR, "uc-p-button.accept")
            accept_shadow = get_shadow(driver, accept_host)
            accept_button = accept_shadow.find_element(By.CSS_SELECTOR, "button.root")
            driver.execute_script("arguments[0].click()", accept_button)
            print(" Accept All clicked")
            delay()

            # 3. Open Burger Menu
            header = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
            shadow = header.shadow_root
            burger = shadow.find_element(By.CSS_SELECTOR, ".phn-burger-button.sc-phn-burger-button.hydrated")
            driver.execute_script("arguments[0].click()", burger)
            print(" Burger opened")
            delay()

            # 4. Click Porsche Shop
            header = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
            shadow = header.shadow_root

            porsche_shop = shadow.find_element(
                By.CSS_SELECTOR,
                "phn-p-button-pure[data-id='shop']"
            )

            driver.execute_script("arguments[0].click()", porsche_shop)
            print(" Porsche Shop clicked")
            delay()

            # 5. Sport & Fitness
            try:
                driver.find_element(By.XPATH, "//*[@id='6eIx5mVTCBDXX9l1gN0INy']/span").is_displayed()
                print(" Sport & Fitness button is displayed")
            except:
                print("Sport & Fitness button NOT displayed")
            el = driver.find_element(By.ID, "6eIx5mVTCBDXX9l1gN0INy")

            # JSON
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
            driver.execute_script("arguments[0].click()", el)

            print(" Sport & Fitness clicked")
            delay()
            print(driver.current_url)
            print("----------------------------------------------------------")

            header5 = driver.find_element(By.CSS_SELECTOR, 'header[class="_54nhml2"]')
            bags5 = header5.find_element(By.CSS_SELECTOR,
                                         'a[class="_1m67wz30 _1m67wz32 _1m67wz33 _1m67wz36 jxylduj"][id="2PfwsCxbcfT9UvGeTcVmTK"]')
            driver.execute_script("arguments[0].click()", bags5)
            time.sleep(2)

            main5 = driver.find_element(By.CSS_SELECTOR, 'main[id="main-content"]')
            slp5 = main5.find_element(By.CSS_SELECTOR,
                                      'sl-p-button[data-testid="search-filter-open-button"][class="hydrated"]')
            shadow5 = slp5.shadow_root
            filter5 = shadow5.find_element(By.CSS_SELECTOR, 'button[aria-haspopup="dialog"][class="root"]')
            driver.execute_script("arguments[0].click()", filter5)
            time.sleep(2)

            main5 = driver.find_element(By.CSS_SELECTOR, "main[id='main-content']")

            accordion5 = main5.find_element(By.CSS_SELECTOR,
                                            "sl-p-accordion[id='accordion-grossPriceFacetValue.amount']")
            shadow5 = accordion5.shadow_root
            price_btn5 = shadow5.find_element(By.CSS_SELECTOR, "button[id='accordion-control']")

            driver.execute_script("arguments[0].click()", price_btn5)
            time.sleep(3)

            search = driver.find_element(By.XPATH, "//input[@id='visible-price-min']")
            search.clear()
            search.send_keys("ASDzxc")
            print("No _ASDzxc_ printable")
            time.sleep(4)

class FirefoxDriverManager(unittest.TestCase):
    def setUp(self):
            options = FF_Options()
            # options.set_preference("dom.webdriver.enabled", False)
            # options.set_preference("useAutomationExtension", False)
            options.add_argument("--disable-blink-features=AutomationControlled")
            self.driver = webdriver.Firefox(options=options, service=FirefoxService(GeckoDriverManager().install()))
            self.driver.maximize_window()

    def test_TC_N_021_porsche(self):
            driver = self.driver

            # 1. Open Porsche
            driver.get("https://www.porsche.com/usa/")
            WebDriverWait(driver, 5).until(EC.url_contains("porsche.com"))
            delay()

            # 2. Accept Cookies (Shadow DOM)
            host = driver.find_element(By.CSS_SELECTOR, "uc-layer2")
            host_shadow = get_shadow(driver, host)
            modal = host_shadow.find_element(By.CSS_SELECTOR, "uc-p-modal.modal")
            footer = modal.find_element(By.CSS_SELECTOR, "uc-footer.footer")
            footer_shadow = get_shadow(driver, footer)
            accept_host = footer_shadow.find_element(By.CSS_SELECTOR, "uc-p-button.accept")
            accept_shadow = get_shadow(driver, accept_host)
            accept_button = accept_shadow.find_element(By.CSS_SELECTOR, "button.root")
            driver.execute_script("arguments[0].click()", accept_button)
            print(" Accept All clicked")
            delay()

            # 3. Open Burger Menu
            header = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
            shadow = header.shadow_root
            burger = shadow.find_element(By.CSS_SELECTOR, ".phn-burger-button.sc-phn-burger-button.hydrated")
            driver.execute_script("arguments[0].click()", burger)
            print(" Burger opened")
            delay()

            # 4. Click Porsche Shop
            header = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
            shadow = header.shadow_root

            porsche_shop = shadow.find_element(
                By.CSS_SELECTOR,
                "phn-p-button-pure[data-id='shop']"
            )

            driver.execute_script("arguments[0].click()", porsche_shop)
            print(" Porsche Shop clicked")
            delay()

            # 5. Sport & Fitness
            try:
                driver.find_element(By.XPATH, "//*[@id='6eIx5mVTCBDXX9l1gN0INy']/span").is_displayed()
                print(" Sport & Fitness button is displayed")
            except:
                print("Sport & Fitness button NOT displayed")
            el = driver.find_element(By.ID, "6eIx5mVTCBDXX9l1gN0INy")

            # JSON
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
            driver.execute_script("arguments[0].click()", el)

            print(" Sport & Fitness clicked")
            delay()
            print(driver.current_url)
            # filter
            driver.find_element(By.XPATH, '//*[@id="main-content"]/div[4]/div[2]/div[1]/sl-p-button').click()

            time.sleep(3)

            # Price
            main1 = driver.find_element(By.CSS_SELECTOR, "main[id='main-content']")

            accordion = main1.find_element(By.CSS_SELECTOR,
                                           "sl-p-accordion[id='accordion-grossPriceFacetValue.amount']")
            shadow1 = accordion.shadow_root
            price_btn = shadow1.find_element(By.CSS_SELECTOR, "button[id='accordion-control']")

            driver.execute_script("arguments[0].click()", price_btn)
            time.sleep(3)

            search = driver.find_element(By.XPATH, "//input[@id='visible-price-min']")
            search.clear()
            search.send_keys("123abc")
            print("No _abc_ printable")
            time.sleep(4)

    def test_TC_N_022_porsche(self):
            driver = self.driver

            # 1. Open Porsche
            driver.get("https://www.porsche.com/usa/")
            WebDriverWait(driver, 5).until(EC.url_contains("porsche.com"))
            delay()

            # 2. Accept Cookies (Shadow DOM)
            host = driver.find_element(By.CSS_SELECTOR, "uc-layer2")
            host_shadow = get_shadow(driver, host)
            modal = host_shadow.find_element(By.CSS_SELECTOR, "uc-p-modal.modal")
            footer = modal.find_element(By.CSS_SELECTOR, "uc-footer.footer")
            footer_shadow = get_shadow(driver, footer)
            accept_host = footer_shadow.find_element(By.CSS_SELECTOR, "uc-p-button.accept")
            accept_shadow = get_shadow(driver, accept_host)
            accept_button = accept_shadow.find_element(By.CSS_SELECTOR, "button.root")
            driver.execute_script("arguments[0].click()", accept_button)
            print(" Accept All clicked")
            delay()

            # 3. Open Burger Menu
            header = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
            shadow = header.shadow_root
            burger = shadow.find_element(By.CSS_SELECTOR, ".phn-burger-button.sc-phn-burger-button.hydrated")
            driver.execute_script("arguments[0].click()", burger)
            print(" Burger opened")
            delay()

            # 4. Click Porsche Shop
            header = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
            shadow = header.shadow_root

            porsche_shop = shadow.find_element(
                By.CSS_SELECTOR,
                "phn-p-button-pure[data-id='shop']"
            )

            driver.execute_script("arguments[0].click()", porsche_shop)
            print(" Porsche Shop clicked")
            delay()

            # 5. Sport & Fitness
            try:
                driver.find_element(By.XPATH, "//*[@id='6eIx5mVTCBDXX9l1gN0INy']/span").is_displayed()
                print(" Sport & Fitness button is displayed")
            except:
                print("Sport & Fitness button NOT displayed")
            el = driver.find_element(By.ID, "6eIx5mVTCBDXX9l1gN0INy")

            # JSON
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
            driver.execute_script("arguments[0].click()", el)

            print(" Sport & Fitness clicked")
            delay()
            print(driver.current_url)
            print("----------------------------------------------------------")

            apparel2 = driver.find_element(By.ID, "3sPh7Q3xNIMDVgMJ0ebWww")
            driver.execute_script("arguments[0].click()", apparel2)
            time.sleep(2)

            fil_but = driver.find_element(By.XPATH, '//*[@id="main-content"]/div[4]/div[2]/div[1]/sl-p-button')
            driver.execute_script("arguments[0].click()", fil_but)
            time.sleep(2)

            main2 = driver.find_element(By.CSS_SELECTOR, "main[id='main-content']")

            accordion = main2.find_element(By.CSS_SELECTOR,
                                           "sl-p-accordion[id='accordion-grossPriceFacetValue.amount']")
            shadow2 = accordion.shadow_root
            price_btn2 = shadow2.find_element(By.CSS_SELECTOR, "button[id='accordion-control']")

            driver.execute_script("arguments[0].click()", price_btn2)
            time.sleep(3)

            search = driver.find_element(By.XPATH, "//input[@id='visible-price-min']")
            search.clear()
            search.send_keys("123abc")
            print("No _abc_ printable")
            time.sleep(4)

    def test_TC_N_023_porsche(self):
            driver = self.driver

            # 1. Open Porsche
            driver.get("https://www.porsche.com/usa/")
            WebDriverWait(driver, 5).until(EC.url_contains("porsche.com"))
            delay()

            # 2. Accept Cookies (Shadow DOM)
            host = driver.find_element(By.CSS_SELECTOR, "uc-layer2")
            host_shadow = get_shadow(driver, host)
            modal = host_shadow.find_element(By.CSS_SELECTOR, "uc-p-modal.modal")
            footer = modal.find_element(By.CSS_SELECTOR, "uc-footer.footer")
            footer_shadow = get_shadow(driver, footer)
            accept_host = footer_shadow.find_element(By.CSS_SELECTOR, "uc-p-button.accept")
            accept_shadow = get_shadow(driver, accept_host)
            accept_button = accept_shadow.find_element(By.CSS_SELECTOR, "button.root")
            driver.execute_script("arguments[0].click()", accept_button)
            print(" Accept All clicked")
            delay()

            # 3. Open Burger Menu
            header = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
            shadow = header.shadow_root
            burger = shadow.find_element(By.CSS_SELECTOR, ".phn-burger-button.sc-phn-burger-button.hydrated")
            driver.execute_script("arguments[0].click()", burger)
            print(" Burger opened")
            delay()

            # 4. Click Porsche Shop
            header = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
            shadow = header.shadow_root

            porsche_shop = shadow.find_element(
                By.CSS_SELECTOR,
                "phn-p-button-pure[data-id='shop']"
            )

            driver.execute_script("arguments[0].click()", porsche_shop)
            print(" Porsche Shop clicked")
            delay()

            # 5. Sport & Fitness
            try:
                driver.find_element(By.XPATH, "//*[@id='6eIx5mVTCBDXX9l1gN0INy']/span").is_displayed()
                print(" Sport & Fitness button is displayed")
            except:
                print("Sport & Fitness button NOT displayed")
            el = driver.find_element(By.ID, "6eIx5mVTCBDXX9l1gN0INy")

            # JSON
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
            driver.execute_script("arguments[0].click()", el)

            print(" Sport & Fitness clicked")
            delay()
            print(driver.current_url)
            print("----------------------------------------------------------")

            header3 = driver.find_element(By.CSS_SELECTOR, 'header[class="_54nhml2"]')
            accessories = header3.find_element(By.CSS_SELECTOR,
                                               'li[class="jxyldu7 jxyldu6 jxyldu4"][data-node-id="16vl2X4FPGuTZTGZv9CBxV"]')
            asc_btn = accessories.find_element(By.CSS_SELECTOR,
                                               'a[class="_1m67wz30 _1m67wz32 _1m67wz33 _1m67wz36 jxylduj"][id="18SjaMTcwsLqjOwsIuNp6e"]')
            driver.execute_script("arguments[0].click()", asc_btn)
            time.sleep(2)
            print("______________________________________________________________")

            main3 = driver.find_element(By.CSS_SELECTOR, 'main[id="main-content"]')
            slp_button = main3.find_element(By.CSS_SELECTOR,
                                            'sl-p-button[class="hydrated"][data-testid="search-filter-open-button"]')
            shadow3 = slp_button.shadow_root
            filter3 = shadow3.find_element(By.CSS_SELECTOR,
                                           'button[aria-haspopup="dialog"][class="root"][type="button"]')
            driver.execute_script("arguments[0].click()", filter3)
            time.sleep(2)

            main3 = driver.find_element(By.CSS_SELECTOR, "main[id='main-content']")

            accordion3 = main3.find_element(By.CSS_SELECTOR,
                                            "sl-p-accordion[id='accordion-grossPriceFacetValue.amount']")
            shadow3 = accordion3.shadow_root
            price_btn3 = shadow3.find_element(By.CSS_SELECTOR, "button[id='accordion-control']")

            driver.execute_script("arguments[0].click()", price_btn3)
            time.sleep(3)

            search = driver.find_element(By.XPATH, "//input[@id='visible-price-min']")
            search.clear()
            search.send_keys("$$&&##")
            print("No _$$&&##_ printable")
            time.sleep(4)

    def test_TC_N_024_porsche(self):
            driver = self.driver

            # 1. Open Porsche
            driver.get("https://www.porsche.com/usa/")
            WebDriverWait(driver, 5).until(EC.url_contains("porsche.com"))
            delay()

            # 2. Accept Cookies (Shadow DOM)
            host = driver.find_element(By.CSS_SELECTOR, "uc-layer2")
            host_shadow = get_shadow(driver, host)
            modal = host_shadow.find_element(By.CSS_SELECTOR, "uc-p-modal.modal")
            footer = modal.find_element(By.CSS_SELECTOR, "uc-footer.footer")
            footer_shadow = get_shadow(driver, footer)
            accept_host = footer_shadow.find_element(By.CSS_SELECTOR, "uc-p-button.accept")
            accept_shadow = get_shadow(driver, accept_host)
            accept_button = accept_shadow.find_element(By.CSS_SELECTOR, "button.root")
            driver.execute_script("arguments[0].click()", accept_button)
            print(" Accept All clicked")
            delay()

            # 3. Open Burger Menu
            header = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
            shadow = header.shadow_root
            burger = shadow.find_element(By.CSS_SELECTOR, ".phn-burger-button.sc-phn-burger-button.hydrated")
            driver.execute_script("arguments[0].click()", burger)
            print(" Burger opened")
            delay()

            # 4. Click Porsche Shop
            header = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
            shadow = header.shadow_root

            porsche_shop = shadow.find_element(
                By.CSS_SELECTOR,
                "phn-p-button-pure[data-id='shop']"
            )

            driver.execute_script("arguments[0].click()", porsche_shop)
            print(" Porsche Shop clicked")
            delay()

            # 5. Sport & Fitness
            try:
                driver.find_element(By.XPATH, "//*[@id='6eIx5mVTCBDXX9l1gN0INy']/span").is_displayed()
                print(" Sport & Fitness button is displayed")
            except:
                print("Sport & Fitness button NOT displayed")
            el = driver.find_element(By.ID, "6eIx5mVTCBDXX9l1gN0INy")

            # JSON
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
            driver.execute_script("arguments[0].click()", el)

            print(" Sport & Fitness clicked")
            delay()
            print(driver.current_url)
            print("----------------------------------------------------------")
            # Watches
            header4 = driver.find_element(By.CSS_SELECTOR, 'header[class="_54nhml2"]')
            watches4 = header4.find_element(By.CSS_SELECTOR, 'a[id="75b4AeyrMgIKwKd6SGdNUH"]')
            driver.execute_script("arguments[0].click()", watches4)
            time.sleep(3)

            main4 = driver.find_element(By.CSS_SELECTOR, 'main[id="main-content"]')
            slp_button = main4.find_element(By.CSS_SELECTOR,
                                            'sl-p-button[class="hydrated"][data-testid="search-filter-open-button"]')
            shadow4 = slp_button.shadow_root
            filter4 = shadow4.find_element(By.CSS_SELECTOR,
                                           'button[aria-haspopup="dialog"][class="root"][type="button"]')
            driver.execute_script("arguments[0].click()", filter4)
            time.sleep(2)

            main4 = driver.find_element(By.CSS_SELECTOR, "main[id='main-content']")

            accordion4 = main4.find_element(By.CSS_SELECTOR,
                                            "sl-p-accordion[id='accordion-grossPriceFacetValue.amount']")
            shadow4 = accordion4.shadow_root
            price_btn4 = shadow4.find_element(By.CSS_SELECTOR, "button[id='accordion-control']")

            driver.execute_script("arguments[0].click()", price_btn4)
            time.sleep(3)

            search = driver.find_element(By.XPATH, "//input[@id='visible-price-min']")
            search.clear()
            search.send_keys("$$&&##")
            print("No _$$&&##_ printable")
            time.sleep(4)

    def test_TC_N_025_porsche(self):
            driver = self.driver

            # 1. Open Porsche
            driver.get("https://www.porsche.com/usa/")
            WebDriverWait(driver, 5).until(EC.url_contains("porsche.com"))
            delay()

            # 2. Accept Cookies (Shadow DOM)
            host = driver.find_element(By.CSS_SELECTOR, "uc-layer2")
            host_shadow = get_shadow(driver, host)
            modal = host_shadow.find_element(By.CSS_SELECTOR, "uc-p-modal.modal")
            footer = modal.find_element(By.CSS_SELECTOR, "uc-footer.footer")
            footer_shadow = get_shadow(driver, footer)
            accept_host = footer_shadow.find_element(By.CSS_SELECTOR, "uc-p-button.accept")
            accept_shadow = get_shadow(driver, accept_host)
            accept_button = accept_shadow.find_element(By.CSS_SELECTOR, "button.root")
            driver.execute_script("arguments[0].click()", accept_button)
            print(" Accept All clicked")
            delay()

            # 3. Open Burger Menu
            header = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
            shadow = header.shadow_root
            burger = shadow.find_element(By.CSS_SELECTOR, ".phn-burger-button.sc-phn-burger-button.hydrated")
            driver.execute_script("arguments[0].click()", burger)
            print(" Burger opened")
            delay()

            # 4. Click Porsche Shop
            header = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
            shadow = header.shadow_root

            porsche_shop = shadow.find_element(
                By.CSS_SELECTOR,
                "phn-p-button-pure[data-id='shop']"
            )

            driver.execute_script("arguments[0].click()", porsche_shop)
            print(" Porsche Shop clicked")
            delay()

            # 5. Sport & Fitness
            try:
                driver.find_element(By.XPATH, "//*[@id='6eIx5mVTCBDXX9l1gN0INy']/span").is_displayed()
                print(" Sport & Fitness button is displayed")
            except:
                print("Sport & Fitness button NOT displayed")
            el = driver.find_element(By.ID, "6eIx5mVTCBDXX9l1gN0INy")

            # JSON
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
            driver.execute_script("arguments[0].click()", el)

            print(" Sport & Fitness clicked")
            delay()
            print(driver.current_url)
            print("----------------------------------------------------------")

            header5 = driver.find_element(By.CSS_SELECTOR, 'header[class="_54nhml2"]')
            bags5 = header5.find_element(By.CSS_SELECTOR,
                                         'a[class="_1m67wz30 _1m67wz32 _1m67wz33 _1m67wz36 jxylduj"][id="2PfwsCxbcfT9UvGeTcVmTK"]')
            driver.execute_script("arguments[0].click()", bags5)
            time.sleep(2)

            main5 = driver.find_element(By.CSS_SELECTOR, 'main[id="main-content"]')
            slp5 = main5.find_element(By.CSS_SELECTOR,
                                      'sl-p-button[data-testid="search-filter-open-button"][class="hydrated"]')
            shadow5 = slp5.shadow_root
            filter5 = shadow5.find_element(By.CSS_SELECTOR, 'button[aria-haspopup="dialog"][class="root"]')
            driver.execute_script("arguments[0].click()", filter5)
            time.sleep(2)

            main5 = driver.find_element(By.CSS_SELECTOR, "main[id='main-content']")

            accordion5 = main5.find_element(By.CSS_SELECTOR,
                                            "sl-p-accordion[id='accordion-grossPriceFacetValue.amount']")
            shadow5 = accordion5.shadow_root
            price_btn5 = shadow5.find_element(By.CSS_SELECTOR, "button[id='accordion-control']")

            driver.execute_script("arguments[0].click()", price_btn5)
            time.sleep(3)

            search = driver.find_element(By.XPATH, "//input[@id='visible-price-min']")
            search.clear()
            search.send_keys("ASDzxc")
            print("No _ASDzxc_ printable")
            time.sleep(4)

    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports'))