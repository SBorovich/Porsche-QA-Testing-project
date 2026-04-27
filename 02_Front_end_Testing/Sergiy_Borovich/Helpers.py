from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import requests
def delay():
    time.sleep(random.randint(1, 3))


def shopping_tools_button(driver):
    host = driver.find_element(By.CSS_SELECTOR, "phn-header")
    shadow = host.shadow_root
    shopping_tools = shadow.find_element(By.CSS_SELECTOR,"phn-p-button-pure[class='sc-phn-nd-side-drawer-item hydrated'][data-id='vehicle_purchase']")
    driver.execute_script("arguments[0].click();", shopping_tools)

def finding_menu_button(driver):
    host = driver.find_element(By.CSS_SELECTOR, "phn-header")
    shadow = host.shadow_root
    models = shadow.find_element(By.CSS_SELECTOR, "phn-p-button-pure")
    driver.execute_script("arguments[0].click();", models)

def build_your_own_button(driver):
    host = driver.find_element(By.CSS_SELECTOR, "phn-header")
    shadow = host.shadow_root
    build_your_own = shadow.find_element(By.CSS_SELECTOR,"a[class='pure-link sc-phn-nd-menu-item'][data-id='vehicle_purchase/mainmenu.vehiclepurchase.configure']")
    driver.execute_script("arguments[0].click();", build_your_own)

def compare_models_button(driver):
    host = driver.find_element(By.CSS_SELECTOR, "phn-header")
    shadow = host.shadow_root
    compare_models = shadow.find_element(By.CSS_SELECTOR,"a[class='pure-link sc-phn-nd-menu-item'][data-id='vehicle_purchase/mainmenu.vehiclepurchase.compare']")
    driver.execute_script("arguments[0].click();", compare_models)

def new_and_used_button(driver):
    host = driver.find_element(By.CSS_SELECTOR, "phn-header")
    shadow = host.shadow_root
    new_and_used = shadow.find_element(By.CSS_SELECTOR,"a[class='pure-link sc-phn-nd-menu-item'][data-id='vehicle_purchase/mainmenu.vehiclepurchase.findvehicles']")
    driver.execute_script("arguments[0].click();", new_and_used)

def current_vehicle_offers_button(driver):
    host = driver.find_element(By.CSS_SELECTOR, "phn-header")
    shadow = host.shadow_root
    current_vehicle_offers = shadow.find_element(By.CSS_SELECTOR,"a[class='pure-link sc-phn-nd-menu-item'][data-id='vehicle_purchase/mainmenu.vehiclepurchase.currentcaroffers']")
    driver.execute_script("arguments[0].click();", current_vehicle_offers)

def certified_button(driver):
    host = driver.find_element(By.CSS_SELECTOR, "phn-header")
    shadow = host.shadow_root
    certified = shadow.find_element(By.CSS_SELECTOR,"a[class='pure-link sc-phn-nd-menu-item'][data-id='vehicle_purchase/mainmenu.vehiclepurchase.approved']")
    driver.execute_script("arguments[0].click();", certified)

def porsche_financial_button(driver):
    host = driver.find_element(By.CSS_SELECTOR, "phn-header")
    shadow = host.shadow_root
    porsche_financial = shadow.find_element(By.CSS_SELECTOR,"a[class='pure-link sc-phn-nd-menu-item'][data-id='vehicle_purchase/mainmenu.vehiclepurchase.financialservices']")
    driver.execute_script("arguments[0].click();", porsche_financial)

def e_mobility_button(driver):
    host = driver.find_element(By.CSS_SELECTOR, "phn-header")
    shadow = host.shadow_root
    e_mobility = shadow.find_element(By.CSS_SELECTOR,"a[class='pure-link sc-phn-nd-menu-item'][data-id='vehicle_purchase/mainmenu.vehiclepurchase.eperformance']")
    driver.execute_script("arguments[0].click();", e_mobility)

def account_button(driver):
    host = driver.find_element(By.CSS_SELECTOR, "phn-header")
    shadow = host.shadow_root
    account = shadow.find_element(By.CSS_SELECTOR,"phn-p-button-pure[class='sc-phn-nd-side-drawer-item hydrated'][data-id='account']")
    driver.execute_script("arguments[0].click();", account)

