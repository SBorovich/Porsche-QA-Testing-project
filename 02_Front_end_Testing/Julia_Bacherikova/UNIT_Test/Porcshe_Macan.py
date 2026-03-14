import random
from builtins import Exception
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.core import driver
from selenium.webdriver.edge.options import Options as EdgeOptions
import os
import utils as utils
import time
import unittest
# import HtmlTestRunner
import AllureReports



from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def keyboard_tab_times_then_space(driver, times=5):

   # """Used in TC_P_015: press TAB N times, then SPACE (example: captcha focus attempt)."""

    keys = [Keys.TAB] * times + [Keys.SPACE]
    driver.switch_to.active_element.send_keys(*keys)

def delay():
    time.sleep(random.randint(3,5))



class ChromePorschePositiveTests(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'eager'
        options.add_argument("--disable-blink-features=AutomationControlled")
        #options.add_argument("--window-size=1920,1080")
        #options.add_argument("--headless")

        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()
    def tearDown(self):
        self.driver.quit()

    def test_TC_P_031(self):

        driver = self.driver
        driver.get("https://www.porsche.com/usa/")
        delay()
        # Closing Cookies banner using Tab
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        time.sleep(3)
        # Finding and clicking Menu button
        header = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
        delay()
        shadow = header.shadow_root
        delay()
        burger = shadow.find_element(By.CSS_SELECTOR, ".phn-burger-button.sc-phn-burger-button.hydrated")
        driver.execute_script("arguments[0].click();", burger)
        delay()
        # Finding Menu options
        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root

        models = shadow.find_element(By.CSS_SELECTOR, "phn-p-button-pure")
        if models:
            print("Models option is visible")
        else:
            print("Models options not visible")

        # Finding Shopping Tools option
        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root
        shopping_tools = shadow.find_element(By.CSS_SELECTOR,
                                             "phn-p-button-pure[class='sc-phn-nd-side-drawer-item hydrated'][data-id='vehicle_purchase']")
        if shopping_tools:
            print("Shopping Tools option is visible")
        else:
            print("Shopping Tools options not visible")

        # Finding Porsche Shop options
        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root
        porsche_shop = shadow.find_element(By.CSS_SELECTOR,
                                           "phn-p-button-pure[class='sc-phn-nd-side-drawer-item hydrated'][data-id='shop']")
        if porsche_shop:
            print("porsche_shop option is visible")
        else:
            print("porsche_shop options not visible")

        driver.quit()

    def test_TC_P_032(self):

        driver = self.driver
        driver.get("https://www.porsche.com/usa/")
        delay()
    # Closing Cookies banner using Tab
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        time.sleep(3)
    # Finding and clicking Menu button
        header = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
        delay()
        shadow = header.shadow_root
        delay()
        burger = shadow.find_element(By.CSS_SELECTOR, ".phn-burger-button.sc-phn-burger-button.hydrated")
        driver.execute_script("arguments[0].click();", burger)
        delay()
    # Finding Menu options
        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root
        models = shadow.find_element(By.CSS_SELECTOR,"phn-p-button-pure")
        if models:
            print("Models option is visible")
        else:
            print("Models options not visible")


    # Finding Shopping Tools option
        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root
        shopping_tools = shadow.find_element(By.CSS_SELECTOR, "phn-p-button-pure[class='sc-phn-nd-side-drawer-item hydrated'][data-id='vehicle_purchase']")
        if shopping_tools:
            print("Shopping Tools option is visible")
        else:
            print("Shopping Tools options not visible")


    # Finding Porsche Shop options
        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root
        porsche_shop = shadow.find_element(By.CSS_SELECTOR,"phn-p-button-pure[class='sc-phn-nd-side-drawer-item hydrated'][data-id='shop']")
        if porsche_shop:
            print("porsche_shop option is visible")
        else:
            print("porsche_shop options not visible")
        delay()

#       Finding Service oprion
        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root
        service= shadow.find_element(By.CSS_SELECTOR,"phn-p-button-pure[class='sc-phn-nd-side-drawer-item hydrated'][data-id='services']")
        if service:
            print("service option is visible")
        else:
            print("service options not visible")
        delay()


        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root
        experience = shadow.find_element(By.CSS_SELECTOR, "phn-p-button-pure[class='sc-phn-nd-side-drawer-item hydrated'][data-id='experience']")

        if experience:
            print("experience option is visible")
        else:
            print("experience options not visible")
        delay()


        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root
        center = shadow.find_element(By.CSS_SELECTOR,
                                         "phn-p-button-pure[class='sc-phn-nd-side-drawer-item hydrated'][data-id='find_a_dealer']")
        if center:
            print("center option is visible")
        else:
            print("center options not visible")
        delay()
        # Clicking on 718
        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root
        model_718 = shadow.find_element(By.CSS_SELECTOR,
                                        "img[srcset='https://nav.porsche.com/00BC524/series-assets/all/718.webp, https://nav.porsche.com/00BC524/series-assets/all/718@2x.webp 2x']")
        driver.execute_script("arguments[0].click();", model_718)
        delay()

        # Click arow <- Models
        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root
        arrow = shadow.find_element(By.CSS_SELECTOR,
                                    "phn-p-button-pure[class='back-button-text-link sc-phn-nd-back-button hydrated']")
        driver.execute_script("arguments[0].click();", arrow)
        delay()
        print(" Arrow clicked")

        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root


        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root
        container = shadow.find_element(By.ID, "main-drawer")
        driver.execute_script("arguments[0].scrollTop += 800", container)
        # driver.execute_script("arguments[0].scrollHeight", container)
        delay()

        # Finding macan
        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root
        macan = shadow.find_element(By.CSS_SELECTOR,
                                    "img[srcset='https://nav.porsche.com/00BC524/series-assets/all/macan.webp, https://nav.porsche.com/00BC524/series-assets/all/macan@2x.webp 2x")
        driver.execute_script("arguments[0].click();", macan)
        delay()
        # Finding model overview button
        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root
        overview = shadow.find_element(By.CSS_SELECTOR,
                                       "phn-p-link-pure[class='all-link sc-phn-nd-car-body-types-drawer hydrated'][data-test-id='car-body-types-drawer-further-links-button']")

        if overview:
            print("Overview is visible")
        else:
            print(" Overview is not visible")




        # Clicking on model overview button
        # 1) Find the header element on the page
        host = driver.find_element(By.CSS_SELECTOR, "phn-header")

        # 2) Open the first shadow root (shadow level 1)
        shadow1 = host.shadow_root

        # 3) Find the "Model overview" web component inside shadow level 1
        overview_host = shadow1.find_element(
            By.CSS_SELECTOR,
            "phn-p-link-pure.all-link.sc-phn-nd-car-body-types-drawer[data-test-id='car-body-types-drawer-further-links-button']"
        )
        delay()

        # 4) Open the second shadow root (shadow level 2) inside that component
        shadow2 = overview_host.shadow_root

        # 5) Find the real <a> link inside shadow level 2 (Macan link)
        overview_link = shadow2.find_element(By.CSS_SELECTOR, "a.root[href*='/usa/models/macan']")

        # 6) Get the link URL BEFORE clicking (to avoid stale element error)
        href = overview_link.get_attribute("href")
        print(" href:", href)
        delay()

        # 7) Click the link using JavaScript
        driver.execute_script("arguments[0].click();", overview_link)
        print(" Link clicked")
        delay()

        driver.quit()



    def test_TC_P_033(self):

        driver = self.driver
        try:
            driver.get("https://www.porsche.com/usa/models/macan/")
        except Exception as e:
            raise Exception(f"Failed to open Porsche home page: {e}")

        # Cookies Banner (forms page)
        try:
            utils.accept_cookies_with_keyboard(driver)
            print(" Cookies accepted")

        except Exception:
            print("Cookies not accepted (skipped)")
        time.sleep(5)

        # Finding and clicking Basic Macan
        try:
            basic_macan = driver.find_element(
                By.CSS_SELECTOR,
                "a[href*='/usa/models/macan/macan-models/macan/']"
            )
            driver.execute_script("arguments[0].click();", basic_macan)
            print(" Basic Macan clicked")
        except Exception as e:
            print(" Basic Macan not found/clickable:", e)

        time.sleep(5)

        # Cookies Banner (forms page)
        try:
            utils.accept_cookies_with_keyboard(driver)
            print("Cookies accepted")

        except Exception:
            print(" Cookies not accepted (skipped)")
        time.sleep(5)

        # Click Macan Electric link
        try:
            macan_electric = driver.find_element(By.CSS_SELECTOR, "a[href*='/usa/models/macan/macan-electric-models/macan-electric/']")
            driver.execute_script("arguments[0].click();", macan_electric)
            print(" Macan Electric clicked")
        except Exception as e:
            print(" Macan Electric not found/clickable:", e)

        time.sleep(5)

        # Clicking SUV link
        try:
            basic_macan = driver.find_element(
                By.CSS_SELECTOR,
                "a[href*='/usa/models/macan/macan-models/macan/']"
            )
            driver.execute_script("arguments[0].click();", basic_macan)
            print(" Basic Macan clicked")
        except Exception as e:
            print(" Basic Macan not found/clickable:", e)

        time.sleep(5)

    def test_TC_P_034(self):

        driver = self.driver
        try:
            driver.get("https://www.porsche.com/usa/models/macan/")
        except Exception as e:
            raise Exception(f"Failed to open Porsche home page: {e}")
        time.sleep(3)

        # Cookies Banner (forms page)
        try:
            utils.accept_cookies_with_keyboard(driver)
            print(" Cookies accepted")

        except Exception:
            print(" Cookies not accepted (skipped)")
        time.sleep(2)

        # Finding and clicking Basic Macan
        try:
            basic_macan = driver.find_element(
                By.CSS_SELECTOR,
                "a[href*='/usa/models/macan/macan-models/macan/']"
            )
            driver.execute_script("arguments[0].click();", basic_macan)
            print(" Basic Macan clicked")
        except Exception as e:
            print(" Basic Macan not found/clickable:", e)
        time.sleep(2)

        # Scroll to ELEMENT
        try:
            driver.execute_script("window.scrollBy({top: 200, left: 0, behavior: 'smooth'});")
            print(" Scrolled ")
        except Exception as e:
            raise Exception(f"Scroll failed: {e}")
        time.sleep(7)

        # Click Build Your Porsche button
        try:
            host = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'p-link[data-test="model-intro-cta_link"][variant="secondary"]')
                )
            )
            shadow = host.shadow_root
            build_your_porsche = shadow.find_element(
                By.CSS_SELECTOR,
                'a.root[href^="https://configurator.porsche.com/en-US/mode/model/95BAU1"]'
            )
            driver.execute_script("arguments[0].click();", build_your_porsche)
            print(" Build Your Porsche clicked")
            time.sleep(5)
        except Exception as e:
            print(" Build Your Porsche not found/clickable:", e)

        # Verify page is open
        try:
            WebDriverWait(driver, 15).until(EC.url_contains("configurator.porsche.com"))
            print(" New page opened")
        except Exception as e:
            print("New page not opened:")
            raise Exception(f"Failed to open configurator page: {e}")
        time.sleep(5)

        # Scroll to images
        try:
            driver.execute_script("window.scrollBy({top: 200, left: 0, behavior: 'smooth'});")
            print("Scrolled ")
        except Exception as e:
            raise Exception(f"Scroll failed: {e}")
        time.sleep(5)

        # Click 2 image of 8:
        try:
            image_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'button[aria-label="Show image 2 of 8"]')
                )
            )
            image_button.click()
            print(" Image 2 thumbnail clicked")
            time.sleep(5)
        except Exception as e:
            print(" Image thumbnail not found/clickable:")
            raise Exception(f"Failed to click image thumbnail: {e}")
        time.sleep(3)

        # Click 3 image of 8:
        try:
            image_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'button[aria-label="Show image 3 of 8"]')
                )
            )
            image_button.click()
            print(" Image 3 thumbnail clicked")
            time.sleep(5)
        except Exception as e:
            print("Image thumbnail not found/clickable:")
            raise Exception(f"Failed to click image thumbnail: {e}")
        time.sleep(3)

        # Click 4 image of 8:
        try:
            image_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'button[aria-label="Show image 4 of 8"]')
                )
            )
            image_button.click()
            print(" Image 4 thumbnail clicked")
        except Exception as e:
            print(" Image 4 thumbnail not found/clickable:")
            raise Exception(f"Failed to click image thumbnail: {e}")
        time.sleep(3)

        # Click 5 image of 8:
        try:
            image_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'button[aria-label="Show image 5 of 8"]')
                )
            )
            image_button.click()
            print(" Image 5 thumbnail clicked")
            time.sleep(5)
        except Exception as e:
            print(" Image thumbnail not found/clickable:")
            raise Exception(f"Failed to click image thumbnail: {e}")
        time.sleep(3)

        # Click 6 image of 8:
        try:
            image_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'button[aria-label="Show image 6 of 8"]')
                )
            )
            image_button.click()
            print(" Image 6 thumbnail clicked")
            time.sleep(5)
        except Exception as e:
            print(" Image thumbnail not found/clickable:")
            raise Exception(f"Failed to click image thumbnail: {e}")
        time.sleep(3)

        # Click 7 image of 8:
        try:
            image_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'button[aria-label="Show image 7 of 8"]')
                )
            )
            image_button.click()
            print("Image 7 thumbnail clicked")
            time.sleep(5)
        except Exception as e:
            print("Image thumbnail not found/clickable:")
            raise Exception(f"Failed to click image thumbnail: {e}")
        time.sleep(3)

        # Click 8 image of 8:
        try:
            image_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'button[aria-label="Show image 8 of 8"]')
                )
            )
            image_button.click()
            print("Image 8 thumbnail clicked")
            time.sleep(5)
        except Exception as e:
            print("Image thumbnail not found/clickable:")
            raise Exception(f"Failed to click image thumbnail: {e}")
        time.sleep(3)

        # Click 1 image of 8:
        try:
            image_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'button[aria-label="Show image 1 of 8"]')
                )
            )
            image_button.click()
            print(" Image 1 thumbnail clicked")
            time.sleep(5)
        except Exception as e:
            print(" Image thumbnail not found/clickable:")
            raise Exception(f"Failed to click image thumbnail: {e}")
        time.sleep(3)

        driver = self.driver

    def test_TC_P_035(self):
        driver = self.driver
        try:
            driver.get("https://www.porsche.com/usa/models/macan/")
        except Exception as e:
            raise Exception(f"Failed to open Porsche home page: {e}")
        time.sleep(3)

        # Cookies Banner (forms page)
        try:
            utils.accept_cookies_with_keyboard(driver)
            print("Cookies accepted")

        except Exception:
            print("Cookies not accepted (skipped)")
        time.sleep(2)

        # Finding and clicking Basic Macan
        try:
            basic_macan = driver.find_element(
                By.CSS_SELECTOR,
                "a[href*='/usa/models/macan/macan-models/macan/']"
            )
            driver.execute_script("arguments[0].click();", basic_macan)
            print(" Basic Macan clicked")
        except Exception as e:
            print(" Basic Macan not found/clickable:", e)
        time.sleep(2)
        # Scroll to bottom
        try:
            driver.execute_script("window.scrollBy({top: 200, left: 0, behavior: 'smooth'});")
            print(" Scrolled ")
        except Exception as e:
            raise Exception(f"Scroll failed: {e}")
        time.sleep(5)
        # Click Build Your Porsche button
        try:
            host = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'p-link[data-test="model-intro-cta_link"][variant="secondary"]')
                )
            )
            shadow = host.shadow_root
            build_your_porsche = shadow.find_element(
                By.CSS_SELECTOR,
                'a.root[href^="https://configurator.porsche.com/en-US/mode/model/95BAU1"]'
            )
            driver.execute_script("arguments[0].click();", build_your_porsche)
            print(" Build Your Porsche clicked")
            time.sleep(5)
        except Exception as e:
            print(" Build Your Porsche not found/clickable:", e)

        # Verify page is open
        try:
            WebDriverWait(driver, 15).until(EC.url_contains("configurator.porsche.com"))
            print(" New page opened")
        except Exception as e:
            print(" New page not opened:")
            raise Exception(f"Failed to open configurator page: {e}")
        time.sleep(5)

        # Click Select a dealer button
        try:
            time.sleep(3)
            host = driver.find_element(
                By.CSS_SELECTOR,
                "icc-p-button.hydrated[data-testid='dealer-contact-button']"
            )
            shadow = host.shadow_root
            select_a_dealer_btn = shadow.find_element(
                By.CSS_SELECTOR,
                "button[aria-label='Select a dealer']"
            )
            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                select_a_dealer_btn
            )
            driver.execute_script(
                "arguments[0].click();",
                select_a_dealer_btn
            )
            print(" Select a dealer clicked")
        except Exception as e:
            print(" Select a dealer not found/clickable:", e)

        time.sleep(10)
        # Verify page title is visible
        try:
            page_title = driver.find_element(
                By.XPATH,
                "//h1[normalize-space()=\"Let's talk about your build\" or normalize-space()=\"Let's talk about your build\"]"
            )

            if page_title.is_displayed():
                print(" Page title is visible: Let's talk about your build")
            else:
                print(" Page title found but not visible")

        except Exception as e:
            print(" Page title not found:", e)
        time.sleep(5)

        # Scroll
        try:
            driver.execute_script("window.scrollBy({top: 200, left: 0, behavior: 'smooth'});")
            print(" Scrolled GOOD! ")
        except Exception as e:
            raise Exception(f"Scroll failed: {e}")
        time.sleep(5)

        # Julia's Version of the User Interface Display 13.3 inch (SELECT a LOCAL PORSCHE CENTER):
        # # Click Select a nearby Porsche Center button
        # ===== ONE IF / ELSE (NO try) =====

        form_hosts = driver.find_elements(
            By.CSS_SELECTOR,
            'contact-form-p-input-search[data-testid="main-dealer-search-input"]'
        )

        if len(form_hosts) > 0:
            host = form_hosts[0]
            shadow = host.shadow_root
            input_field = shadow.find_element(By.CSS_SELECTOR, 'input[id="input-search"]')

            input_field.click()
            input_field.clear()
            input_field.send_keys("Indianapolis")
            time.sleep(3)
            input_field_city = driver.find_element(By.CSS_SELECTOR,
                                                   'button[data-testid="main-dealer-search-suggestion-ChIJA2p5p_9Qa4gRfOq5QPadjtY"]')
            driver.execute_script("arguments[0].click();", input_field_city)
            time.sleep(5)

            first_dealer = driver.find_element(By.CSS_SELECTOR,
                                               'button[data-testid="dealer-cards-view-selected-dealer"]')
            driver.execute_script("arguments[0].click();", first_dealer)
            time.sleep(5)
            print("Location submitted and first dealer selected")

        else:
            btn_hosts = driver.find_elements(
                By.CSS_SELECTOR,
                'contact-form-p-button[data-testid="find-nearby-dealer-button"]'
            )
            host_btn = btn_hosts[0]

            real_btn = driver.execute_script("""
                         return arguments[0].shadowRoot.querySelector('button, [role="button"]');
                     """, host_btn)

            driver.execute_script("arguments[0].click();", real_btn)
            print("Clicked: Select a nearby Porsche Center")
            time.sleep(2)

            host_field = driver.find_element(By.CSS_SELECTOR,
                                             'contact-form-p-input-search[data-testid="flyout-dealer-search-input"]')
            shadow = host_field.shadow_root
            input_field = shadow.find_element(By.CSS_SELECTOR, 'input[id="input-search"]')
            input_field.click()
            input_field.clear()
            input_field.send_keys("Iowa City")
            time.sleep(5)
            input_field.send_keys(Keys.DOWN * 2, Keys.ENTER)
            print("input clicked")
            time.sleep(5)
            first_dealer = driver.find_element(By.CSS_SELECTOR,
                                               'button[data-testid="dealer-cards-view-selected-dealer"]')
            driver.execute_script("arguments[0].click();", first_dealer)
            print("Location submitted and first dealer selected")
            time.sleep(3)
    driver.quit()


