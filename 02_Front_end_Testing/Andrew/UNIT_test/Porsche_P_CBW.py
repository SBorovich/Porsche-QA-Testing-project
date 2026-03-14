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
#import AllureReports


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

    def test_TC_P_021_porsche(self):
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


    def test_TC_P_022_porsche(self):
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

    def test_TC_P_023_porsche(self):
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


        try:
            driver.find_element(By.XPATH, "//*[@id='main-content']/div[2]/h1").is_displayed()
            print("logo SPORT & Fitness  displayed")
        except:
            print("logo SPORT & Fitness  NOT displayed")

    def test_TC_P_024_porsche(self):
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


        try:
            driver.find_element(By.XPATH, "//*[@id='main-content']/div[2]/h1").is_displayed()
            print("logo SPORT & Fitness  displayed")
        except:
            print("logo SPORT & Fitness  NOT displayed")

        try:
            driver.find_element(By.XPATH, "/html/body/header/div/div[1]/nav/div[1]/div/div/div/div/div/div/div/"
                                          "div[3]/div[1]/div[1]")
            print("icon Search is displayed")
        except:
            print("icon Search NOT displayed")
        try:
            driver.find_element(By.XPATH, "/html/body/header/div/div[1]/nav/div[1]/div/div/div/div/div/div"
                                          "/div/div[3]/div[1]/div[3]")
            print("icon Shopping cart displayed")
        except:
            print("icon Shopping cart NOT displayed")
    def test_TC_P_025_porsche(self):
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

        try:
            driver.find_element(By.XPATH, "//*[@id='main-content']/div[2]/h1").is_displayed()
            print("logo SPORT & Fitness  displayed")
        except:
            print("logo SPORT & Fitness  NOT displayed")

        try:
            driver.find_element(By.XPATH, "/html/body/header/div/div[1]/nav/div[1]/div/div/div/div/div/div/div/"
                                          "div[3]/div[1]/div[1]")
            print("icon Search is displayed")
        except:
            print("icon Search NOT displayed")
        try:
            driver.find_element(By.XPATH, "/html/body/header/div/div[1]/nav/div[1]/div/div/div/div/div/div"
                                          "/div/div[3]/div[1]/div[3]")
            print("icon Shopping cart displayed")
        except:
            print("icon Shopping cart NOT displayed")

        try:
            driver.find_element(By.XPATH, "/html/body/header/div/div[1]/nav/div[1]/div/div/div/"
                                          "div/div/div/div/div[1]")
            print("buton menu displayed")
        except:
            print("buton menu NOT displayed")

class EdgeDriverManager(unittest.TestCase):
    def setUp(self):
            os.environ["SE_DRIVER_MIRROR_URL"] = "https://msedgedriver.microsoft.com"
            options = Edge_Options()
            options.add_argument("--disable-blink-features=AutomationControlled")
            self.driver = webdriver.Edge(options=options)
            self.driver.maximize_window()

    def test_TC_P_021_porsche(self):
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

    def test_TC_P_022_porsche(self):
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

    def test_TC_P_023_porsche(self):
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

            try:
                driver.find_element(By.XPATH, "//*[@id='main-content']/div[2]/h1").is_displayed()
                print("logo SPORT & Fitness  displayed")
            except:
                print("logo SPORT & Fitness  NOT displayed")

    def test_TC_P_024_porsche(self):
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

            try:
                driver.find_element(By.XPATH, "//*[@id='main-content']/div[2]/h1").is_displayed()
                print("logo SPORT & Fitness  displayed")
            except:
                print("logo SPORT & Fitness  NOT displayed")

            try:
                driver.find_element(By.XPATH, "/html/body/header/div/div[1]/nav/div[1]/div/div/div/div/div/div/div/"
                                              "div[3]/div[1]/div[1]")
                print("icon Search is displayed")
            except:
                print("icon Search NOT displayed")
            try:
                driver.find_element(By.XPATH, "/html/body/header/div/div[1]/nav/div[1]/div/div/div/div/div/div"
                                              "/div/div[3]/div[1]/div[3]")
                print("icon Shopping cart displayed")
            except:
                print("icon Shopping cart NOT displayed")

    def test_TC_P_025_porsche(self):
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

            try:
                driver.find_element(By.XPATH, "//*[@id='main-content']/div[2]/h1").is_displayed()
                print("logo SPORT & Fitness  displayed")
            except:
                print("logo SPORT & Fitness  NOT displayed")

            try:
                driver.find_element(By.XPATH, "/html/body/header/div/div[1]/nav/div[1]/div/div/div/div/div/div/div/"
                                              "div[3]/div[1]/div[1]")
                print("icon Search is displayed")
            except:
                print("icon Search NOT displayed")
            try:
                driver.find_element(By.XPATH, "/html/body/header/div/div[1]/nav/div[1]/div/div/div/div/div/div"
                                              "/div/div[3]/div[1]/div[3]")
                print("icon Shopping cart displayed")
            except:
                print("icon Shopping cart NOT displayed")

            try:
                driver.find_element(By.XPATH, "/html/body/header/div/div[1]/nav/div[1]/div/div/div/"
                                              "div/div/div/div/div[1]")
                print("buton menu displayed")
            except:
                print("buton menu NOT displayed")