def log_in_button(driver):
    host = driver.find_element(By.CSS_SELECTOR, "phn-header")
    shadow = host.shadow_root
    log_in = shadow.find_element(By.CSS_SELECTOR, ".login.sc-phn-nd-pcom-login.hydrated")
    driver.execute_script("arguments[0].click();", log_in)

def saved_searches_button(driver):
    host = driver.find_element(By.CSS_SELECTOR, "phn-header")
    shadow = host.shadow_root
    saved_searches = shadow.find_element(By.CSS_SELECTOR,"a[class='pure-link sc-phn-nd-menu-item'][data-id='account/mainmenu.account.savedsearches']")
    driver.execute_script("arguments[0].click();", saved_searches)

def saved_cars_button(driver):
    host = driver.find_element(By.CSS_SELECTOR, "phn-header")
    shadow = host.shadow_root
    saved_cars = shadow.find_element(By.CSS_SELECTOR,"a[class='pure-link sc-phn-nd-menu-item'][data-id='account/mainmenu.account.savedvehicles']")
    driver.execute_script("arguments[0].click();", saved_cars)

def find_connect_services_button(driver):
    host = driver.find_element(By.CSS_SELECTOR, "phn-header")
    shadow = host.shadow_root
    find_connect_services = shadow.find_element(By.CSS_SELECTOR,"a[class='pure-link sc-phn-nd-menu-item'][data-id='account/mainmenu.account.connect']")
    driver.execute_script("arguments[0].click();", find_connect_services)

def contact_and_support_button(driver):
    host = driver.find_element(By.CSS_SELECTOR, "phn-header")
    shadow = host.shadow_root
    contact_and_support = shadow.find_element(By.CSS_SELECTOR,"a[class='pure-link sc-phn-nd-menu-item'][data-id='account/mainmenu.account.contact']")
    driver.execute_script("arguments[0].click();", contact_and_support)

def find_your_porsche_center(driver):
    host = driver.find_element(By.CSS_SELECTOR, "phn-header")
    shadow = host.shadow_root
    find_a_dealer = shadow.find_element(By.CSS_SELECTOR,
                                        "phn-p-button-pure[class='sc-phn-nd-side-drawer-item hydrated'][data-id='find_a_dealer']")
    driver.execute_script("arguments[0].click();", find_a_dealer)

def zip_code1(driver):
    host = driver.find_element(By.CSS_SELECTOR, "phn-header")
    shadow = host.shadow_root
    zip_code = shadow.find_element(By.CSS_SELECTOR,
                                   ".autofocus.sc-phn-nd-autocomplete-search-geolocation-field.hydrated")
    driver.execute_script("arguments[0].click();", zip_code)
    zip_code.send_keys("!@#$%^&*()_+")

def zip_code2(driver):
    host = driver.find_element(By.CSS_SELECTOR, "phn-header")
    shadow = host.shadow_root
    zip_code = shadow.find_element(By.CSS_SELECTOR,
                                   ".autofocus.sc-phn-nd-autocomplete-search-geolocation-field.hydrated")
    driver.execute_script("arguments[0].click();", zip_code)
    zip_code.send_keys("AsDFghjKL")

def zip_code3(driver):
    host = driver.find_element(By.CSS_SELECTOR, "phn-header")
    shadow = host.shadow_root
    zip_code = shadow.find_element(By.CSS_SELECTOR,
                                   ".autofocus.sc-phn-nd-autocomplete-search-geolocation-field.hydrated")
    driver.execute_script("arguments[0].click();", zip_code)
    zip_code.send_keys("123456789")

def career_button(driver):
    host = driver.find_element(By.CSS_SELECTOR, ".pcom-main-footer.hydrated")
    shadow = host.shadow_root
    host2 = shadow.find_element(By.CSS_SELECTOR,
                                "footer:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > pnav-further-links:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > pnav-footer-p-link-pure:nth-child(1)")
    shadow2 = host2.shadow_root
    career = shadow2.find_element(By.CSS_SELECTOR, ".root")
    driver.execute_script("arguments[0].click();", career)