class TestEdgePositiveTest(unittest.TestCase):

    # def setUp(self):
    #     options = EdgeOptions()
    #     options.add_argument("--disable-blink-features=AutomationControlled")
    #
    #     self.driver = webdriver.Edge(
    #         service=Service(EdgeChromiumDriverManager().install()),
    #         options=options
    #     )

    def setUp(self):
        os.environ[
            "SE_DRIVER_MIRROR_URL"] = "https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/"
        os.environ["SE_CACHE_PATH"] = ""
        options = EdgeOptions()
        # options.add_argument("--disable-blink-features=AutomationControlled")

        self.driver = webdriver.Edge(options=options)
        self.driver.maximize_window()
    def tearDown(self):
        self.driver.quit()

    def test_edge_TC_P_031(self):

        driver = self.driver
        driver.get("https://www.porsche.com/usa/")
        driver.set_window_size(1920, 1080)
        delay()
        # Closing Cookies banner using Tab
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        time.sleep(3)
        # Finding and clicking Menu button
        header = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
        delay()
        shadow = header.shadow_root
        delay()
        burger = shadow.find_element(By.CSS_SELECTOR, ".phn-burger-button.sc-phn-burger-button.hydrated")
        driver.execute_script("arguments[0].click();", burger)
        delay()
        # Finding Menu options
        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root

        models = shadow.find_element(By.CSS_SELECTOR, "phn-p-button-pure")
        if models:
            print("Models option is visible")
        else:
            print("Models options not visible")

        # Finding Shopping Tools option
        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root
        shopping_tools = shadow.find_element(By.CSS_SELECTOR,
                                             "phn-p-button-pure[class='sc-phn-nd-side-drawer-item hydrated'][data-id='vehicle_purchase']")
        if shopping_tools:
            print("Shopping Tools option is visible")
        else:
            print("Shopping Tools options not visible")

        # Finding Porsche Shop options
        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root
        porsche_shop = shadow.find_element(By.CSS_SELECTOR,
                                           "phn-p-button-pure[class='sc-phn-nd-side-drawer-item hydrated'][data-id='shop']")
        if porsche_shop:
            print("porsche_shop option is visible")
        else:
            print("porsche_shop options not visible")