class FirefoxDriverManager(unittest.TestCase):
    def setUp(self):
            options = FF_Options()
            # options.set_preference("dom.webdriver.enabled", False)
            # options.set_preference("useAutomationExtension", False)
            options.add_argument("--disable-blink-features=AutomationControlled")
            self.driver = webdriver.Firefox(options=options, service=FirefoxService(GeckoDriverManager().install()))
            self.driver.maximize_window()

    def test_TC_P_021_porsche(self):
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

    def test_TC_P_022_porsche(self):
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

    def test_TC_P_023_porsche(self):
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

            try:
                driver.find_element(By.XPATH, "//*[@id='main-content']/div[2]/h1").is_displayed()
                print("logo SPORT & Fitness  displayed")
            except:
                print("logo SPORT & Fitness  NOT displayed")

    def test_TC_P_024_porsche(self):
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

            try:
                driver.find_element(By.XPATH, "//*[@id='main-content']/div[2]/h1").is_displayed()
                print("logo SPORT & Fitness  displayed")
            except:
                print("logo SPORT & Fitness  NOT displayed")

            try:
                driver.find_element(By.XPATH, "/html/body/header/div/div[1]/nav/div[1]/div/div/div/div/div/div/div/"
                                              "div[3]/div[1]/div[1]")
                print("icon Search is displayed")
            except:
                print("icon Search NOT displayed")
            try:
                driver.find_element(By.XPATH, "/html/body/header/div/div[1]/nav/div[1]/div/div/div/div/div/div"
                                              "/div/div[3]/div[1]/div[3]")
                print("icon Shopping cart displayed")
            except:
                print("icon Shopping cart NOT displayed")

    def test_TC_P_025_porsche(self):
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

            try:
                driver.find_element(By.XPATH, "//*[@id='main-content']/div[2]/h1").is_displayed()
                print("logo SPORT & Fitness  displayed")
            except:
                print("logo SPORT & Fitness  NOT displayed")

            try:
                driver.find_element(By.XPATH, "/html/body/header/div/div[1]/nav/div[1]/div/div/div/div/div/div/div/"
                                              "div[3]/div[1]/div[1]")
                print("icon Search is displayed")
            except:
                print("icon Search NOT displayed")
            try:
                driver.find_element(By.XPATH, "/html/body/header/div/div[1]/nav/div[1]/div/div/div/div/div/div"
                                              "/div/div[3]/div[1]/div[3]")
                print("icon Shopping cart displayed")
            except:
                print("icon Shopping cart NOT displayed")

            try:
                driver.find_element(By.XPATH, "/html/body/header/div/div[1]/nav/div[1]/div/div/div/"
                                              "div/div/div/div/div[1]")
                print("buton menu displayed")
            except:
                print("buton menu NOT displayed")




    def tearDown(self):
        self.driver.quit()
#if __name__ == "__main__":
 #   unittest.main(AllureReports)