def find_search_window1(driver):
    search_window = driver.find_element(By.XPATH, "//input[@placeholder='Job title, location,..']")
    driver.execute_script("arguments[0].click()", search_window)
    search_window.send_keys("!@#$%^&*()_+")

def find_search_window2(driver):
    search_window = driver.find_element(By.XPATH, "//input[@placeholder='Job title, location,..']")
    driver.execute_script("arguments[0].click()", search_window)
    search_window.send_keys("AsDFghjKL")

def find_search_window3(driver):
    search_window = driver.find_element(By.XPATH, "//input[@placeholder='Job title, location,..']")
    driver.execute_script("arguments[0].click()", search_window)
    search_window.send_keys("123456789")

def find_ask_search_window1(driver):
    search_window = driver.find_element(By.XPATH, "//p-input-search[@placeholder='Search support topics']")
    driver.execute_script("arguments[0].click()", search_window)
    search_window.send_keys("!@#$%^&*()_+")

def find_ask_search_window2(driver):
    search_window = driver.find_element(By.XPATH, "//p-input-search[@placeholder='Search support topics']")
    driver.execute_script("arguments[0].click()", search_window)
    search_window.send_keys("AsDFghjKL")

def find_ask_search_window3(driver):
    search_window = driver.find_element(By.XPATH, "//p-input-search[@placeholder='Search support topics']")
    driver.execute_script("arguments[0].click()", search_window)
    search_window.send_keys("123456789")

def find_owner_manual_button(driver):
    host = driver.find_element(By.CSS_SELECTOR, "p-link[class='hydrated']")
    shadow = host.shadow_root
    owner_manual = shadow.find_element(By.CSS_SELECTOR, ".root")
    driver.execute_script("arguments[0].click();", owner_manual)

def find_vin_search_window_button1(driver):
    host = driver.find_element(By.CSS_SELECTOR, "bod-web-plugin[hif-path='bodWpi2BodSpaHostInterface']")
    shadow = host.shadow_root
    vin_number = shadow.find_element(By.CSS_SELECTOR, "#vin-input-field")
    driver.execute_script("arguments[0].click()", vin_number)
    vin_number.send_keys("A12345H6789QWE001")

def find_vin_search_window_button2(driver):
    host = driver.find_element(By.CSS_SELECTOR, "bod-web-plugin[hif-path='bodWpi2BodSpaHostInterface']")
    shadow = host.shadow_root
    vin_number = shadow.find_element(By.CSS_SELECTOR, "#vin-input-field")
    driver.execute_script("arguments[0].click()", vin_number)
    vin_number.send_keys("!@#$%^&*()_+{}-=+")

def find_vin_search_window_button3(driver):
    host = driver.find_element(By.CSS_SELECTOR, "bod-web-plugin[hif-path='bodWpi2BodSpaHostInterface']")
    shadow = host.shadow_root
    vin_number = shadow.find_element(By.CSS_SELECTOR, "#vin-input-field")
    driver.execute_script("arguments[0].click()", vin_number)
    vin_number.send_keys("12345678912345678")



def check_porsche_url(driver):
    try:
        assert "https://www.porsche.com/usa/" in driver.current_url
        print("Test result: Page URL is: ", driver.current_url)
    except AssertionError:
        print("Test result: Page URL is different", driver.current_url)

def check_build_your_own_url(driver):
    try:
        assert "https://models.porsche.com/en-US/model-start" in driver.current_url
        print("Test result: Page URL is: ", driver.current_url)
    except AssertionError:
        print("Test result: Page URL is different", driver.current_url)

def check_compare_models_url(driver):
    try:
        assert "https://compare.porsche.com/en-US" in driver.current_url
        print("Test result: Page URL is: ", driver.current_url)
    except AssertionError:
        print("Test result: Page URL is different", driver.current_url)

def check_new_and_used_url(driver):
    try:
        assert "https://finder.porsche.com/us/en-US?int_ref=globalnav&int_medium=link&int_id=inventory" in driver.current_url
        print("Test result: Page URL is: ", driver.current_url)
    except AssertionError:
        print("Test result: Page URL is different", driver.current_url)

def check_current_vehicle_offers_url(driver):
    try:
        assert "https://www.porsche.com/usa/accessoriesandservice/porschefinancialservices/pfs-leasing-offers/" in driver.current_url
        print("Test result: Page URL is: ", driver.current_url)
    except AssertionError:
        print("Test result: Page URL is different", driver.current_url)