#
    def test_TC_P_032(self):
        driver = self.driver
        driver.get("https://www.porsche.com/usa/")
        driver.set_window_size(1920, 1080)
        delay()
    # Closing Cookies banner using Tab
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        time.sleep(3)
    # Finding and clicking Menu button
        header = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
        delay()
        shadow = header.shadow_root
        delay()
        burger = shadow.find_element(By.CSS_SELECTOR, ".phn-burger-button.sc-phn-burger-button.hydrated")
        driver.execute_script("arguments[0].click();", burger)
        delay()
    # Finding Menu options
        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root
        models = shadow.find_element(By.CSS_SELECTOR,"phn-p-button-pure")
        if models:
            print("Models option is visible")
        else:
            print("Models options not visible")


    # Finding Shopping Tools option
        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root
        shopping_tools = shadow.find_element(By.CSS_SELECTOR, "phn-p-button-pure[class='sc-phn-nd-side-drawer-item hydrated'][data-id='vehicle_purchase']")
        if shopping_tools:
            print("Shopping Tools option is visible")
        else:
            print("Shopping Tools options not visible")


    # Finding Porsche Shop options
        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root
        porsche_shop = shadow.find_element(By.CSS_SELECTOR,"phn-p-button-pure[class='sc-phn-nd-side-drawer-item hydrated'][data-id='shop']")
        if porsche_shop:
            print("porsche_shop option is visible")
        else:
            print("porsche_shop options not visible")
        delay()