def check_certified_url(driver):
    try:
        assert "https://www.porsche.com/usa/approved-used/?int_ref=globalnav&int_medium=link&int_id=inventory" in driver.current_url
        print("Test result: Page URL is: ", driver.current_url)
    except AssertionError:
        print("Test result: Page URL is different", driver.current_url)

def check_porsche_financial_url(driver):
    try:
        assert "https://www.porsche.com/usa/accessoriesandservice/porschefinancialservices/" in driver.current_url
        print("Test result: Page URL is: ", driver.current_url)
    except AssertionError:
        print("Test result: Page URL is different", driver.current_url)

def check_e_mobility_url(driver):
    try:
        assert "https://www.porsche.com/usa/aboutporsche/e-performance/" in driver.current_url
        print("Test result: Page URL is: ", driver.current_url)
    except AssertionError:
        print("Test result: Page URL is different", driver.current_url)

def check_log_in_url(driver):
    try:
        assert ('https://identity.porsche.com/u/login/identifier?state'
                '=hKFo2SBSSXRfb3BmbWVvdWtjZ2JMOUtCWk9DSG5zcjJQTl85ZaFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIF9PMXBIMUMxamVWYTVQRllVZW9FQlZCcHo1T1hZanNjo2NpZNkgd01ZMTdNT1hZNHFCYUUyZnByYlY5VXQ0Zk1OM2hqR2w&ui_locales=en') in driver.current_url
        print("Test result: Page URL is: ", driver.current_url)
    except AssertionError:
        print("Test result: Page URL is different", driver.current_url)

def check_saved_searches_url(driver):
    try:
        assert "https://finder.porsche.com/us/en-US/saved-searches" in driver.current_url
        print("Test result: Page URL is: ", driver.current_url)
    except AssertionError:
        print("Test result: Page URL is different", driver.current_url)

def check_saved_cars_url(driver):
    try:
        assert "https://finder.porsche.com/us/en-US/favorites" in driver.current_url
        print("Test result: Page URL is: ", driver.current_url)
    except AssertionError:
        print("Test result: Page URL is different", driver.current_url)

def check_find_connect_services_url(driver):
    try:
        assert "https://connect-store.porsche.com/offer/us/en-US" in driver.current_url
        print("Test result: Page URL is: ", driver.current_url)
    except AssertionError:
        print("Test result: Page URL is different", driver.current_url)

def check_contact_and_support_url(driver):
    try:
        assert "https://ask.porsche.com/us/en-US" in driver.current_url
        print("Test result: Page URL is: ", driver.current_url)
    except AssertionError:
        print("Test result: Page URL is different", driver.current_url)

def check_job_porsche_url(driver):
    try:
        assert "https://www.porsche.com/usa/aboutporsche/jobs/" in driver.current_url
        print("Test result: Page URL is: ", driver.current_url)
    except AssertionError:
        print("Test result: Page URL is different", driver.current_url)

def check_ask_porsche_url(driver):
    try:
        assert "https://ask.porsche.com/us/en-US" in driver.current_url
        print("Test result: Page URL is: ", driver.current_url)
    except AssertionError:
        print("Test result: Page URL is different", driver.current_url)

def check_result_ask_porsche_url1(driver):
    try:
        assert "https://ask.porsche.com/us/en-US/search/?q=!%40%23%24%25%5E%26*()_%2B" in driver.current_url
        print("Test result: Page URL is: ", driver.current_url)
    except AssertionError:
        print("Test result: Page URL is different", driver.current_url)

def check_result_ask_porsche_url2(driver):
    try:
        assert "https://ask.porsche.com/us/en-US/search/?q=AsDFghjKL" in driver.current_url
        print("Test result: Page URL is: ", driver.current_url)
    except AssertionError:
        print("Test result: Page URL is different", driver.current_url)

def check_result_ask_porsche_url3(driver):
    try:
        assert "https://ask.porsche.com/us/en-US/search/?q=123456789" in driver.current_url
        print("Test result: Page URL is: ", driver.current_url)
    except AssertionError:
        print("Test result: Page URL is different", driver.current_url)