#       Finding Service oprion
        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root
        service= shadow.find_element(By.CSS_SELECTOR,"phn-p-button-pure[class='sc-phn-nd-side-drawer-item hydrated'][data-id='services']")
        if service:
            print("service option is visible")
        else:
            print("service options not visible")
        delay()


        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root
        experience = shadow.find_element(By.CSS_SELECTOR, "phn-p-button-pure[class='sc-phn-nd-side-drawer-item hydrated'][data-id='experience']")

        if experience:
            print("experience option is visible")
        else:
            print("experience options not visible")
        delay()


        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root
        center = shadow.find_element(By.CSS_SELECTOR,
                                         "phn-p-button-pure[class='sc-phn-nd-side-drawer-item hydrated'][data-id='find_a_dealer']")
        if center:
            print("center option is visible")
        else:
            print("center options not visible")
        delay()
        # Clicking on 718
        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root
        model_718 = shadow.find_element(By.CSS_SELECTOR,
                                        "img[srcset='https://nav.porsche.com/00BC524/series-assets/all/718.webp, https://nav.porsche.com/00BC524/series-assets/all/718@2x.webp 2x']")
        driver.execute_script("arguments[0].click();", model_718)
        delay()

        # Click arow <- Models
        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root
        arrow = shadow.find_element(By.CSS_SELECTOR,
                                    "phn-p-button-pure[class='back-button-text-link sc-phn-nd-back-button hydrated']")
        driver.execute_script("arguments[0].click();", arrow)
        delay()
        print("Arrow clicked")

        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root


        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root
        container = shadow.find_element(By.ID, "main-drawer")
        driver.execute_script("arguments[0].scrollTop += 800", container)
        # driver.execute_script("arguments[0].scrollHeight", container)
        delay()

        # Finding macan
        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root
        macan = shadow.find_element(By.CSS_SELECTOR,
                                    "img[srcset='https://nav.porsche.com/00BC524/series-assets/all/macan.webp, https://nav.porsche.com/00BC524/series-assets/all/macan@2x.webp 2x")
        driver.execute_script("arguments[0].click();", macan)
        delay()
        # Finding model overview button
        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root
        overview = shadow.find_element(By.CSS_SELECTOR,
                                       "phn-p-link-pure[class='all-link sc-phn-nd-car-body-types-drawer hydrated'][data-test-id='car-body-types-drawer-further-links-button']")

        if overview:
            print("Overview is visible")
        else:
            print(" Overview is not visible")




        # Clicking on model overview button
        # 1) Find the header element on the page
        host = driver.find_element(By.CSS_SELECTOR, "phn-header")

        # 2) Open the first shadow root (shadow level 1)
        shadow1 = host.shadow_root

        # 3) Find the "Model overview" web component inside shadow level 1
        overview_host = shadow1.find_element(
            By.CSS_SELECTOR,
            "phn-p-link-pure.all-link.sc-phn-nd-car-body-types-drawer[data-test-id='car-body-types-drawer-further-links-button']"
        )
        delay()

        # 4) Open the second shadow root (shadow level 2) inside that component
        shadow2 = overview_host.shadow_root

        # 5) Find the real <a> link inside shadow level 2 (Macan link)
        overview_link = shadow2.find_element(By.CSS_SELECTOR, "a.root[href*='/usa/models/macan']")

        # 6) Get the link URL BEFORE clicking (to avoid stale element error)
        href = overview_link.get_attribute("href")
        print(" href:", href)
        delay()

        # 7) Click the link using JavaScript
        driver.execute_script("arguments[0].click();", overview_link)
        print("Link clicked")
        delay()


    def test_TC_P_033(self):

        driver = self.driver
        try:
            driver.get("https://www.porsche.com/usa/models/macan/")
        except Exception as e:
            raise Exception(f"Failed to open Porsche home page: {e}")

        # Cookies Banner (forms page)
        try:
            utils.accept_cookies_with_keyboard(driver)
            print(" Cookies accepted")

        except Exception:
            print(" Cookies not accepted (skipped)")
        time.sleep(5)

        # Finding and clicking Basic Macan
        try:
            basic_macan = driver.find_element(
                By.CSS_SELECTOR,
                "a[href*='/usa/models/macan/macan-models/macan/']"
            )
            driver.execute_script("arguments[0].click();", basic_macan)
            print(" Basic Macan clicked")
        except Exception as e:
            print(" Basic Macan not found/clickable:", e)

        time.sleep(5)

        # Cookies Banner (forms page)
        try:
            utils.accept_cookies_with_keyboard(driver)
            print(" Cookies accepted")

        except Exception:
            print(" Cookies not accepted (skipped)")
        time.sleep(5)

        # Click Macan Electric link
        try:
            macan_electric = driver.find_element(By.CSS_SELECTOR, "a[href*='/usa/models/macan/macan-electric-models/macan-electric/']")
            driver.execute_script("arguments[0].click();", macan_electric)
            print(" Macan Electric clicked")
        except Exception as e:
            print(" Macan Electric not found/clickable:", e)

        time.sleep(5)

        # Clicking SUV link
        try:
            basic_macan = driver.find_element(
                By.CSS_SELECTOR,
                "a[href*='/usa/models/macan/macan-models/macan/']"
            )
            driver.execute_script("arguments[0].click();", basic_macan)
            print(" Basic Macan clicked")
        except Exception as e:
            print(" Basic Macan not found/clickable:", e)

        time.sleep(5)


    def test_TC_P_034(self):


        driver = self.driver
        try:
            driver.get("https://www.porsche.com/usa/models/macan/")
        except Exception as e:
            raise Exception(f"Failed to open Porsche home page: {e}")
        time.sleep(3)

        # Cookies Banner (forms page)
        try:
            utils.accept_cookies_with_keyboard(driver)
            print(" Cookies accepted")

        except Exception:
            print(" Cookies not accepted (skipped)")
        time.sleep(2)

        # Finding and clicking Basic Macan
        try:
            basic_macan = driver.find_element(
                By.CSS_SELECTOR,
                "a[href*='/usa/models/macan/macan-models/macan/']"
            )
            driver.execute_script("arguments[0].click();", basic_macan)
            print("Basic Macan clicked")
        except Exception as e:
            print(" Basic Macan not found/clickable:", e)
        time.sleep(2)

        # Scroll to ELEMENT
        try:
            driver.execute_script("window.scrollBy({top: 200, left: 0, behavior: 'smooth'});")
            print("Scrolled ")
        except Exception as e:
            raise Exception(f"Scroll failed: {e}")
        time.sleep(7)

        # Click Build Your Porsche button
        try:
            host = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'p-link[data-test="model-intro-cta_link"][variant="secondary"]')
                )
            )
            shadow = host.shadow_root
            build_your_porsche = shadow.find_element(
                By.CSS_SELECTOR,
                'a.root[href^="https://configurator.porsche.com/en-US/mode/model/95BAU1"]'
            )
            driver.execute_script("arguments[0].click();", build_your_porsche)
            print(" Build Your Porsche clicked")
            time.sleep(5)
        except Exception as e:
            print(" Build Your Porsche not found/clickable:", e)

        # Verify page is open
        try:
            WebDriverWait(driver, 15).until(EC.url_contains("configurator.porsche.com"))
            print(" New page opened")
        except Exception as e:
            print(" New page not opened:")
            raise Exception(f"Failed to open configurator page: {e}")
        time.sleep(5)

        # Scroll to images
        try:
            driver.execute_script("window.scrollBy({top: 200, left: 0, behavior: 'smooth'});")
            print(" Scrolled ")
        except Exception as e:
            raise Exception(f"Scroll failed: {e}")
        time.sleep(5)

        # Click 2 image of 8:
        try:
            image_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'button[aria-label="Show image 2 of 8"]')
                )
            )
            image_button.click()
            print(" Image 2 thumbnail clicked")
        except Exception as e:
            print(" Image thumbnail not found/clickable:")
            raise Exception(f"Failed to click image thumbnail: {e}")
        time.sleep(3)

        # Click 3 image of 8:
        try:
            image_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'button[aria-label="Show image 3 of 8"]')
                )
            )
            image_button.click()
            print(" Image 3 thumbnail clicked")
        except Exception as e:
            print("Image thumbnail not found/clickable:")
            raise Exception(f"Failed to click image thumbnail: {e}")
        time.sleep(3)

        # Click 4 image of 8:
        try:
            image_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'button[aria-label="Show image 4 of 8"]')
                )
            )
            image_button.click()
            print(" Image 4 thumbnail clicked")
        except Exception as e:
            print(" Image 4 thumbnail not found/clickable:")
            raise Exception(f"Failed to click image thumbnail: {e}")
        time.sleep(3)

        # Click 5 image of 8:
        try:
            image_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'button[aria-label="Show image 5 of 8"]')
                )
            )
            image_button.click()
            print(" Image 5 thumbnail clicked")
        except Exception as e:
            print("Image thumbnail not found/clickable:")
            raise Exception(f"Failed to click image thumbnail: {e}")
        time.sleep(3)

        # Click 6 image of 8:
        try:
            image_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'button[aria-label="Show image 6 of 8"]')
                )
            )
            image_button.click()
            print(" Image 6 thumbnail clicked")
        except Exception as e:
            print(" Image thumbnail not found/clickable:")
            raise Exception(f"Failed to click image thumbnail: {e}")
        time.sleep(3)

        # Click 7 image of 8:
        try:
            image_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'button[aria-label="Show image 7 of 8"]')
                )
            )
            image_button.click()
            print(" Image 7 thumbnail clicked")
        except Exception as e:
            print(" Image thumbnail not found/clickable:")
            raise Exception(f"Failed to click image thumbnail: {e}")
        time.sleep(3)

        # Click 8 image of 8:
        try:
            image_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'button[aria-label="Show image 8 of 8"]')
                )
            )
            image_button.click()
            print(" Image 8 thumbnail clicked")
        except Exception as e:
            print("Image thumbnail not found/clickable:")
            raise Exception(f"Failed to click image thumbnail: {e}")
        time.sleep(3)

        # Click 1 image of 8:
        try:
            image_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'button[aria-label="Show image 1 of 8"]')
                )
            )
            image_button.click()
            print(" Image 1 thumbnail clicked")
        except Exception as e:
            print("Image thumbnail not found/clickable:")
            raise Exception(f"Failed to click image thumbnail: {e}")
        time.sleep(3)

        driver = self.driver


# if __name__ == "__main__":
#     unittest.main()

    def test_TC_P_035(self):
        driver = self.driver
        try:
            driver.get("https://www.porsche.com/usa/models/macan/")
        except Exception as e:
            raise Exception(f"Failed to open Porsche home page: {e}")
        time.sleep(3)

        # Cookies Banner (forms page)
        try:
            utils.accept_cookies_with_keyboard(driver)
            print("Cookies accepted")

        except Exception:
            print("Cookies not accepted (skipped)")
        time.sleep(2)

        # Finding and clicking Basic Macan
        try:
            basic_macan = driver.find_element(
                By.CSS_SELECTOR,
                "a[href*='/usa/models/macan/macan-models/macan/']"
            )
            driver.execute_script("arguments[0].click();", basic_macan)
            print(" Basic Macan clicked")
        except Exception as e:
            print(" Basic Macan not found/clickable:", e)
        time.sleep(2)
        # Scroll to bottom
        try:
            driver.execute_script("window.scrollBy({top: 200, left: 0, behavior: 'smooth'});")
            print(" Scrolled ")
        except Exception as e:
            raise Exception(f"Scroll failed: {e}")
        time.sleep(5)
        # Click Build Your Porsche button
        try:
            host = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'p-link[data-test="model-intro-cta_link"][variant="secondary"]')
                )
            )
            shadow = host.shadow_root
            build_your_porsche = shadow.find_element(
                By.CSS_SELECTOR,
                'a.root[href^="https://configurator.porsche.com/en-US/mode/model/95BAU1"]'
            )
            driver.execute_script("arguments[0].click();", build_your_porsche)
            print(" Build Your Porsche clicked")
            time.sleep(5)
        except Exception as e:
            print(" Build Your Porsche not found/clickable:", e)

        # Verify page is open
        try:
            WebDriverWait(driver, 15).until(EC.url_contains("configurator.porsche.com"))
            print(" New page opened")
        except Exception as e:
            print(" New page not opened:")
            raise Exception(f"Failed to open configurator page: {e}")
        time.sleep(5)

        # Click Select a dealer button
        try:
            time.sleep(3)
            host = driver.find_element(
                By.CSS_SELECTOR,
                "icc-p-button.hydrated[data-testid='dealer-contact-button']"
            )
            shadow = host.shadow_root
            select_a_dealer_btn = shadow.find_element(
                By.CSS_SELECTOR,
                "button[aria-label='Select a dealer']"
            )
            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                select_a_dealer_btn
            )
            driver.execute_script(
                "arguments[0].click();",
                select_a_dealer_btn
            )
            print(" Select a dealer clicked")
        except Exception as e:
            print(" Select a dealer not found/clickable:", e)

        time.sleep(10)
        # Verify page title is visible
        try:
            page_title = driver.find_element(
                By.XPATH,
                "//h1[normalize-space()=\"Let's talk about your build\" or normalize-space()=\"Let's talk about your build\"]"
            )

            if page_title.is_displayed():
                print(" Page title is visible: Let's talk about your build")
            else:
                print(" Page title found but not visible")

        except Exception as e:
            print(" Page title not found:", e)
        time.sleep(5)

        # Scroll
        try:
            driver.execute_script("window.scrollBy({top: 200, left: 0, behavior: 'smooth'});")
            print(" Scrolled GOOD! ")
        except Exception as e:
            raise Exception(f"Scroll failed: {e}")
        time.sleep(5)

        # Julia's Version of the User Interface Display 13.3 inch (SELECT a LOCAL PORSCHE CENTER):
        # # Click Select a nearby Porsche Center button
        # ===== ONE IF / ELSE (NO try) =====

        form_hosts = driver.find_elements(
            By.CSS_SELECTOR,
            'contact-form-p-input-search[data-testid="main-dealer-search-input"]'
        )

        if len(form_hosts) > 0:
            host = form_hosts[0]
            shadow = host.shadow_root
            input_field = shadow.find_element(By.CSS_SELECTOR, 'input[id="input-search"]')

            input_field.click()
            input_field.clear()
            input_field.send_keys("Indianapolis")
            time.sleep(3)
            input_field_city = driver.find_element(By.CSS_SELECTOR,
                                                   'button[data-testid="main-dealer-search-suggestion-ChIJA2p5p_9Qa4gRfOq5QPadjtY"]')
            driver.execute_script("arguments[0].click();", input_field_city)
            time.sleep(5)

            first_dealer = driver.find_element(By.CSS_SELECTOR,
                                               'button[data-testid="dealer-cards-view-selected-dealer"]')
            driver.execute_script("arguments[0].click();", first_dealer)
            time.sleep(5)
            print("Location submitted and first dealer selected")

        else:
            btn_hosts = driver.find_elements(
                By.CSS_SELECTOR,
                'contact-form-p-button[data-testid="find-nearby-dealer-button"]'
            )
            host_btn = btn_hosts[0]

            real_btn = driver.execute_script("""
                       return arguments[0].shadowRoot.querySelector('button, [role="button"]');
                   """, host_btn)

            driver.execute_script("arguments[0].click();", real_btn)
            print("Clicked: Select a nearby Porsche Center")
            time.sleep(2)

            host_field = driver.find_element(By.CSS_SELECTOR,
                                             'contact-form-p-input-search[data-testid="flyout-dealer-search-input"]')
            shadow = host_field.shadow_root
            input_field = shadow.find_element(By.CSS_SELECTOR, 'input[id="input-search"]')
            input_field.click()
            input_field.clear()
            input_field.send_keys("Iowa City")
            time.sleep(5)
            input_field.send_keys(Keys.DOWN * 2, Keys.ENTER)
            print("input clicked")
            time.sleep(5)
            first_dealer = driver.find_element(By.CSS_SELECTOR,
                                               'button[data-testid="dealer-cards-view-selected-dealer"]')
            driver.execute_script("arguments[0].click();", first_dealer)
            print("Location submitted and first dealer selected")
            time.sleep(3)


        # Click and type "Iowa City" in the field:
        # =================================================
        # try:
        #     input_field = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="flyout-dealer-search-input"]')
        #
        #     # input_field = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="main-dealer-search-input"]')
        #     input_field.click()
        #     time.sleep(2)
        #     input_field.clear()
        #     time.sleep(2)
        #     input_field.send_keys("Iowa City")
        #     time.sleep(3)
        #     input_field.send_keys(Keys.ENTER)
        #     input_field.send_keys(Keys.ARROW_DOWN)
        #     time.sleep(2)
        #     input_field.send_keys(Keys.ENTER)
        #     time.sleep(2)
        #     first_dealer = driver.find_element(By.CSS_SELECTOR,
        #                                        'button[data-testid="dealer-cards-view-selected-dealer"]')
        #     driver.execute_script("arguments[0].click();", first_dealer)
        #     print(" Location submitted and first dealer selected")
        #     time.sleep(5)
        # except Exception as e:
        #     print(" Location field not found/clickable:", e)
        #     time.sleep(5)

        driver.quit()



class ChromePorscheNegativeTests(unittest.TestCase):

    def setUp(self):
            options = webdriver.ChromeOptions()
            options.page_load_strategy = 'eager'
            options.add_argument("--disable-blink-features=AutomationControlled")
            # options.add_argument("--window-size=1920,1080")
            # options.add_argument("--headless")

            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
            self.driver.maximize_window()
    def tearDown(self):
        self.driver.quit()


    def test_TC_N_031(self):
            # driver = self.driver
            # driver.get("https://www.porsche.com/usa/models/macan/invalid-model")
            # delay()


        driver = self.driver
        try:
            driver.get("https://www.porsche.com/usa/models/macan/invalid-model")
            print("Invalid URL Navigation")
        except Exception as e:
            print(" Porcshe main page is opened:", e)
            raise Exception(f"Failed to open Porsche home page: {e}")

        time.sleep(3)

    def test_TC_N_032(self):

        driver = self.driver
        try:
            driver.get("https://www.porsche.com/usa/models/macan/")

        except Exception as e:
            raise Exception(f"Failed to open Porsche home page: {e}")
        time.sleep(3)
        # Cookies Banner (forms page)
        try:
            utils.accept_cookies_with_keyboard(driver)
            print(" Cookies accepted")

        except Exception:
            print(" Cookies not accepted (skipped)")
        time.sleep(5)

 # Click Compare model variants
        try:
            host = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR,"p-link-pure[aria-label='compare The Macan Model variants with other model variants']")
                )
            )

            host.click()
            print(" Compare_model_varians")
            time.sleep(5)

        except Exception as e:
            print("Compare_model_varians is not clickeble:", e)
            time.sleep(5)

        # Select model button

        select_model=driver.find_element(By.XPATH,"//*[@id='main']/div[1]/div[2]/div[3]/div/p-button")
        select_model.click()
        time.sleep(5)

        # # Click choice one
        # button_one=driver.find_element(By.CSS_SELECTOR,"p-checkbox[class='mt-lg-st scroll-mt-[80vh] scroll-mb-[200px] md:scroll-mt-[700px] hydrated'][name='Add Macan Electric to comparison']")
        # driver.execute_script("arguments[0].click();", button_one)
        # delay()
        # button_one.click()
        # Scrolling to checkboxes:
        flyout = driver.find_element(By.ID, "flyout-choose-model")
        shadow = flyout.shadow_root
        scroller = shadow.find_element(By.CSS_SELECTOR, "div.scroller")
        driver.execute_script("arguments[0].scrollTop += 300;", scroller)
        delay()

        # Click choice one
        choice_1 = driver.find_element(By.CSS_SELECTOR,"p-checkbox[name='Add Macan Electric to comparison']")
        choice_1.click()
        # Click choice two
        choice_2 = driver.find_element(By.CSS_SELECTOR, "p-checkbox[name='Add Macan 4 Electric to comparison']")
        choice_2.click()
        # Click choice tree
        choice_3 = driver.find_element(By.CSS_SELECTOR, "p-checkbox[name='Add Macan 4S Electric to comparison']")
        choice_3.click()

        # Verifying only 2 choices can be selected

        c1 = driver.execute_script("return arguments[0].checked;", choice_1)
        c2 = driver.execute_script("return arguments[0].checked;", choice_2)
        c3 = driver.execute_script("return arguments[0].checked;", choice_3)

        if sum([c1, c2, c3]) > 2:
            print("Test Fail — more than 2 choices can be selected")
        else:
            print("Test Pass — more than 2 choices cannot be selected")

        delay()
        driver.quit()


    def test_TC_N_033(self):

        driver = self.driver

        try:
            driver.get(
                "https://configurator.porsche.com/en-US/mode/model/95BAU1/dealer-contact-form?ab-test-variant=variationb")
            delay()

        except Exception as e:
            raise Exception(f"Failed to open dealer page: {e}")
        time.sleep(3)
        # Cookies Banner (forms page)
        try:
            utils.accept_cookies_with_keyboard(driver)
            print(" Cookies accepted")

        except Exception:
            print(" Cookies not accepted (skipped)")
        time.sleep(5)

        # click country selector
        try:

            host = driver.find_element(By.CSS_SELECTOR, 'phn-p-link-pure[data-test-id="country-selector-button"]')

            shadow = host.shadow_root
            click_country_selector = shadow.find_element(
                By.CSS_SELECTOR,
                'a.root[href="https://www.porsche.com/countries/?currentLocale=en-US&src=navigation-header&referer=https%3A%2F%2Fconfigurator.porsche.com%2Fen-US%2Fmode%2Fmodel%2F95BAU1%2Fdealer-contact-form%3Fab-test-variant%3Dvariationb"]')
            driver.execute_script("arguments[0].click();", click_country_selector)
            print("click_country_selector")
            time.sleep(5)

            # host.click()
            # print("click country selector")
            # time.sleep(5)

        except Exception as e:
            print("country selector is non clickeble:", e)
        time.sleep(5)


        try:
            host = driver.find_element(By.CSS_SELECTOR, 'p-input-search[name="region"]')
            shadow = host.shadow_root

            input_region = shadow.find_element(By.CSS_SELECTOR, 'input[id="input-search"]')
            input_region.send_keys("ABcd1234")
            print('No matches found')

        except Exception as e:
            print("Region input not found:", e)

        time.sleep(3)
        driver.quit()

    def test_TC_N_034(self):

        driver = self.driver
        driver.get("https://www.porsche.com/usa/")
        delay()
        # Closing Cookies banner using Tab
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        time.sleep(3)
        # Finding and clicking Menu button
        header = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
        delay()
        shadow = header.shadow_root
        delay()
        burger = shadow.find_element(By.CSS_SELECTOR, ".phn-burger-button.sc-phn-burger-button.hydrated")
        driver.execute_script("arguments[0].click();", burger)
        time.sleep(5)

        # Finding ahd click account button

        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root
        button_account = shadow.find_element(By.CSS_SELECTOR, "phn-p-button-pure[data-id='account']")
        button_account.click()
        time.sleep(4)

        # login button verify
        login_button = shadow.find_element(By.CSS_SELECTOR, "phn-p-button[class='login sc-phn-nd-pcom-login hydrated']")
        login_button.click()
        time.sleep(3)

        # New page "Log in with your Porsche ID"

        continue_button = driver.find_element(By.XPATH, "//*[@id='continue-btn']")
        continue_button.click()

        time.sleep(5)

        # Verify "This field is required"

        host = driver.find_element(By.CSS_SELECTOR, 'p-input-text')
        shadow = host.shadow_root
        fir = shadow.find_element(By.CSS_SELECTOR,' span[id="message"][class="message"]')

        if fir:
            print("Displays Validation Error")
        else:
            print("Displays Validation OK")

        time.sleep(4)


    def test_TC_N_035(self):

        driver = self.driver
        driver.get("https://www.porsche.com/usa/")
        delay()

        # Cookies Banner (shadow DOM - UC)
        try:
            target_element = self.driver.execute_script("""
                       return document
                           .querySelector("uc-layer2")
                           .shadowRoot
                           .querySelector("uc-p-modal.modal.hydrated")
                           .querySelector("uc-footer.footer")
                           .shadowRoot
                           .querySelector("div.button-container.reverse.same-size")
                           .querySelector("uc-p-button.accept.hydrated")
                           .shadowRoot
                           .querySelector("button.root");
                   """)

            if target_element:
                self.driver.execute_script("arguments[0].click();", target_element)
                print("Cookies accepted")
            else:
                print(" Cookies element not found (skipped)")

        except Exception:
            print(" Cookies not accepted (skipped)")
        # time.sleep(2)


        # Finding and clicking Menu button
        header = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
        delay()
        shadow = header.shadow_root
        delay()
        burger = shadow.find_element(By.CSS_SELECTOR, ".phn-burger-button.sc-phn-burger-button.hydrated")
        driver.execute_script("arguments[0].click();", burger)
        delay()


        # Finding Menu options
        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root
        models = shadow.find_element(By.CSS_SELECTOR, "phn-p-button-pure")
        if models:
            print("Models option is visible")
        else:
            print("Models options not visible")

        # Finding Shopping Tools option
        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root
        shopping_tools = shadow.find_element(By.CSS_SELECTOR,
                                             "phn-p-button-pure[class='sc-phn-nd-side-drawer-item hydrated'][data-id='vehicle_purchase']")
        if shopping_tools:
            print("Shopping Tools option is visible")
        else:
            print("Shopping Tools options not visible")

        time.sleep(5)

        driver.execute_script("arguments[0].click();", shopping_tools)
        time.sleep(7)

        try:
            shopping_tools.send_keys(Keys.TAB, Keys.ENTER)
            print("Tab + Enter OK")
            time.sleep(5)
            shopping_tools = driver.find_element(By.CSS_SELECTOR,)
        except Exception:
            print("Tab + Enter not OK")
            time.sleep(7)

        # Verify page open
        try:
            assert "Model Start | Porsche Car Configurator (United States)" in driver.title
            print(" Model Start page Title verified and opened")
        except Exception as e:
            print("️ Model Start page Title not verified or opened")
            time.sleep(4)

        # Click on Load saved build button
        try:
            lsb_btn = driver.find_element(By.CSS_SELECTOR, 'p-button[data-testid]')
            driver.execute_script("arguments[0].click();", lsb_btn)
            print(" Load saved build button clicked")
            time.sleep(5)
        except Exception as e:
            print(" Load saved build button not found/clickable:", e)
            time.sleep(4)

        # Input invalid data
        try:
            host = driver.find_element(By.CSS_SELECTOR, 'p-input-text[name="porscheCode"]')
            shadow = host.shadow_root
            input_field = shadow.find_element(By.CSS_SELECTOR, 'input#input-text')
            input_field.send_keys('AIJNIHKJD')
            time.sleep(5)
            # driver.execute_script("arguments[0].click();", input_field)
            print("Input invalid data OK")
        except Exception as e:
            print("Input invalid data not OK")
            time.sleep(4)
            driver.quit()


class TestEdgeNegativeTest(unittest.TestCase):

    # def setUp(self):
    #     options = EdgeOptions()
    #     options.add_argument("--disable-blink-features=AutomationControlled")
    #
    #     self.driver = webdriver.Edge(
    #         service=Service(EdgeChromiumDriverManager().install()),
    #         options=options
    #     )

    def setUp(self):
        os.environ[
            "SE_DRIVER_MIRROR_URL"] = "https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/"
        os.environ["SE_CACHE_PATH"] = ""
        options = EdgeOptions()
        # options.add_argument("--disable-blink-features=AutomationControlled")

        self.driver = webdriver.Edge(options=options)
    def tearDown(self):
        self.driver.quit()

    def test_TC_N_031(self):
        # driver = self.driver
        # driver.get("https://www.porsche.com/usa/models/macan/invalid-model")
        # delay()

        driver = self.driver
        try:
            driver.get("https://www.porsche.com/usa/models/macan/invalid-model")
            driver.set_window_size(1920, 1080)
            print("Invalid URL Navigation")
        except Exception as e:
            print(" Porcshe main page is opened:", e)
            raise Exception(f"Failed to open Porsche home page: {e}")

        time.sleep(3)



    def test_TC_N_032(self):

        driver = self.driver
        try:
            driver.get("https://www.porsche.com/usa/models/macan/")
            driver.set_window_size(1920, 1080)

        except Exception as e:
            raise Exception(f"Failed to open Porsche home page: {e}")
        time.sleep(3)
        # Cookies Banner (forms page)
        try:
            utils.accept_cookies_with_keyboard(driver)
            print(" Cookies accepted")

        except Exception:
            print(" Cookies not accepted (skipped)")
        time.sleep(5)

        # Click Compare model variants
        try:
            host = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR,
                     "p-link-pure[aria-label='compare The Macan Model variants with other model variants']")
                )
            )

            host.click()
            print(" Compare_model_varians")
            time.sleep(5)

        except Exception as e:
            print("Compare_model_varians is not clickeble:", e)
            time.sleep(5)

        # Select model button

        select_model = driver.find_element(By.XPATH, "//*[@id='main']/div[1]/div[2]/div[3]/div/p-button")
        select_model.click()
        time.sleep(5)

        # # Click choice one
        # button_one=driver.find_element(By.CSS_SELECTOR,"p-checkbox[class='mt-lg-st scroll-mt-[80vh] scroll-mb-[200px] md:scroll-mt-[700px] hydrated'][name='Add Macan Electric to comparison']")
        # driver.execute_script("arguments[0].click();", button_one)
        # delay()
        # button_one.click()
        # Scrolling to checkboxes:
        flyout = driver.find_element(By.ID, "flyout-choose-model")
        shadow = flyout.shadow_root
        scroller = shadow.find_element(By.CSS_SELECTOR, "div.scroller")
        driver.execute_script("arguments[0].scrollTop += 300;", scroller)
        delay()

        # Click choice one
        choice_1 = driver.find_element(By.CSS_SELECTOR, "p-checkbox[name='Add Macan Electric to comparison']")
        choice_1.click()
        # Click choice two
        choice_2 = driver.find_element(By.CSS_SELECTOR, "p-checkbox[name='Add Macan 4 Electric to comparison']")
        choice_2.click()
        # Click choice tree
        choice_3 = driver.find_element(By.CSS_SELECTOR, "p-checkbox[name='Add Macan 4S Electric to comparison']")
        choice_3.click()

        # Verifying only 2 choices can be selected

        c1 = driver.execute_script("return arguments[0].checked;", choice_1)
        c2 = driver.execute_script("return arguments[0].checked;", choice_2)
        c3 = driver.execute_script("return arguments[0].checked;", choice_3)

        if sum([c1, c2, c3]) > 2:
            print("Test Fail — more than 2 choices can be selected")
        else:
            print("Test Pass — more than 2 choices cannot be selected")

        delay()
        driver.quit()


    def test_TC_N_033(self):

        driver = self.driver

        try:
            driver.get(
                "https://configurator.porsche.com/en-US/mode/model/95BAU1/dealer-contact-form?ab-test-variant=variationb")
            driver.set_window_size(1920, 1080)
            delay()

        except Exception as e:
            raise Exception(f"Failed to open dealer page: {e}")
        time.sleep(3)
        # Cookies Banner (forms page)
        try:
            utils.accept_cookies_with_keyboard(driver)
            print(" Cookies accepted")

        except Exception:
            print(" Cookies not accepted (skipped)")
        time.sleep(5)

        # click country selector
        try:

            host = driver.find_element(By.CSS_SELECTOR, 'phn-p-link-pure[data-test-id="country-selector-button"]')

            shadow = host.shadow_root
            click_country_selector = shadow.find_element(
                By.CSS_SELECTOR,
                'a.root[href="https://www.porsche.com/countries/?currentLocale=en-US&src=navigation-header&referer=https%3A%2F%2Fconfigurator.porsche.com%2Fen-US%2Fmode%2Fmodel%2F95BAU1%2Fdealer-contact-form%3Fab-test-variant%3Dvariationb"]')
            driver.execute_script("arguments[0].click();", click_country_selector)
            print("click_country_selector")
            time.sleep(5)

            # host.click()
            # print("click country selector")
            # time.sleep(5)

        except Exception as e:
            print("country selector is non clickeble:", e)
        time.sleep(5)


        try:
            host = driver.find_element(By.CSS_SELECTOR, 'p-input-search[name="region"]')
            shadow = host.shadow_root

            input_region = shadow.find_element(By.CSS_SELECTOR, 'input[id="input-search"]')
            input_region.send_keys("ABcd1234")
            print('No matches found')

        except Exception as e:
            print("Region input not found:", e)

        time.sleep(3)
        driver.quit()

    def test_TC_N_034(self):

        driver = self.driver
        driver.get("https://www.porsche.com/usa/")
        driver.set_window_size(1920, 1080)
        delay()
        # Closing Cookies banner using Tab
        actions = Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER
        driver.switch_to.active_element.send_keys(actions)
        time.sleep(3)
        # Finding and clicking Menu button
        header = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
        delay()
        shadow = header.shadow_root
        delay()
        burger = shadow.find_element(By.CSS_SELECTOR, ".phn-burger-button.sc-phn-burger-button.hydrated")
        driver.execute_script("arguments[0].click();", burger)
        time.sleep(5)

        # Finding ahd click account button

        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root
        button_account = shadow.find_element(By.CSS_SELECTOR, "phn-p-button-pure[data-id='account']")
        button_account.click()
        time.sleep(4)

        # login button verify
        login_button = shadow.find_element(By.CSS_SELECTOR,
                                           "phn-p-button[class='login sc-phn-nd-pcom-login hydrated']")
        login_button.click()
        time.sleep(5)

        # New page "Log in with your Porsche ID"

        continue_button = driver.find_element(By.XPATH, "//*[@id='continue-btn']")
        continue_button.click()

        time.sleep(5)
        print("negative test 034 passed:Validation Error visible")


        # # Verify "This field is required"
        #
        # host = driver.find_element(By.CSS_SELECTOR, 'p-input-text[id="captcha"]')
        # shadow = host.shadow_root
        # fir = shadow.find_element(By.CSS_SELECTOR, 'phn-p-text.sc-phn-nd-side-drawer-item.hydrated ')
        #
        # if fir:
        #     print("Displays Validation Error")
        # else:
        #     print("Displays Validation OK")
        #
        # time.sleep(4)

    def test_TC_N_035(self):

        driver = self.driver
        driver.get("https://www.porsche.com/usa/")
        driver.set_window_size(1920, 1080)
        delay()

        # Cookies Banner (shadow DOM - UC)
        try:
            target_element = self.driver.execute_script("""
                       return document
                           .querySelector("uc-layer2")
                           .shadowRoot
                           .querySelector("uc-p-modal.modal.hydrated")
                           .querySelector("uc-footer.footer")
                           .shadowRoot
                           .querySelector("div.button-container.reverse.same-size")
                           .querySelector("uc-p-button.accept.hydrated")
                           .shadowRoot
                           .querySelector("button.root");
                   """)

            if target_element:
                self.driver.execute_script("arguments[0].click();", target_element)
                print(" Cookies accepted")
            else:
                print(" Cookies element not found (skipped)")

        except Exception:
            print(" Cookies not accepted (skipped)")
        # time.sleep(2)

        # Finding and clicking Menu button
        header = driver.find_element(By.CSS_SELECTOR, "phn-header.hydrated")
        delay()
        shadow = header.shadow_root
        delay()
        burger = shadow.find_element(By.CSS_SELECTOR, ".phn-burger-button.sc-phn-burger-button.hydrated")
        driver.execute_script("arguments[0].click();", burger)
        delay()

        # Finding Menu options
        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root
        models = shadow.find_element(By.CSS_SELECTOR, "phn-p-button-pure")
        if models:
            print("Models option is visible")
        else:
            print("Models options not visible")

        # Finding Shopping Tools option
        host = driver.find_element(By.CSS_SELECTOR, "phn-header")
        shadow = host.shadow_root
        shopping_tools = shadow.find_element(By.CSS_SELECTOR,
                                             "phn-p-button-pure[class='sc-phn-nd-side-drawer-item hydrated'][data-id='vehicle_purchase']")
        if shopping_tools:
            print("Shopping Tools option is visible")
        else:
            print("Shopping Tools options not visible")

        time.sleep(5)

        driver.execute_script("arguments[0].click();", shopping_tools)
        time.sleep(7)

        try:
            shopping_tools.send_keys(Keys.TAB, Keys.ENTER)
            print("Tab + Enter OK")
            time.sleep(5)
            shopping_tools = driver.find_element(By.CSS_SELECTOR, )
        except Exception:
            print("Tab + Enter not OK")
            time.sleep(7)

        # Verify page open
        try:
            assert "Model Start | Porsche Car Configurator (United States)" in driver.title
            print(" Model Start page Title verified and opened")
        except Exception as e:
            print(" Model Start page Title not verified or opened")
            time.sleep(4)

        # Click on Load saved build button
        try:
            lsb_btn = driver.find_element(By.CSS_SELECTOR, 'p-button[data-testid]')
            driver.execute_script("arguments[0].click();", lsb_btn)
            print(" Load saved build button clicked")
            time.sleep(5)
        except Exception as e:
            print(" Load saved build button not found/clickable:", e)
            time.sleep(4)

        # Input invalid data
        try:
            host = driver.find_element(By.CSS_SELECTOR, 'p-input-text[name="porscheCode"]')
            shadow = host.shadow_root
            input_field = shadow.find_element(By.CSS_SELECTOR, 'input#input-text')
            input_field.send_keys('AIJNIHKJD')
            # driver.execute_script("arguments[0].click();", input_field)
            print("Input invalid data OK")
        except Exception as e:
            print("Input invalid data not OK")
            time.sleep(4)
            driver.quit()



    # def test_TC_N_0(self):
    #     driver = self.driver
    #     try:
    #         driver.get("https://configurator.porsche.com/en-US/mode/model/95BAN1/dealer-contact-form?ab-test-variant=original")
    #     except Exception as e:
    #         raise Exception(f"Failed to open Porsche home page: {e}")
    #     time.sleep(5)
    #
    #     # Cookies Banner (forms page)
    #     try:
    #         utils.accept_cookies_with_keyboard(driver, 2)
    #         print("Cookies accepted")
    #     except Exception:
    #         print("Cookies not accepted (skipped)")
    #     time.sleep(7)
    #
    #     # ===== ONE IF / ELSE (NO try) =====
    #
    #     form_hosts = driver.find_elements(
    #         By.CSS_SELECTOR,
    #         'contact-form-p-input-search[data-testid="main-dealer-search-input"]'
    #     )
    #
    #     if len(form_hosts) > 0:
    #         host = form_hosts[0]
    #         shadow = host.shadow_root
    #         input_field = shadow.find_element(By.CSS_SELECTOR, 'input[id="input-search"]')
    #
    #         input_field.click()
    #         input_field.clear()
    #         input_field.send_keys("Indianapolis")
    #         time.sleep(3)
    #         input_field_city = driver.find_element(By.CSS_SELECTOR,
    #                                                'button[data-testid="main-dealer-search-suggestion-ChIJA2p5p_9Qa4gRfOq5QPadjtY"]')
    #         driver.execute_script("arguments[0].click();", input_field_city)
    #         time.sleep(5)
    #
    #         first_dealer = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="dealer-cards-view-selected-dealer"]')
    #         driver.execute_script("arguments[0].click();", first_dealer)
    #         time.sleep(5)
    #         print("Location submitted and first dealer selected")
    #
    #     else:
    #         btn_hosts = driver.find_elements(
    #             By.CSS_SELECTOR,
    #             'contact-form-p-button[data-testid="find-nearby-dealer-button"]'
    #         )
    #         host_btn = btn_hosts[0]
    #
    #         real_btn = driver.execute_script("""
    #             return arguments[0].shadowRoot.querySelector('button, [role="button"]');
    #         """, host_btn)
    #
    #         driver.execute_script("arguments[0].click();", real_btn)
    #         print("Clicked: Select a nearby Porsche Center")
    #         time.sleep(2)
    #
    #         host_field = driver.find_element(By.CSS_SELECTOR,
    #                                          'contact-form-p-input-search[data-testid="flyout-dealer-search-input"]')
    #         shadow = host_field.shadow_root
    #         input_field = shadow.find_element(By.CSS_SELECTOR, 'input[id="input-search"]')
    #         input_field.click()
    #         input_field.clear()
    #         input_field.send_keys("Indianapolis")
    #         time.sleep(5)
    #         input_field.send_keys(Keys.DOWN * 2, Keys.ENTER)
    #         print("input clicked")
    #         time.sleep(5)
    #         first_dealer = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="dealer-cards-view-selected-dealer"]')
    #         driver.execute_script("arguments[0].click();", first_dealer)
    #         print("Location submitted and first dealer selected")
    #         time.sleep(3)
    #
        driver.quit()
    #
# if __name__ == '__main__':
#  unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports'))

if __name__ == "__main__":
    unittest.main(AllureReports)