
"""
Porsche UI Tests (Selenium + unittest)

Author: Oybek Tashpulatov (aka Moonbek)

Short: UI tests for Porsche USA website in Chrome, Firefox, and Edge,
implemented using Python unittest framework.

What we check:
- Positive flows: Home → Locations & Contact → General contact → Contact Us form,
  plus a successful form submit (with valid data).
- Negative flows: Contact Us form validation (no CAPTCHA, bad data, empty fields,
  invalid Porsche ID / account case).
- Also: cookie banner handling (shadow DOM) and shadow clicks on Porsche UI parts.
"""

import time
import unittest
# import HtmlTestRunner
# import AllureReports

from .help import utils

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ChromeDriverPorsche(unittest.TestCase):
    driver: WebDriver

    def setUp(self):
        # Create driver
        self.driver = utils.create_driver("chrome")

    def tearDown(self):
        # Close driver
        self.driver.quit()

    # ===== POSITIVE TESTS =====

    def test_TC_P_011(self):
        # Print group name
        print("\n========== POSITIVE TESTS (TC_P) ==========")

        driver = self.driver

        # Open home page
        try:
            driver.get("https://www.porsche.com/usa/")
        except Exception as e:
            raise Exception(f"Failed to open home page: {e}")

        # Wait page load
        try:
            utils.wait_body(driver)
        except Exception as e:
            raise Exception(f"Page not loaded: {e}")

        # Check title
        try:
            self.assertIn("Porsche", driver.title)
        except Exception as e:
            raise Exception(f"Title check failed. Title='{driver.title}'. Error: {e}")

        time.sleep(3)

        # Accept cookies
        try:
            utils.accept_cookies_with_keyboard(driver)
            print("✅ Cookies accepted")
        except Exception:
            print("⚠️ Cookies not accepted (skipped)")
        time.sleep(3)

        # Scroll to bottom
        try:
            utils.scroll_to_bottom(driver)
            print("✅ Scrolled to bottom")
        except Exception as e:
            raise Exception(f"Scroll failed: {e}")

        # Click "Get in touch" (shadow)
        try:
            selector = "a.root[href*='locations-and-contact']"

            # Wait shadow element
            utils.wait_shadow(driver, selector, timeout=20)

            clicked = utils.shadow_click(driver, selector)
            if not clicked:
                raise Exception("Link not found (shadow)")
            print("✅ Get in touch clicked")
        except Exception as e:
            raise Exception(f"Click failed: {e}")
        time.sleep(5)

        # Check URL
        try:
            expected_url = "https://www.porsche.com/usa/locations-and-contact/"
            utils.wait_url_starts(driver, expected_url)
            print(f"✅ URL OK: {driver.current_url}")
        except Exception as e:
            raise Exception(f"Wrong URL. Current='{driver.current_url}'. Error: {e}")

        print("✅ TC_P_011 PASSED!")
        

    def test_TC_P_012(self):
        # Print group name
        print("\n========== POSITIVE TESTS (TC_P) ==========")

        driver = self.driver

        # Open page
        try:
            driver.get("https://www.porsche.com/usa/locations-and-contact/")
        except Exception as e:
            raise Exception(f"Failed to open page: {e}")

        # Wait page load
        try:
            utils.wait_body(driver)
        except Exception as e:
            raise Exception(f"Page not loaded: {e}")

        time.sleep(3)

        # Accept cookies
        try:
            utils.accept_cookies_with_keyboard(driver)
            print("✅ Cookies accepted")
        except Exception:
            print("⚠️ Cookies not accepted (skipped)")

        # Check URL
        try:
            expected_url = "https://www.porsche.com/usa/locations-and-contact/"
            utils.wait_url_starts(driver, expected_url)
            print(f"✅ URL OK: {driver.current_url}")
        except Exception as e:
            raise Exception(f"Wrong URL. Current='{driver.current_url}'. Error: {e}")

        # Click "General contact" (shadow)
        try:
            selector = "a[href*='/usa/locations-and-contact/#General-contact']"
            clicked = utils.shadow_click(driver, selector)
            if not clicked:
                raise Exception("Link not found (shadow)")
            print("✅ General contact clicked")
        except Exception as e:
            raise Exception(f"Click failed: {e}")

        # Check block present
        try:
            utils.wait_present(driver, (By.ID, "pcom-General-contact"))
            print("✅ Block present")
        except Exception as e:
            raise Exception(f"Block not present: {e}")

        print("✅ TC_P_012 PASSED!")
        

    def test_TC_P_013(self):
        # Print group name
        print("\n========== POSITIVE TESTS (TC_P) ==========")

        driver = self.driver

        # Open page
        try:
            driver.get("https://www.porsche.com/usa/locations-and-contact/")
        except Exception as e:
            raise Exception(f"Failed to open page: {e}")

        # Wait page load
        try:
            utils.wait_body(driver)
        except Exception as e:
            raise Exception(f"Page not loaded: {e}")

        time.sleep(3)

        # Accept cookies
        try:
            utils.accept_cookies_with_keyboard(driver)
            print("✅ Cookies accepted")
        except Exception:
            print("⚠️ Cookies not accepted (skipped)")

        # Click "General contact" (shadow)
        try:
            selector = "a[href*='/usa/locations-and-contact/#General-contact']"
            clicked = utils.shadow_click(driver, selector)
            if not clicked:
                raise Exception("Link not found (shadow)")
            print("✅ General contact clicked")
        except Exception as e:
            raise Exception(f"Click failed: {e}")

        # Check block visible
        try:
            el = utils.wait_visible(driver, (By.ID, "pcom-General-contact"))
            print(el.text)
        except Exception as e:
            raise Exception(f"Block not visible: {e}")

        print("✅ TC_P_013 PASSED!")
        

    def test_TC_P_014(self):
        # Print group name
        print("\n========== POSITIVE TESTS (TC_P) ==========")

        driver = self.driver

        # Open page
        try:
            driver.get("https://www.porsche.com/usa/locations-and-contact/")
        except Exception as e:
            raise Exception(f"Failed to open page: {e}")

        # Wait page load
        try:
            utils.wait_body(driver)
        except Exception as e:
            raise Exception(f"Page not loaded: {e}")

        time.sleep(3)

        # Accept cookies
        try:
            utils.accept_cookies_with_keyboard(driver)
            print("✅ Cookies accepted")
        except Exception:
            print("⚠️ Cookies not accepted (skipped)")

        # Click "General contact" (shadow)
        try:
            selector = "a[href*='/usa/locations-and-contact/#General-contact']"
            clicked = utils.shadow_click(driver, selector)
            if not clicked:
                raise Exception("Link not found (shadow)")
            print("✅ General contact clicked")
        except Exception as e:
            raise Exception(f"Click failed: {e}")

        # Click contact form link (shadow)
        try:
            link_selector = "a[href*='https://forms.porsche.com/en-us/contactus/']"
            href = utils.shadow_click_and_return_href(driver, link_selector)
            if not href:
                raise Exception("Link not found (shadow)")
            print(f"✅ Contact form clicked. href={href}")
        except Exception as e:
            raise Exception(f"Click failed: {e}")

        # Accept cookies (forms)
        try:
            utils.accept_cookies_with_keyboard(driver)
            print("✅ Cookies accepted (forms)")
        except Exception:
            print("⚠️ Cookies not accepted (forms skipped)")

        # Check form URL
        try:
            utils.wait_url_starts(driver, "https://forms.porsche.com/en-us/contactus/")
            print(f"✅ Form URL OK: {driver.current_url}")
        except Exception as e:
            raise Exception(f"Wrong form URL. Current='{driver.current_url}'. Error: {e}")

        print("✅ TC_P_014 PASSED!")
        

    def test_TC_P_015(self):
        driver = self.driver

        # Open form page
        driver.get("https://forms.porsche.com/en-us/contactus/")
        utils.wait_url_contains(driver, "forms.porsche.com/en-us/contactus")
        time.sleep(7)

        # Accept cookies
        try:
            utils.accept_cookies_with_keyboard(driver)
        except Exception:
            pass

        # Open category dropdown
        input_el = utils.wait_shadow(driver, "input#filter", timeout=20)
        driver.execute_script("arguments[0].click(); arguments[0].focus();", input_el)

        # Select first option
        opt1 = utils.wait_shadow(driver, "#option-1", timeout=20)
        driver.execute_script("arguments[0].click();", opt1)

        # Select next option (keyboard)
        try:
            utils.keyboard_select_next_option(driver)
        except Exception as e:
            print(f"Sales select failed: {e}")

        # Fill subject
        utils.fill_input(driver, (By.XPATH, "//input[@name='subject']"), "Service")

        # Fill message
        body = utils.wait_clickable(driver, (By.CSS_SELECTOR, "textarea[name='contact_message']"))
        body.send_keys("Hello!")

        # Select salutation (keyboard)
        try:
            utils.keyboard_select_next_option(driver)
        except Exception as e:
            print(f"Salutation select failed: {e}")

        # Select title (keyboard)
        try:
            utils.keyboard_select_next_option(driver)
        except Exception as e:
            print(f"Title select failed: {e}")

        # Fill personal data
        utils.fill_input(driver, (By.XPATH, "//input[@name='firstname']"), "David")
        utils.fill_input(driver, (By.XPATH, "//input[@name='middlename']"), "Maison")
        utils.fill_input(driver, (By.XPATH, "//input[@name='lastname']"), "Rodgers")
        utils.fill_input(driver, (By.XPATH, "//input[@name='suffix']"), "Sr")
        utils.fill_input(driver, (By.XPATH, "//input[@name='emailstandard']"), "pink@floyd.com")
        utils.fill_input(driver, (By.XPATH, "//input[@name='phone']"), "123-222-7890")

        time.sleep(3)

        # Select "No account"
        no_account_locator = (
            By.XPATH,
            "//input[@type='radio' and @name='myporscheaccount' and "
            "@aria-label='No, I do not have a My Porsche account.']"
        )
        radio = utils.wait_clickable(driver, no_account_locator)
        driver.execute_script("arguments[0].click();", radio)

        time.sleep(3)

        # Try captcha (keyboard)
        try:
            utils.keyboard_tab_times_then_space(driver, times=5)
            print("✅ Captcha try done")
        except Exception as e:
            print(f"Captcha step failed: {e}")

        time.sleep(7)

        # Click submit
        submit_locator = (
            By.XPATH,
            "//faas-p-button[contains(@class,'hydrated') and normalize-space(.)='Submit']"
        )
        submit_btn = utils.wait_clickable(driver, submit_locator, timeout=20)
        submit_btn.click()

        # Check success message
        success_locator = (By.CSS_SELECTOR, "div.component-formcopytext.span-4 faas-p-text.hydrated")
        el = utils.wait_visible(driver, success_locator, timeout=30)
        print(el.text)

        if "Your message has been successfully sent!" not in el.text:
            raise Exception(f"Success text not found. Actual='{el.text}'")

        print("✅ TC_P_015 PASSED!")
        

    # ===== NEGATIVE TESTS =====

    def test_TC_N_011(self):
        # Print group name
        print("\n========== NEGATIVE TESTS (TC_N) ==========")

        driver = self.driver

        # Open home page
        try:
            driver.get("https://www.porsche.com/usa/")
        except Exception as e:
            raise Exception(f"Failed to open home page: {e}")

        # Wait page load
        try:
            utils.wait_body(driver)
        except Exception as e:
            raise Exception(f"Page not loaded: {e}")

        # Check title
        try:
            self.assertIn("Porsche", driver.title)
        except Exception as e:
            raise Exception(f"Title check failed. Title='{driver.title}'. Error: {e}")

        time.sleep(3)

        # Accept cookies
        try:
            utils.accept_cookies_with_keyboard(driver)
            print("✅ Cookies accepted")
        except Exception:
            print("⚠️ Cookies not accepted (skipped)")
        time.sleep(3)

        # Scroll to bottom
        try:
            utils.scroll_to_bottom(driver)
            print("✅ Scrolled to bottom")
        except Exception as e:
            raise Exception(f"Scroll failed: {e}")

        # Click "Get in touch" (shadow)
        try:
            selector = "a.root[href*='locations-and-contact']"
            clicked = utils.shadow_click(driver, selector)
            if not clicked:
                raise Exception("Link not found (shadow)")
            print("✅ Get in touch clicked")
        except Exception as e:
            raise Exception(f"Click failed: {e}")

        # Check URL
        try:
            expected_url = "https://www.porsche.com/usa/locations-and-contact/"
            utils.wait_url_starts(driver, expected_url)
            print(f"✅ URL OK: {driver.current_url}")
        except Exception as e:
            raise Exception(f"Wrong URL. Current='{driver.current_url}'. Error: {e}")

        time.sleep(3)

        # Click "General contact" (shadow)
        try:
            selector = "a[href*='/usa/locations-and-contact/#General-contact']"
            clicked = utils.shadow_click(driver, selector)
            if not clicked:
                raise Exception("Link not found (shadow)")
            print("✅ General contact clicked")
        except Exception as e:
            raise Exception(f"Click failed: {e}")

        # Get section
        try:
            section = utils.wait_visible(driver, (By.ID, "pcom-General-contact"))
            print("✅ Section visible")
        except Exception as e:
            raise Exception(f"Section not visible: {e}")

        time.sleep(5)

        # Click empty space
        try:
            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", section)
            time.sleep(2)

            driver.execute_script(
                """
                const el = arguments[0];
                const r = el.getBoundingClientRect();
                const x = r.left + 20;
                const y = r.top + 20;
                document.elementFromPoint(x, y).click();
                """,
                section
            )
            print("✅ Empty space clicked")
        except Exception as e:
            raise Exception(f"Click failed: {e}")

        time.sleep(3)

        # Select all (CMD+A)
        try:
            driver.switch_to.active_element.send_keys(Keys.COMMAND, "a")
            print("✅ Select all done")
        except Exception as e:
            raise Exception(f"Select all failed: {e}")

        time.sleep(5)

        # Click contact form (shadow)
        try:
            selector = "a[href*='https://forms.porsche.com/en-us/contactus/']"
            href = utils.shadow_click_and_return_href(driver, selector)
            if not href:
                raise Exception("Link not found (shadow)")
            print(f"✅ Contact form clicked. href={href}")
        except Exception as e:
            raise Exception(f"Click failed: {e}")

        time.sleep(7)

        # Check form URL
        try:
            utils.wait_url_contains(driver, "forms.porsche.com/en-us/contactus")
            print(f"✅ Form opened: {driver.current_url}")
        except Exception as e:
            raise Exception(f"Form not opened: {e}")

        print("✅ TC_N_011 PASSED!")
        

    def test_TC_N_012(self):
        # Print group name
        print("\n========== NEGATIVE TESTS (TC_N) ==========")

        driver = self.driver

        # Open form page
        try:
            driver.get("https://forms.porsche.com/en-us/contactus/")
        except Exception as e:
            raise Exception(f"Failed to open form page: {e}")

        time.sleep(3)

        # Accept cookies
        try:
            utils.accept_cookies_with_keyboard(driver)
            print("✅ Cookies accepted")
        except Exception:
            print("⚠️ Cookies not accepted (skipped)")
        time.sleep(5)

        # Open category dropdown
        try:
            input_el = utils.wait_shadow(driver, "input#filter", timeout=20)
            driver.execute_script("arguments[0].click(); arguments[0].focus();", input_el)
            print("✅ Category opened")
        except Exception as e:
            raise Exception(f"Category open failed: {e}")

        # Select first option
        try:
            opt1 = utils.wait_shadow(driver, "#option-1", timeout=20)
            driver.execute_script("arguments[0].click();", opt1)
            print("✅ First option selected")
        except Exception as e:
            raise Exception(f"Option select failed: {e}")

        # Select next option (keyboard)
        try:
            utils.keyboard_select_next_option(driver)
            print("✅ Next option selected")
        except Exception as e:
            raise Exception(f"Keyboard select failed: {e}")

        # Fill subject
        try:
            utils.fill_input(driver, (By.XPATH, "//input[@name='subject']"), "Service")
            print("✅ Subject filled")
        except Exception as e:
            raise Exception(f"Subject fill failed: {e}")

        # Fill message
        try:
            body = utils.wait_clickable(driver, (By.CSS_SELECTOR, "textarea[name='contact_message']"))
            body.clear()
            body.send_keys("Hello!")
            print("✅ Message filled")
        except Exception as e:
            raise Exception(f"Message fill failed: {e}")

        # Select salutation (keyboard)
        try:
            utils.keyboard_select_next_option(driver)
            print("✅ Salutation selected")
        except Exception as e:
            raise Exception(f"Salutation select failed: {e}")

        # Select title (keyboard)
        try:
            utils.keyboard_select_next_option(driver)
            print("✅ Title selected")
        except Exception as e:
            raise Exception(f"Title select failed: {e}")

        # Fill personal data
        try:
            utils.fill_input(driver, (By.XPATH, "//input[@name='firstname']"), "David")
            utils.fill_input(driver, (By.XPATH, "//input[@name='middlename']"), "Maison")
            utils.fill_input(driver, (By.XPATH, "//input[@name='lastname']"), "Rodgers")
            utils.fill_input(driver, (By.XPATH, "//input[@name='suffix']"), "Sr")
            utils.fill_input(driver, (By.XPATH, "//input[@name='emailstandard']"), "pink@floyd.com")
            utils.fill_input(driver, (By.XPATH, "//input[@name='phone']"), "123-222-7890")
            print("✅ Personal data filled")
        except Exception as e:
            raise Exception(f"Personal data fill failed: {e}")

        time.sleep(3)

        # Select "No account"
        try:
            no_account_locator = (
                By.XPATH,
                "//input[@type='radio' and @name='myporscheaccount' and "
                "@aria-label='No, I do not have a My Porsche account.']"
            )
            radio = utils.wait_clickable(driver, no_account_locator)
            driver.execute_script("arguments[0].click();", radio)
            print("✅ No account selected")
        except Exception as e:
            raise Exception(f"No account select failed: {e}")

        # Leave captcha empty
        print("✅ Captcha left empty")

        time.sleep(2)

        # Click submit
        try:
            submit_locator = (
                By.XPATH,
                "//faas-p-button[contains(@class,'hydrated') and normalize-space(.)='Submit']"
            )
            submit_btn = utils.wait_clickable(driver, submit_locator, timeout=20)
            submit_btn.click()
            print("✅ Submit clicked")
        except Exception as e:
            raise Exception(f"Submit click failed: {e}")

        time.sleep(5)

        # Check validation
        try:
            success_locator = (By.CSS_SELECTOR, "div.component-formcopytext.span-4 faas-p-text.hydrated")
            try:
                el = utils.wait_visible(driver, success_locator, timeout=6)
                if "Your message has been successfully sent!" in el.text:
                    raise Exception("Unexpected success (captcha was empty).")
            except Exception:
                pass

            try:
                error_el = utils.wait_visible(
                    driver,
                    (By.XPATH, "//*[contains(text(),'Verification was not successful')]"),
                    timeout=10
                )
                print(f"✅ Validation shown: {error_el.text}")
                utils.take_screenshot(driver, folder="screenshots_Wiki")
            except Exception as e:
                raise Exception(f"Validation text not found: {e}")

        except Exception as e:
            raise Exception(f"Validation check failed: {e}")

        print("✅ TC_N_012 PASSED!")
        

    def test_TC_N_013(self):
        # Print group name
        print("\n========== NEGATIVE TESTS (TC_N) ==========")

        driver = self.driver

        # Open form page
        try:
            driver.get("https://forms.porsche.com/en-us/contactus/")
        except Exception as e:
            raise Exception(f"Failed to open form page: {e}")

        time.sleep(3)

        # Accept cookies
        try:
            utils.accept_cookies_with_keyboard(driver)
            print("✅ Cookies accepted")
        except Exception:
            print("⚠️ Cookies not accepted (skipped)")
        time.sleep(5)

        # Open category dropdown
        try:
            input_el = utils.wait_shadow(driver, "input#filter", timeout=20)
            driver.execute_script("arguments[0].click(); arguments[0].focus();", input_el)
            print("✅ Category opened")
        except Exception as e:
            raise Exception(f"Category open failed: {e}")

        # Select first option
        try:
            opt1 = utils.wait_shadow(driver, "#option-1", timeout=20)
            driver.execute_script("arguments[0].click();", opt1)
            print("✅ First option selected")
        except Exception as e:
            raise Exception(f"Option select failed: {e}")

        # Select next option (keyboard)
        try:
            utils.keyboard_select_next_option(driver)
            print("✅ Next option selected")
        except Exception as e:
            raise Exception(f"Keyboard select failed: {e}")

        # Fill subject
        try:
            utils.fill_input(driver, (By.XPATH, "//input[@name='subject']"), "Service")
            print("✅ Subject filled")
        except Exception as e:
            raise Exception(f"Subject fill failed: {e}")

        # Fill message
        try:
            body = utils.wait_clickable(driver, (By.CSS_SELECTOR, "textarea[name='contact_message']"))
            body.clear()
            body.send_keys("Hello!")
            print("✅ Message filled")
        except Exception as e:
            raise Exception(f"Message fill failed: {e}")

        # Select salutation (keyboard)
        try:
            utils.keyboard_select_next_option(driver)
            print("✅ Salutation selected")
        except Exception as e:
            raise Exception(f"Salutation select failed: {e}")

        # Select title (keyboard)
        try:
            utils.keyboard_select_next_option(driver)
            print("✅ Title selected")
        except Exception as e:
            raise Exception(f"Title select failed: {e}")

        # Fill personal data
        try:
            utils.fill_input(driver, (By.XPATH, "//input[@name='firstname']"), "David")
            utils.fill_input(driver, (By.XPATH, "//input[@name='middlename']"), "Maison")
            utils.fill_input(driver, (By.XPATH, "//input[@name='lastname']"), "Rodgers")
            utils.fill_input(driver, (By.XPATH, "//input[@name='suffix']"), "Sr")
            utils.fill_input(driver, (By.XPATH, "//input[@name='emailstandard']"), "pink@floyd.com")
            utils.fill_input(driver, (By.XPATH, "//input[@name='phone']"), "123-222-7890")
            print("✅ Personal data filled")
        except Exception as e:
            raise Exception(f"Personal data fill failed: {e}")

        time.sleep(3)

        # Select "Yes account"
        try:
            yes_locator = (
                By.XPATH,
                "//input[@type='radio' and @name='myporscheaccount' and "
                "@aria-label='Yes, I have a My Porsche account.']"
            )
            radio = utils.wait_clickable(driver, yes_locator)
            radio.click()
            print("✅ Yes account selected")
        except Exception:
            print("⚠️ Yes account not selected (continue)")

        time.sleep(3)

        # Fill Porsche ID
        try:
            porsche_id_locator = (By.XPATH, "//input[@name='porscheid']")
            utils.wait_visible(driver, porsche_id_locator, timeout=20)
            utils.fill_input(driver, porsche_id_locator, "pink@floyd.")
            print("✅ Porsche ID filled")
        except Exception as e:
            raise Exception(f"Porsche ID step failed: {e}")

        time.sleep(3)

        # Try captcha (keyboard)
        try:
            utils.keyboard_tab_times_then_space(driver, times=4)
            print("✅ Captcha try done")
        except Exception as e:
            print(f"Captcha step failed: {e}")

        time.sleep(7)

        # Click submit
        try:
            submit_locator = (
                By.XPATH,
                "//faas-p-button[contains(@class,'hydrated') and normalize-space(.)='Submit']"
            )
            submit_btn = utils.wait_clickable(driver, submit_locator, timeout=20)
            submit_btn.click()
            print("✅ Submit clicked")
        except Exception as e:
            raise Exception(f"Submit click failed: {e}")

        time.sleep(5)

        # Check validation
        try:
            success_locator = (By.CSS_SELECTOR, "div.component-formcopytext.span-4 faas-p-text.hydrated")

            try:
                el = utils.wait_visible(driver, success_locator, timeout=6)
                if "Your message has been successfully sent!" in el.text:
                    utils.take_screenshot(driver, folder="screenshots_Wiki")
                    raise Exception("Unexpected success in negative test.")
            except Exception as e:
                if "Unexpected success" in str(e):
                    raise
                print("✅ Success not shown")

            try:
                utils.take_screenshot(driver, folder="screenshots_Wiki")

                if "error" in driver.current_url.lower():
                    print(f"✅ Error page opened: {driver.current_url}")
                else:
                    invalid_mark = driver.find_elements(
                        By.XPATH,
                        "//input[@name='porscheid' and "
                        "(@aria-invalid='true' or contains(@class,'error') or contains(@class,'invalid'))]"
                    )
                    described_by = driver.find_elements(
                        By.XPATH,
                        "//input[@name='porscheid' and string-length(@aria-describedby) > 0]"
                    )

                    if len(invalid_mark) > 0 or len(described_by) > 0:
                        print("✅ Porsche ID validation shown")
                    else:
                        raise Exception("No Porsche ID validation found")

            except Exception as e:
                utils.take_screenshot(driver, folder="screenshots_Wiki")
                raise Exception(f"Porsche ID validation missing: {e}")

        except Exception as e:
            raise Exception(f"Validation check failed: {e}")

        print("✅ TC_N_013 PASSED!")
        

    def test_TC_N_014(self):
        # Print group name
        print("\n========== NEGATIVE TESTS (TC_N) ==========")

        driver = self.driver

        # Open form page
        try:
            driver.get("https://forms.porsche.com/en-us/contactus/")
        except Exception as e:
            raise Exception(f"Failed to open form page: {e}")

        time.sleep(3)

        # Accept cookies
        try:
            utils.accept_cookies_with_keyboard(driver)
            print("✅ Cookies accepted")
        except Exception:
            print("⚠️ Cookies not accepted (skipped)")
        time.sleep(5)

        # Open category dropdown
        try:
            input_el = utils.wait_shadow(driver, "input#filter", timeout=20)
            driver.execute_script("arguments[0].click(); arguments[0].focus();", input_el)
            print("✅ Category opened")
        except Exception as e:
            raise Exception(f"Category open failed: {e}")

        # Select first option
        try:
            opt1 = utils.wait_shadow(driver, "#option-1", timeout=20)
            driver.execute_script("arguments[0].click();", opt1)
            print("✅ First option selected")
        except Exception as e:
            raise Exception(f"Option select failed: {e}")

        # Select next option (keyboard)
        try:
            utils.keyboard_select_next_option(driver)
            print("✅ Next option selected")
        except Exception as e:
            raise Exception(f"Keyboard select failed: {e}")

        # Fill subject (bad data)
        try:
            utils.fill_input(driver, (By.XPATH, "//input[@name='subject']"), "!!!@@@###")
            print("✅ Subject filled (bad)")
        except Exception as e:
            raise Exception(f"Subject fill failed: {e}")

        # Fill message (bad data)
        try:
            body = utils.wait_clickable(driver, (By.CSS_SELECTOR, "textarea[name='contact_message']"))
            body.clear()
            body.send_keys("1")
            print("✅ Message filled (bad)")
        except Exception as e:
            raise Exception(f"Message fill failed: {e}")

        # Select salutation (keyboard)
        try:
            utils.keyboard_select_next_option(driver)
            print("✅ Salutation selected")
        except Exception as e:
            raise Exception(f"Salutation select failed: {e}")

        # Select title (keyboard)
        try:
            utils.keyboard_select_next_option(driver)
            print("✅ Title selected")
        except Exception as e:
            raise Exception(f"Title select failed: {e}")

        # Fill personal data (bad)
        try:
            utils.fill_input(driver, (By.XPATH, "//input[@name='firstname']"), "12345")
            utils.fill_input(driver, (By.XPATH, "//input[@name='middlename']"), "!!!")
            utils.fill_input(driver, (By.XPATH, "//input[@name='lastname']"), "@@@")
            utils.fill_input(driver, (By.XPATH, "//input[@name='suffix']"), "%%%%")
            utils.fill_input(driver, (By.XPATH, "//input[@name='emailstandard']"), "pink@")
            utils.fill_input(driver, (By.XPATH, "//input[@name='phone']"), "abc")
            print("✅ Personal data filled (bad)")
        except Exception as e:
            raise Exception(f"Personal data fill failed: {e}")

        time.sleep(2)

        # Select "No account"
        try:
            no_account_locator = (
                By.XPATH,
                "//input[@type='radio' and @name='myporscheaccount' and "
                "@aria-label='No, I do not have a My Porsche account.']"
            )
            radio = utils.wait_clickable(driver, no_account_locator)
            driver.execute_script("arguments[0].click();", radio)
            print("✅ No account selected")
        except Exception as e:
            raise Exception(f"No account select failed: {e}")

        time.sleep(2)

        # Try captcha (keyboard)
        try:
            utils.keyboard_tab_times_then_space(driver, times=5)
            print("✅ Captcha try done")
        except Exception as e:
            print(f"Captcha step failed: {e}")

        time.sleep(7)

        # Click submit
        try:
            submit_locator = (
                By.XPATH,
                "//faas-p-button[contains(@class,'hydrated') and normalize-space(.)='Submit']"
            )
            submit_btn = utils.wait_clickable(driver, submit_locator, timeout=20)
            submit_btn.click()
            print("✅ Submit clicked")
        except Exception as e:
            raise Exception(f"Submit click failed: {e}")

        time.sleep(4)

        # Check validation
        try:
            success_locator = (By.CSS_SELECTOR, "div.component-formcopytext.span-4 faas-p-text.hydrated")
            try:
                el = utils.wait_visible(driver, success_locator, timeout=4)
                if "Your message has been successfully sent!" in el.text:
                    raise Exception("Unexpected success with bad data.")
            except Exception:
                pass

            invalid_fields = driver.find_elements(By.CSS_SELECTOR, "[aria-invalid='true']")

            validation_text_el = None
            try:
                validation_text_el = utils.wait_visible(
                    driver,
                    (By.XPATH,
                     "//*[contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'email') "
                     "or contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'phone') "
                     "or contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'invalid')]"),
                    timeout=6
                )
            except Exception:
                pass

            if len(invalid_fields) == 0 and validation_text_el is None:
                raise Exception("No validation shown")

            if len(invalid_fields) > 0:
                print(f"✅ Invalid fields: {len(invalid_fields)}")

            if validation_text_el is not None:
                print(f"✅ Validation text: {validation_text_el.text}")

            utils.take_screenshot(driver, folder="screenshots_Wiki")

        except Exception as e:
            raise Exception(f"Validation check failed: {e}")

        print("✅ TC_N_014 PASSED!")
        

    def test_TC_N_015(self):
        # Print group name
        print("\n========== NEGATIVE TESTS (TC_N) ==========")

        driver = self.driver

        # Open form page
        try:
            driver.get("https://forms.porsche.com/en-us/contactus/")
        except Exception as e:
            raise Exception(f"Failed to open form page: {e}")

        time.sleep(3)

        # Accept cookies
        try:
            utils.accept_cookies_with_keyboard(driver)
            print("✅ Cookies accepted")
        except Exception:
            print("⚠️ Cookies not accepted (skipped)")
        time.sleep(5)

        # Select "No account"
        try:
            no_account_locator = (
                By.XPATH,
                "//input[@type='radio' and @name='myporscheaccount' and "
                "@aria-label='No, I do not have a My Porsche account.']"
            )
            radio = utils.wait_clickable(driver, no_account_locator)

            # Scroll to radio button
            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", radio)
            time.sleep(1)
            driver.execute_script("window.scrollBy(0, -120);")

            driver.execute_script("arguments[0].click();", radio)
            print("✅ No account selected")
        except Exception as e:
            raise Exception(f"No account select failed: {e}")

        time.sleep(5)

        # Try captcha (keyboard)
        try:
            utils.keyboard_tab_times_then_space(driver, times=5)
            print("✅ Captcha try done")
        except Exception as e:
            print(f"⚠️ Captcha step failed (ignored): {e}")

        time.sleep(5)

        # Click submit
        try:
            submit_locator = (
                By.XPATH,
                "//faas-p-button[contains(@class,'hydrated') and normalize-space(.)='Submit']"
            )
            submit_btn = utils.wait_clickable(driver, submit_locator, timeout=10)
            submit_btn.click()
            print("✅ Submit clicked")
        except Exception as e:
            raise Exception(f"Submit click failed: {e}")

        time.sleep(5)

        # Check validation
        try:
            success_locator = (By.CSS_SELECTOR, "div.component-formcopytext.span-4 faas-p-text.hydrated")
            try:
                el = utils.wait_visible(driver, success_locator, timeout=4)
                if "Your message has been successfully sent!" in el.text:
                    raise Exception("Unexpected success with empty fields.")
            except Exception:
                pass

            invalid_fields = driver.find_elements(By.CSS_SELECTOR, "[aria-invalid='true']")

            required_text_el = None
            try:
                required_text_el = utils.wait_visible(
                    driver,
                    (By.XPATH,
                     "//*[contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'required') "
                     "or contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'please fill') "
                     "or contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'mandatory')]"),
                    timeout=8
                )
            except Exception:
                pass

            if len(invalid_fields) == 0 and required_text_el is None:
                raise Exception("No validation shown")

            if len(invalid_fields) > 0:
                print(f"✅ Invalid fields: {len(invalid_fields)}")

            if required_text_el is not None:
                print(f"✅ Required text: {required_text_el.text}")

            utils.take_screenshot(driver, folder="screenshots_Wiki")

        except Exception as e:
            raise Exception(f"Validation check failed: {e}")

        print("✅ TC_N_015 PASSED!")
        

class FirefoxDriverPorsche(unittest.TestCase):
    driver: WebDriver

    def setUp(self):
        # Create driver
        self.driver = utils.create_driver("firefox")

    def tearDown(self):
        # Close driver
        self.driver.quit()

    # ===== POSITIVE TESTS =====

    def test_TC_P_011(self):
        print("\n========== POSITIVE TESTS (TC_P) ==========")

        driver = self.driver

        # Open home page
        try:
            driver.get("https://www.porsche.com/usa/")
        except Exception as e:
            raise Exception(f"Failed to open home page: {e}")

        # Wait page load
        try:
            utils.wait_body(driver)
        except Exception as e:
            raise Exception(f"Page not loaded: {e}")

        # Check title
        try:
            self.assertIn("Porsche", driver.title)
        except Exception as e:
            raise Exception(f"Title check failed. Title='{driver.title}'. Error: {e}")

        time.sleep(3)

        # Accept cookies (UC shadow)
        try:
            target = driver.execute_script(
                """
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
                """
            )
            if target:
                driver.execute_script("arguments[0].click();", target)
                print("✅ Cookies accepted")
            else:
                print("ℹ️ Cookies not shown")
        except Exception:
            print("ℹ️ Cookies not shown")

        time.sleep(2)

        # Scroll to bottom
        try:
            utils.scroll_to_bottom(driver)
            print("✅ Scrolled to bottom")
        except Exception as e:
            raise Exception(f"Scroll failed: {e}")

        # Click "Get in touch" (shadow)
        try:
            selector = "a.root[href*='locations-and-contact']"
            utils.wait_shadow(driver, selector, timeout=20)

            clicked = utils.shadow_click(driver, selector)
            if not clicked:
                raise Exception("Link not found (shadow)")
            print("✅ Get in touch clicked")
        except Exception as e:
            raise Exception(f"Click failed: {e}")

        # Check URL
        try:
            expected = "https://www.porsche.com/usa/locations-and-contact/"
            utils.wait_url_starts(driver, expected)
            print(f"✅ URL OK: {driver.current_url}")
        except Exception as e:
            raise Exception(f"Wrong URL. Current='{driver.current_url}'. Error: {e}")

        print("✅ TC_P_011 PASSED!")
        

    def test_TC_P_012(self):
        print("\n========== POSITIVE TESTS (TC_P) ==========")

        driver = self.driver

        # Open page
        try:
            driver.get("https://www.porsche.com/usa/locations-and-contact/")
        except Exception as e:
            raise Exception(f"Failed to open page: {e}")

        # Wait page load
        try:
            utils.wait_body(driver)
        except Exception as e:
            raise Exception(f"Page not loaded: {e}")

        time.sleep(5)

        # Accept cookies (UC shadow)
        try:
            wait = WebDriverWait(driver, 5)
            layer = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "uc-layer2")))
            shadow1 = utils.get_shadow(driver, layer)

            modal = shadow1.find_element(By.CSS_SELECTOR, "uc-p-modal.modal.hydrated")
            footer = modal.find_element(By.CSS_SELECTOR, "uc-footer.footer")
            shadow2 = utils.get_shadow(driver, footer)

            container = shadow2.find_element(By.CSS_SELECTOR, "div.button-container.reverse.same-size")
            accept_component = container.find_element(By.CSS_SELECTOR, "uc-p-button.accept.hydrated")

            shadow3 = utils.get_shadow(driver, accept_component)
            accept_btn = shadow3.find_element(By.CSS_SELECTOR, "button.root")

            driver.execute_script("arguments[0].click();", accept_btn)
            print("✅ Cookies accepted")
        except Exception:
            print("ℹ️ Cookies not shown")

        time.sleep(2)

        # Check URL
        try:
            expected = "https://www.porsche.com/usa/locations-and-contact/"
            utils.wait_url_starts(driver, expected)
            print(f"✅ URL OK: {driver.current_url}")
        except Exception as e:
            raise Exception(f"Wrong URL. Current='{driver.current_url}'. Error: {e}")

        # Click "General contact" (shadow)
        try:
            selector = "a[href*='/usa/locations-and-contact/#General-contact']"
            clicked = utils.shadow_click(driver, selector)
            if not clicked:
                raise Exception("Link not found (shadow)")
            print("✅ General contact clicked")
        except Exception as e:
            raise Exception(f"Click failed: {e}")

        # Check block present
        try:
            utils.wait_present(driver, (By.ID, "pcom-General-contact"))
            print("✅ Block present")
        except Exception as e:
            raise Exception(f"Block not present: {e}")

        time.sleep(7)
        print("✅ TC_P_012 PASSED!")
        

    def test_TC_P_013(self):
        print("\n========== POSITIVE TESTS (TC_P) ==========")

        driver = self.driver

        # Open page
        try:
            driver.get("https://www.porsche.com/usa/locations-and-contact/")
        except Exception as e:
            raise Exception(f"Failed to open page: {e}")

        # Wait page load
        try:
            utils.wait_body(driver)
        except Exception as e:
            raise Exception(f"Page not loaded: {e}")

        time.sleep(3)

        # Accept cookies (UC shadow)
        try:
            wait = WebDriverWait(driver, 5)
            layer = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "uc-layer2")))
            shadow1 = utils.get_shadow(driver, layer)

            modal = shadow1.find_element(By.CSS_SELECTOR, "uc-p-modal.modal.hydrated")
            footer = modal.find_element(By.CSS_SELECTOR, "uc-footer.footer")
            shadow2 = utils.get_shadow(driver, footer)

            container = shadow2.find_element(By.CSS_SELECTOR, "div.button-container.reverse.same-size")
            accept_component = container.find_element(By.CSS_SELECTOR, "uc-p-button.accept.hydrated")

            shadow3 = utils.get_shadow(driver, accept_component)
            accept_btn = shadow3.find_element(By.CSS_SELECTOR, "button.root")

            driver.execute_script("arguments[0].click();", accept_btn)
            print("✅ Cookies accepted")
        except Exception:
            print("ℹ️ Cookies not shown")

        time.sleep(2)

        # Click "General contact" (shadow)
        try:
            selector = "a[href*='/usa/locations-and-contact/#General-contact']"
            clicked = utils.shadow_click(driver, selector)
            if not clicked:
                raise Exception("Link not found (shadow)")
            print("✅ General contact clicked")
        except Exception as e:
            raise Exception(f"Click failed: {e}")

        # Check block visible
        try:
            el = utils.wait_visible(driver, (By.ID, "pcom-General-contact"))
            print(el.text)
        except Exception as e:
            raise Exception(f"Block not visible: {e}")

        print("✅ TC_P_013 PASSED!")
        

    def test_TC_P_014(self):
        print("\n========== POSITIVE TESTS (TC_P) ==========")

        driver = self.driver

        # Open page
        try:
            self.driver.get("https://www.porsche.com/usa/locations-and-contact/")
        except Exception as e:
            raise Exception(f"Failed to open Locations & Contact page: {e}")

        # Wait page load
        try:
            utils.wait_body(self.driver)
        except Exception as e:
            raise Exception(f"Body not loaded on Locations & Contact page: {e}")

        time.sleep(5)

        # Cookies Banner (shadow DOM - UC) - 2nd variant with waits
        try:
            wait = WebDriverWait(self.driver, 5)

            layer = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "uc-layer2")))
            shadow1 = utils.get_shadow(self.driver, layer)

            modal = shadow1.find_element(By.CSS_SELECTOR, "uc-p-modal.modal.hydrated")
            footer = modal.find_element(By.CSS_SELECTOR, "uc-footer.footer")
            shadow2 = utils.get_shadow(self.driver, footer)

            container = shadow2.find_element(By.CSS_SELECTOR, "div.button-container.reverse.same-size")
            accept_component = container.find_element(By.CSS_SELECTOR, "uc-p-button.accept.hydrated")

            shadow3 = utils.get_shadow(self.driver, accept_component)
            accept_btn = shadow3.find_element(By.CSS_SELECTOR, "button.root")

            self.driver.execute_script("arguments[0].click();", accept_btn)
            print("✅ Cookies accepted")

        except Exception:
            print("ℹ️ Cookies banner not shown / already accepted")

        time.sleep(5)

        # Click General contact link (shadow DOM)
        try:
            selector = "a[href*='/usa/locations-and-contact/#General-contact']"
            clicked = utils.shadow_click(self.driver, selector)
            if not clicked:
                raise Exception("General contact link not found (shadow DOM)")
            print("✅ General contact link clicked")
        except Exception as e:
            raise Exception(f"Failed to click General contact link: {e}")
        time.sleep(5)
        # Verify and Click "Go to contact form"
        try:
            host = utils.wait_visible(self.driver,
                                      (By.CSS_SELECTOR, "p-link[href*='forms.porsche.com/en-us/contactus']"))
            shadow = host.shadow_root
            print(f"✅ Button '{host.text}' visible")
            cta = shadow.find_element(By.CSS_SELECTOR, "a.root[href*='forms.porsche.com/en-us/contactus/']")
            self.driver.execute_script("arguments[0].click();", cta)
            print("✅ Button 'Go to contact form' clicked")

        except Exception as e:
            print("'Go to contact from' not visible and not clicked")
        time.sleep(5)

        # Cookies Banner on forms page (shadow DOM - UC) - 2nd variant with waits
        try:
            wait = WebDriverWait(self.driver, 5)

            layer = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "uc-layer2")))
            shadow1 = utils.get_shadow(self.driver, layer)

            modal = shadow1.find_element(By.CSS_SELECTOR, "uc-p-modal.modal.hydrated")
            footer = modal.find_element(By.CSS_SELECTOR, "uc-footer.footer")
            shadow2 = utils.get_shadow(self.driver, footer)

            container = shadow2.find_element(By.CSS_SELECTOR, "div.button-container.reverse.same-size")
            accept_component = container.find_element(By.CSS_SELECTOR, "uc-p-button.accept.hydrated")

            shadow3 = utils.get_shadow(self.driver, accept_component)
            accept_btn = shadow3.find_element(By.CSS_SELECTOR, "button.root")

            self.driver.execute_script("arguments[0].click();", accept_btn)
            print("✅ Cookies accepted (forms)")
        except Exception:
            print("ℹ️ Cookies banner not shown / already accepted (forms)")
        time.sleep(5)


        # Check form URL
        try:
            expected_url = "https://forms.porsche.com/en-us/contactus/"
            utils.wait_url_starts(self.driver, expected_url)
            print("✅ 'Contact Us' page loaded and URL OK: ", expected_url)
        except Exception as e:
            raise Exception(f"Wrong URL. Current: {self.driver.current_url}. Error: {e}")
        time.sleep(5)

        print("✅ TC_P_014 PASSED!")
        

    def test_TC_P_015(self):
        driver = self.driver

        # Open form page
        driver.get("https://forms.porsche.com/en-us/contactus/")
        utils.wait_url_contains(driver, "forms.porsche.com/en-us/contactus")
        time.sleep(7)

        # Accept cookies (UC shadow)
        try:
            wait = WebDriverWait(driver, 5)
            layer = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "uc-layer2")))
            shadow1 = utils.get_shadow(driver, layer)

            modal = shadow1.find_element(By.CSS_SELECTOR, "uc-p-modal.modal.hydrated")
            footer = modal.find_element(By.CSS_SELECTOR, "uc-footer.footer")
            shadow2 = utils.get_shadow(driver, footer)

            container = shadow2.find_element(By.CSS_SELECTOR, "div.button-container.reverse.same-size")
            accept_component = container.find_element(By.CSS_SELECTOR, "uc-p-button.accept.hydrated")

            shadow3 = utils.get_shadow(driver, accept_component)
            accept_btn = shadow3.find_element(By.CSS_SELECTOR, "button.root")

            driver.execute_script("arguments[0].click();", accept_btn)
            print("✅ Cookies accepted")
        except Exception:
            print("ℹ️ Cookies not shown")

        time.sleep(5)

        # Open category dropdown
        input_el = utils.wait_shadow(driver, "input#filter", timeout=20)
        driver.execute_script("arguments[0].click(); arguments[0].focus();", input_el)

        # Select first option
        opt1 = utils.wait_shadow(driver, "#option-1", timeout=20)
        driver.execute_script("arguments[0].click();", opt1)

        # Reset focus (Firefox)
        driver.find_element(By.TAG_NAME, "body").click()

        # Select next option (keyboard)
        try:
            utils.keyboard_select_next_option(driver)
        except Exception as e:
            print(f"Sales select failed: {e}")

        # Reset focus (Firefox)
        driver.find_element(By.TAG_NAME, "body").click()

        # Fill subject
        utils.fill_input(driver, (By.XPATH, "//input[@name='subject']"), "Service")

        # Fill message
        utils.fill_input(driver, (By.CSS_SELECTOR, "textarea[name='contact_message']"), "Hello!")

        # Reset focus
        driver.find_element(By.TAG_NAME, "body").click()
        time.sleep(3)

        # Select salutation (shadow + keys)
        input_salutation = utils.wait_shadow(driver, "input#filter[aria-label=', Salutation']", timeout=20)
        driver.execute_script("arguments[0].click(); arguments[0].focus();", input_salutation)
        time.sleep(1)
        input_salutation.send_keys(Keys.ARROW_DOWN, Keys.ENTER)
        time.sleep(1)

        # Fill personal data
        utils.fill_input(driver, (By.XPATH, "//input[@name='firstname']"), "David")
        utils.fill_input(driver, (By.XPATH, "//input[@name='middlename']"), "Maison")
        utils.fill_input(driver, (By.XPATH, "//input[@name='lastname']"), "Rodgers")
        utils.fill_input(driver, (By.XPATH, "//input[@name='suffix']"), "Sr")
        utils.fill_input(driver, (By.XPATH, "//input[@name='emailstandard']"), "pink@floyd.com")
        utils.fill_input(driver, (By.XPATH, "//input[@name='phone']"), "123-222-7890")

        # Select "No account"
        no_account_locator = (
            By.XPATH,
            "//input[@type='radio' and @name='myporscheaccount' and "
            "@aria-label='No, I do not have a My Porsche account.']"
        )
        radio = utils.wait_clickable(driver, no_account_locator)
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", radio)
        driver.execute_script("arguments[0].click();", radio)

        # Try captcha (keyboard)
        try:
            utils.keyboard_tab_times_then_space(driver, times=5)
            print("✅ Captcha try done")
        except Exception as e:
            print(f"Captcha step failed: {e}")

        time.sleep(5)

        # Click submit
        submit_locator = (
            By.XPATH,
            "//faas-p-button[contains(@class,'hydrated') and normalize-space(.)='Submit']"
        )
        submit_btn = utils.wait_clickable(driver, submit_locator, timeout=20)
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", submit_btn)
        time.sleep(2)
        try:
            submit_btn.click()
        except Exception:
            driver.execute_script("arguments[0].click();", submit_btn)

        time.sleep(7)

        # Check success message
        success_locator = (By.CSS_SELECTOR, "div.component-formcopytext.span-4 faas-p-text.hydrated")
        el = utils.wait_visible(driver, success_locator, timeout=30)
        print(el.text)

        if "Your message has been successfully sent!" not in el.text:
            raise Exception(f"Success text not found. Actual='{el.text}'")

        print("✅ TC_P_015 PASSED!")
        

    # ===== NEGATIVE TESTS =====

    def test_TC_N_011(self):
        print("\n========== NEGATIVE TESTS (TC_N) ==========")

        driver = self.driver

        # Open home page
        try:
            driver.get("https://www.porsche.com/usa/")
        except Exception as e:
            raise Exception(f"Failed to open home page: {e}")

        # Wait page load
        try:
            utils.wait_body(driver)
        except Exception as e:
            raise Exception(f"Page not loaded: {e}")

        # Check title
        try:
            self.assertIn("Porsche", driver.title)
        except Exception as e:
            raise Exception(f"Title check failed. Title='{driver.title}'. Error: {e}")

        time.sleep(3)

        # Accept cookies (UC shadow)
        try:
            wait = WebDriverWait(driver, 15)
            layer = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "uc-layer2")))
            shadow1 = utils.get_shadow(driver, layer)

            modal = shadow1.find_element(By.CSS_SELECTOR, "uc-p-modal.modal.hydrated")
            footer = modal.find_element(By.CSS_SELECTOR, "uc-footer.footer")
            shadow2 = utils.get_shadow(driver, footer)

            container = shadow2.find_element(By.CSS_SELECTOR, "div.button-container.reverse.same-size")
            accept_component = container.find_element(By.CSS_SELECTOR, "uc-p-button.accept.hydrated")

            shadow3 = utils.get_shadow(driver, accept_component)
            accept_btn = shadow3.find_element(By.CSS_SELECTOR, "button.root")

            driver.execute_script("arguments[0].click();", accept_btn)
            print("✅ Cookies accepted")
        except Exception:
            print("ℹ️ Cookies not shown")

        time.sleep(2)

        # Click "Get in touch" (shadow)
        try:
            selector = "a.root[href*='locations-and-contact']"
            clicked = utils.shadow_click(driver, selector)
            if not clicked:
                raise Exception("Link not found (shadow)")
            print("✅ Get in touch clicked")
        except Exception as e:
            raise Exception(f"Click failed: {e}")
        time.sleep(3)


        # Check URL
        try:
            expected = "https://www.porsche.com/usa/locations-and-contact/"
            utils.wait_url_starts(driver, expected)
            print(f"✅ URL OK: {driver.current_url}")
        except Exception as e:
            raise Exception(f"Wrong URL. Current='{driver.current_url}'. Error: {e}")

        time.sleep(5)

        # Click "General contact" (shadow)
        try:
            selector = "a[href*='/usa/locations-and-contact/#General-contact']"
            clicked = utils.shadow_click(driver, selector)
            time.sleep(3)
            if not clicked:
                raise Exception("Link not found (shadow)")
            print("✅ General contact clicked")
        except Exception as e:
            raise Exception(f"Click failed: {e}")

        # Get section
        try:
            section = utils.wait_visible(driver, (By.ID, "pcom-General-contact"))
            print("✅ Section visible")
        except Exception as e:
            raise Exception(f"Section not visible: {e}")

        time.sleep(5)

        # Click empty space
        try:
            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", section)
            time.sleep(2)

            driver.execute_script(
                """
                const el = arguments[0];
                const r = el.getBoundingClientRect();
                const x = r.left + 20;
                const y = r.top + 20;
                document.elementFromPoint(x, y).click();
                """,
                section
            )
            print("✅ Empty space clicked")
        except Exception as e:
            raise Exception(f"Click failed: {e}")

        time.sleep(3)

        # Select all (CMD+A)
        try:
            driver.switch_to.active_element.send_keys(Keys.COMMAND, "a")
            print("✅ Select all done")
        except Exception as e:
            raise Exception(f"Select all failed: {e}")

        time.sleep(5)

        # Click contact form (shadow)
        try:
            selector = "a[href*='https://forms.porsche.com/en-us/contactus/']"
            href = utils.shadow_click_and_return_href(driver, selector)
            if not href:
                raise Exception("Link not found (shadow)")
            print(f"✅ Contact form clicked. href={href}")
        except Exception as e:
            raise Exception(f"Click failed: {e}")

        time.sleep(7)

        # Check form URL
        try:
            utils.wait_url_contains(driver, "forms.porsche.com/en-us/contactus")
            print(f"✅ Form opened: {driver.current_url}")
        except Exception as e:
            raise Exception(f"Form not opened: {e}")

        print("✅ TC_N_011 PASSED!")
        

    def test_TC_N_012(self):
        print("\n========== NEGATIVE TESTS (TC_N) ==========")

        driver = self.driver

        # Open form page
        try:
            driver.get("https://forms.porsche.com/en-us/contactus/")
        except Exception as e:
            raise Exception(f"Failed to open form page: {e}")

        time.sleep(3)

        # Accept cookies (UC shadow)
        try:
            wait = WebDriverWait(driver, 5)
            layer = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "uc-layer2")))
            shadow1 = utils.get_shadow(driver, layer)

            modal = shadow1.find_element(By.CSS_SELECTOR, "uc-p-modal.modal.hydrated")
            footer = modal.find_element(By.CSS_SELECTOR, "uc-footer.footer")
            shadow2 = utils.get_shadow(driver, footer)

            container = shadow2.find_element(By.CSS_SELECTOR, "div.button-container.reverse.same-size")
            accept_component = container.find_element(By.CSS_SELECTOR, "uc-p-button.accept.hydrated")

            shadow3 = utils.get_shadow(driver, accept_component)
            accept_btn = shadow3.find_element(By.CSS_SELECTOR, "button.root")

            driver.execute_script("arguments[0].click();", accept_btn)
            print("✅ Cookies accepted")
        except Exception:
            print("ℹ️ Cookies not shown")

        time.sleep(5)

        # Open category dropdown
        try:
            input_el = utils.wait_shadow(driver, "input#filter", timeout=20)
            driver.execute_script("arguments[0].click(); arguments[0].focus();", input_el)
            print("✅ Category opened")
        except Exception as e:
            raise Exception(f"Category open failed: {e}")

        # Select first option
        try:
            opt1 = utils.wait_shadow(driver, "#option-1", timeout=20)
            driver.execute_script("arguments[0].click();", opt1)
            print("✅ First option selected")
        except Exception as e:
            raise Exception(f"Option select failed: {e}")

        # Select next option (keyboard)
        try:
            utils.keyboard_select_next_option(driver)
            print("✅ Next option selected")
        except Exception as e:
            raise Exception(f"Keyboard select failed: {e}")

        # Fill subject
        try:
            utils.fill_input(driver, (By.XPATH, "//input[@name='subject']"), "Service")
            print("✅ Subject filled")
        except Exception as e:
            raise Exception(f"Subject fill failed: {e}")

        # Fill message
        try:
            body = utils.wait_clickable(driver, (By.CSS_SELECTOR, "textarea[name='contact_message']"))
            body.clear()
            body.send_keys("Hello!")
            print("✅ Message filled")
        except Exception as e:
            raise Exception(f"Message fill failed: {e}")

        # Select salutation (keyboard)
        try:
            utils.keyboard_select_next_option(driver)
            print("✅ Salutation selected")
        except Exception as e:
            raise Exception(f"Salutation select failed: {e}")

        # Select title (keyboard)
        try:
            utils.keyboard_select_next_option(driver)
            print("✅ Title selected")
        except Exception as e:
            raise Exception(f"Title select failed: {e}")

        # Fill personal data
        try:
            utils.fill_input(driver, (By.XPATH, "//input[@name='firstname']"), "David")
            utils.fill_input(driver, (By.XPATH, "//input[@name='middlename']"), "Maison")
            utils.fill_input(driver, (By.XPATH, "//input[@name='lastname']"), "Rodgers")
            utils.fill_input(driver, (By.XPATH, "//input[@name='suffix']"), "Sr")
            utils.fill_input(driver, (By.XPATH, "//input[@name='emailstandard']"), "pink@floyd.com")
            utils.fill_input(driver, (By.XPATH, "//input[@name='phone']"), "123-222-7890")
            print("✅ Personal data filled")
        except Exception as e:
            raise Exception(f"Personal data fill failed: {e}")

        time.sleep(3)

        # Select "No account"
        try:
            no_account_locator = (
                By.XPATH,
                "//input[@type='radio' and @name='myporscheaccount' and "
                "@aria-label='No, I do not have a My Porsche account.']"
            )
            radio = utils.wait_clickable(driver, no_account_locator)
            driver.execute_script("arguments[0].click();", radio)
            print("✅ No account selected")
        except Exception as e:
            raise Exception(f"No account select failed: {e}")

        # Leave captcha empty
        print("✅ Captcha left empty")

        time.sleep(3)

        # Click submit
        try:
            submit_locator = (
                By.XPATH,
                "//faas-p-button[contains(@class,'hydrated') and normalize-space(.)='Submit']"
            )
            submit_btn = utils.wait_clickable(driver, submit_locator, timeout=20)
            submit_btn.click()
            print("✅ Submit clicked")
        except Exception as e:
            raise Exception(f"Submit click failed: {e}")

        time.sleep(5)

        # Check validation
        try:
            success_locator = (By.CSS_SELECTOR, "div.component-formcopytext.span-4 faas-p-text.hydrated")
            try:
                el = utils.wait_visible(driver, success_locator, timeout=6)
                if "Your message has been successfully sent!" in el.text:
                    raise Exception("Unexpected success (captcha was empty).")
            except Exception:
                pass
            time.sleep(3)

            try:
                error_el = utils.wait_visible(
                    driver,
                    (By.XPATH, "//*[contains(text(),'Verification was not successful')]"),
                    timeout=10
                )
                print(f"✅ Validation shown: {error_el.text}")
                utils.take_screenshot(driver, folder="screenshots_Wiki")
            except Exception as e:
                raise Exception(f"Validation text not found: {e}")

        except Exception as e:
            raise Exception(f"Validation check failed: {e}")

        print("✅ TC_N_012 PASSED!")
        

    def test_TC_N_013(self):
        print("\n========== NEGATIVE TESTS (TC_N) ==========")

        driver = self.driver

        # Open form page
        try:
            driver.get("https://forms.porsche.com/en-us/contactus/")
        except Exception as e:
            raise Exception(f"Failed to open form page: {e}")

        time.sleep(3)

        # Accept cookies (UC shadow)
        try:
            wait = WebDriverWait(driver, 5)
            layer = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "uc-layer2")))
            shadow1 = utils.get_shadow(driver, layer)

            modal = shadow1.find_element(By.CSS_SELECTOR, "uc-p-modal.modal.hydrated")
            footer = modal.find_element(By.CSS_SELECTOR, "uc-footer.footer")
            shadow2 = utils.get_shadow(driver, footer)

            container = shadow2.find_element(By.CSS_SELECTOR, "div.button-container.reverse.same-size")
            accept_component = container.find_element(By.CSS_SELECTOR, "uc-p-button.accept.hydrated")

            shadow3 = utils.get_shadow(driver, accept_component)
            accept_btn = shadow3.find_element(By.CSS_SELECTOR, "button.root")

            driver.execute_script("arguments[0].click();", accept_btn)
            print("✅ Cookies accepted")
        except Exception:
            print("ℹ️ Cookies not shown")

        time.sleep(5)

        # Open category dropdown
        input_el = utils.wait_shadow(driver, "input#filter", timeout=20)
        driver.execute_script("arguments[0].click(); arguments[0].focus();", input_el)
        print("✅ Category opened")

        # Select first option
        opt1 = utils.wait_shadow(driver, "#option-1", timeout=20)
        driver.execute_script("arguments[0].click();", opt1)
        print("✅ First option selected")

        # Select next option (keyboard)
        utils.keyboard_select_next_option(driver)
        print("✅ Next option selected")

        # Fill subject
        utils.fill_input(driver, (By.XPATH, "//input[@name='subject']"), "Service")
        print("✅ Subject filled")

        # Fill message
        body = utils.wait_clickable(driver, (By.CSS_SELECTOR, "textarea[name='contact_message']"))
        body.clear()
        body.send_keys("Hello!")
        print("✅ Message filled")

        # Select salutation/title (keyboard)
        utils.keyboard_select_next_option(driver)
        print("✅ Salutation selected")
        utils.keyboard_select_next_option(driver)
        print("✅ Title selected")

        # Fill personal data
        utils.fill_input(driver, (By.XPATH, "//input[@name='firstname']"), "David")
        utils.fill_input(driver, (By.XPATH, "//input[@name='middlename']"), "Maison")
        utils.fill_input(driver, (By.XPATH, "//input[@name='lastname']"), "Rodgers")
        utils.fill_input(driver, (By.XPATH, "//input[@name='suffix']"), "Sr")
        utils.fill_input(driver, (By.XPATH, "//input[@name='emailstandard']"), "pink@floyd.com")
        utils.fill_input(driver, (By.XPATH, "//input[@name='phone']"), "123-222-7890")
        print("✅ Personal data filled")

        time.sleep(3)

        # Select "Yes account"
        try:
            yes_locator = (
                By.XPATH,
                "//input[@type='radio' and @name='myporscheaccount' and "
                "@aria-label='Yes, I have a My Porsche account.']"
            )
            radio = utils.wait_clickable(driver, yes_locator)
            radio.click()
            print("✅ Yes account selected")
        except Exception:
            print("ℹ️ Yes account not selected")

        # Fill Porsche ID
        try:
            porsche_id_locator = (By.XPATH, "//input[@name='porscheid']")
            utils.wait_visible(driver, porsche_id_locator, timeout=20)
            utils.fill_input(driver, porsche_id_locator, "pink@floyd.")
            print("✅ Porsche ID filled")
        except Exception as e:
            raise Exception(f"Porsche ID step failed: {e}")

        time.sleep(3)

        # Try captcha (keyboard)
        try:
            utils.keyboard_tab_times_then_space(driver, times=4)
            print("✅ Captcha try done")
        except Exception as e:
            print(f"Captcha step failed: {e}")

        time.sleep(7)

        # Click submit
        try:
            submit_locator = (
                By.XPATH,
                "//faas-p-button[contains(@class,'hydrated') and normalize-space(.)='Submit']"
            )
            submit_btn = utils.wait_clickable(driver, submit_locator, timeout=20)
            submit_btn.click()
            print("✅ Submit clicked")
        except Exception as e:
            raise Exception(f"Submit click failed: {e}")

        time.sleep(5)

        # Check validation
        try:
            success_locator = (By.CSS_SELECTOR, "div.component-formcopytext.span-4 faas-p-text.hydrated")

            try:
                el = utils.wait_visible(driver, success_locator, timeout=6)
                if "Your message has been successfully sent!" in el.text:
                    utils.take_screenshot(driver, folder="screenshots_Wiki")
                    raise Exception("Unexpected success in negative test.")
            except Exception as e:
                if "Unexpected success" in str(e):
                    raise
                print("✅ Success not shown")

            try:
                utils.take_screenshot(driver, folder="screenshots_Wiki")

                if "error" in driver.current_url.lower():
                    print(f"✅ Error page opened: {driver.current_url}")
                else:
                    invalid_mark = driver.find_elements(
                        By.XPATH,
                        "//input[@name='porscheid' and "
                        "(@aria-invalid='true' or contains(@class,'error') or contains(@class,'invalid'))]"
                    )
                    described_by = driver.find_elements(
                        By.XPATH,
                        "//input[@name='porscheid' and string-length(@aria-describedby) > 0]"
                    )

                    if len(invalid_mark) > 0 or len(described_by) > 0:
                        print("✅ Porsche ID validation shown")
                    else:
                        raise Exception("No Porsche ID validation found")
            except Exception as e:
                utils.take_screenshot(driver, folder="screenshots_Wiki")
                raise Exception(f"Porsche ID validation missing: {e}")

        except Exception as e:
            raise Exception(f"Validation check failed: {e}")

        print("✅ TC_N_013 PASSED!")
        

    def test_TC_N_014(self):
        print("\n========== NEGATIVE TESTS (TC_N) ==========")

        driver = self.driver

        # Open form page
        try:
            driver.get("https://forms.porsche.com/en-us/contactus/")
        except Exception as e:
            raise Exception(f"Failed to open form page: {e}")

        time.sleep(3)

        # Accept cookies (UC shadow)
        try:
            wait = WebDriverWait(driver, 5)
            layer = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "uc-layer2")))
            shadow1 = utils.get_shadow(driver, layer)

            modal = shadow1.find_element(By.CSS_SELECTOR, "uc-p-modal.modal.hydrated")
            footer = modal.find_element(By.CSS_SELECTOR, "uc-footer.footer")
            shadow2 = utils.get_shadow(driver, footer)

            container = shadow2.find_element(By.CSS_SELECTOR, "div.button-container.reverse.same-size")
            accept_component = container.find_element(By.CSS_SELECTOR, "uc-p-button.accept.hydrated")

            shadow3 = utils.get_shadow(driver, accept_component)
            accept_btn = shadow3.find_element(By.CSS_SELECTOR, "button.root")

            driver.execute_script("arguments[0].click();", accept_btn)
            print("✅ Cookies accepted")
        except Exception:
            print("ℹ️ Cookies not shown")

        time.sleep(5)

        # Open category dropdown
        input_el = utils.wait_shadow(driver, "input#filter", timeout=20)
        driver.execute_script("arguments[0].click(); arguments[0].focus();", input_el)
        print("✅ Category opened")

        # Select first option
        opt1 = utils.wait_shadow(driver, "#option-1", timeout=20)
        driver.execute_script("arguments[0].click();", opt1)
        print("✅ First option selected")

        # Select next option (keyboard)
        utils.keyboard_select_next_option(driver)
        print("✅ Next option selected")

        # Fill subject (bad)
        utils.fill_input(driver, (By.XPATH, "//input[@name='subject']"), "!!!@@@###")
        print("✅ Subject filled (bad)")

        # Fill message (bad)
        body = utils.wait_clickable(driver, (By.CSS_SELECTOR, "textarea[name='contact_message']"))
        body.clear()
        body.send_keys("1")
        print("✅ Message filled (bad)")

        # Select salutation/title (keyboard)
        utils.keyboard_select_next_option(driver)
        print("✅ Salutation selected")
        utils.keyboard_select_next_option(driver)
        print("✅ Title selected")

        # Fill personal data (bad)
        utils.fill_input(driver, (By.XPATH, "//input[@name='firstname']"), "12345")
        utils.fill_input(driver, (By.XPATH, "//input[@name='middlename']"), "!!!")
        utils.fill_input(driver, (By.XPATH, "//input[@name='lastname']"), "@@@")
        utils.fill_input(driver, (By.XPATH, "//input[@name='suffix']"), "%%%%")
        utils.fill_input(driver, (By.XPATH, "//input[@name='emailstandard']"), "pink@")
        utils.fill_input(driver, (By.XPATH, "//input[@name='phone']"), "abc")
        print("✅ Personal data filled (bad)")

        time.sleep(2)

        # Select "No account"
        no_account_locator = (
            By.XPATH,
            "//input[@type='radio' and @name='myporscheaccount' and "
            "@aria-label='No, I do not have a My Porsche account.']"
        )
        radio = utils.wait_clickable(driver, no_account_locator)
        driver.execute_script("arguments[0].click();", radio)
        print("✅ No account selected")

        time.sleep(2)

        # Try captcha (keyboard)
        try:
            utils.keyboard_tab_times_then_space(driver, times=5)
            print("✅ Captcha try done")
        except Exception as e:
            print(f"Captcha step failed: {e}")

        time.sleep(7)

        # Click submit
        submit_locator = (
            By.XPATH,
            "//faas-p-button[contains(@class,'hydrated') and normalize-space(.)='Submit']"
        )
        submit_btn = utils.wait_clickable(driver, submit_locator, timeout=20)
        submit_btn.click()
        print("✅ Submit clicked")

        time.sleep(4)

        # Check validation
        try:
            success_locator = (By.CSS_SELECTOR, "div.component-formcopytext.span-4 faas-p-text.hydrated")
            try:
                el = utils.wait_visible(driver, success_locator, timeout=4)
                if "Your message has been successfully sent!" in el.text:
                    raise Exception("Unexpected success with bad data.")
            except Exception:
                pass

            invalid_fields = driver.find_elements(By.CSS_SELECTOR, "[aria-invalid='true']")

            validation_text_el = None
            try:
                validation_text_el = utils.wait_visible(
                    driver,
                    (By.XPATH,
                     "//*[contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'email') "
                     "or contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'phone') "
                     "or contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'invalid')]"),
                    timeout=6
                )
            except Exception:
                pass

            if len(invalid_fields) == 0 and validation_text_el is None:
                raise Exception("No validation shown")

            if len(invalid_fields) > 0:
                print(f"✅ Invalid fields: {len(invalid_fields)}")

            if validation_text_el is not None:
                print(f"✅ Validation text: {validation_text_el.text}")

            utils.take_screenshot(driver, folder="screenshots_Wiki")

        except Exception as e:
            raise Exception(f"Validation check failed: {e}")

        print("✅ TC_N_014 PASSED!")
        

    def test_TC_N_015(self):
        print("\n========== NEGATIVE TESTS (TC_N) ==========")

        driver = self.driver

        # Open form page
        try:
            driver.get("https://forms.porsche.com/en-us/contactus/")
        except Exception as e:
            raise Exception(f"Failed to open form page: {e}")

        time.sleep(3)

        # Accept cookies (UC shadow)
        try:
            wait = WebDriverWait(driver, 5)
            layer = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "uc-layer2")))
            shadow1 = utils.get_shadow(driver, layer)

            modal = shadow1.find_element(By.CSS_SELECTOR, "uc-p-modal.modal.hydrated")
            footer = modal.find_element(By.CSS_SELECTOR, "uc-footer.footer")
            shadow2 = utils.get_shadow(driver, footer)

            container = shadow2.find_element(By.CSS_SELECTOR, "div.button-container.reverse.same-size")
            accept_component = container.find_element(By.CSS_SELECTOR, "uc-p-button.accept.hydrated")

            shadow3 = utils.get_shadow(driver, accept_component)
            accept_btn = shadow3.find_element(By.CSS_SELECTOR, "button.root")

            driver.execute_script("arguments[0].click();", accept_btn)
            print("✅ Cookies accepted")
        except Exception:
            print("ℹ️ Cookies not shown")

        time.sleep(5)

        # Select "No account"
        try:
            no_account_locator = (
                By.XPATH,
                "//input[@type='radio' and @name='myporscheaccount' and "
                "@aria-label='No, I do not have a My Porsche account.']"
            )
            radio = utils.wait_clickable(driver, no_account_locator)

            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", radio)
            time.sleep(1)
            driver.execute_script("window.scrollBy(0, 60);")

            driver.execute_script("arguments[0].click();", radio)
            print("✅ No account selected")
        except Exception as e:
            raise Exception(f"No account select failed: {e}")

        time.sleep(2)

        # Try captcha (direct click)
        try:
            captcha = driver.find_element(By.CSS_SELECTOR, "input[id^='altcha_verification_checkbox_']")
            driver.execute_script("arguments[0].click();", captcha)
            print("✅ Captcha try done")
        except Exception as e:
            print(f"⚠️ Captcha step failed (ignored): {e}")

        time.sleep(7)

        # Click submit
        try:
            submit_locator = (
                By.XPATH,
                "//faas-p-button[contains(@class,'hydrated') and normalize-space(.)='Submit']"
            )
            submit_btn = utils.wait_clickable(driver, submit_locator, timeout=10)
            submit_btn.click()
            print("✅ Submit clicked")
        except Exception as e:
            raise Exception(f"Submit click failed: {e}")

        time.sleep(5)

        # Check validation
        try:
            success_locator = (By.CSS_SELECTOR, "div.component-formcopytext.span-4 faas-p-text.hydrated")
            try:
                el = utils.wait_visible(driver, success_locator, timeout=4)
                if "Your message has been successfully sent!" in el.text:
                    raise Exception("Unexpected success with empty fields.")
            except Exception:
                pass

            invalid_fields = driver.find_elements(By.CSS_SELECTOR, "[aria-invalid='true']")

            required_text_el = None
            try:
                required_text_el = utils.wait_visible(
                    driver,
                    (By.XPATH,
                     "//*[contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'required') "
                     "or contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'please fill') "
                     "or contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'mandatory')]"),
                    timeout=8
                )
            except Exception:
                pass
            time.sleep(3)

            if len(invalid_fields) == 0 and required_text_el is None:
                raise Exception("No validation shown")

            if len(invalid_fields) > 0:
                print(f"✅ Invalid fields: {len(invalid_fields)}")

            if required_text_el is not None:
                print(f"✅ Required text: {required_text_el.text}")

            utils.take_screenshot(driver, folder="screenshots_Wiki")

        except Exception as e:
            raise Exception(f"Validation check failed: {e}")

        print("✅ TC_N_015 PASSED!")
        

class EdgeDriverPorsche(unittest.TestCase):
    driver: WebDriver

    def setUp(self):
        # Create driver
        self.driver = utils.create_driver("edge")

    def tearDown(self):
        # Close driver
        self.driver.quit()


    # ===== POSITIVE TESTS =====

    def test_TC_P_011(self):
        print("\n========== POSITIVE TESTS (TC_P) ==========")

        driver = self.driver

        # Open home page
        try:
            driver.get("https://www.porsche.com/usa/")
        except Exception as e:
            raise Exception(f"Failed to open home page: {e}")

        # Wait page load
        try:
            utils.wait_body(driver)
        except Exception as e:
            raise Exception(f"Page not loaded: {e}")

        # Check title
        try:
            self.assertIn("Porsche", driver.title)
        except Exception as e:
            raise Exception(f"Title check failed. Title='{driver.title}'. Error: {e}")

        time.sleep(3)

        # Accept cookies (UC shadow)
        try:
            wait = WebDriverWait(driver, 5)
            layer = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "uc-layer2")))
            shadow1 = utils.get_shadow(driver, layer)

            modal = shadow1.find_element(By.CSS_SELECTOR, "uc-p-modal.modal.hydrated")
            footer = modal.find_element(By.CSS_SELECTOR, "uc-footer.footer")
            shadow2 = utils.get_shadow(driver, footer)

            container = shadow2.find_element(By.CSS_SELECTOR, "div.button-container.reverse.same-size")
            accept_component = container.find_element(By.CSS_SELECTOR, "uc-p-button.accept.hydrated")

            shadow3 = utils.get_shadow(driver, accept_component)
            accept_btn = shadow3.find_element(By.CSS_SELECTOR, "button.root")

            driver.execute_script("arguments[0].click();", accept_btn)
            print("✅ Cookies accepted")
        except Exception:
            print("ℹ️ Cookies not shown")

        time.sleep(5)

        # Scroll to bottom
        try:
            utils.scroll_to_bottom(driver)
            print("✅ Scrolled to bottom")
        except Exception as e:
            raise Exception(f"Scroll failed: {e}")

        # Click "Get in touch" (shadow)
        try:
            selector = "a.root[href*='locations-and-contact']"
            utils.wait_shadow(driver, selector, timeout=20)

            clicked = utils.shadow_click(driver, selector)
            if not clicked:
                raise Exception("Link not found (shadow)")
            print("✅ Get in touch clicked")
        except Exception as e:
            raise Exception(f"Click failed: {e}")

        # Check URL
        try:
            expected = "https://www.porsche.com/usa/locations-and-contact/"
            utils.wait_url_starts(driver, expected)
            print(f"✅ URL OK: {driver.current_url}")
        except Exception as e:
            raise Exception(f"Wrong URL. Current='{driver.current_url}'. Error: {e}")

        print("✅ TC_P_011 PASSED!")

    def test_TC_P_012(self):
        print("\n========== POSITIVE TESTS (TC_P) ==========")

        driver = self.driver

        # Open page
        try:
            driver.get("https://www.porsche.com/usa/locations-and-contact/")
        except Exception as e:
            raise Exception(f"Failed to open page: {e}")

        # Wait page load
        try:
            utils.wait_body(driver)
        except Exception as e:
            raise Exception(f"Page not loaded: {e}")

        time.sleep(3)

        # Accept cookies
        try:
            utils.accept_cookies_with_keyboard(driver)
            print("✅ Cookies accepted")
        except Exception:
            print("ℹ️ Cookies not shown")

        # Check URL
        try:
            expected = "https://www.porsche.com/usa/locations-and-contact/"
            utils.wait_url_starts(driver, expected)
            print(f"✅ URL OK: {driver.current_url}")
        except Exception as e:
            raise Exception(f"Wrong URL. Current='{driver.current_url}'. Error: {e}")

        # Click "General contact" (shadow)
        try:
            selector = "a[href*='/usa/locations-and-contact/#General-contact']"
            clicked = utils.shadow_click(driver, selector)
            if not clicked:
                raise Exception("Link not found (shadow)")
            print("✅ General contact clicked")
        except Exception as e:
            raise Exception(f"Click failed: {e}")

        # Check block present
        try:
            utils.wait_present(driver, (By.ID, "pcom-General-contact"))
            print("✅ Block present")
        except Exception as e:
            raise Exception(f"Block not present: {e}")

        print("✅ TC_P_012 PASSED!")

    def test_TC_P_013(self):
        print("\n========== POSITIVE TESTS (TC_P) ==========")

        driver = self.driver

        # Open page
        try:
            driver.get("https://www.porsche.com/usa/locations-and-contact/")
        except Exception as e:
            raise Exception(f"Failed to open page: {e}")

        # Wait page load
        try:
            utils.wait_body(driver)
        except Exception as e:
            raise Exception(f"Page not loaded: {e}")

        time.sleep(3)

        # Accept cookies
        try:
            utils.accept_cookies_with_keyboard(driver)
            print("✅ Cookies accepted")
        except Exception:
            print("ℹ️ Cookies not shown")

        # Click "General contact" (shadow)
        try:
            selector = "a[href*='/usa/locations-and-contact/#General-contact']"
            clicked = utils.shadow_click(driver, selector)
            if not clicked:
                raise Exception("Link not found (shadow)")
            print("✅ General contact clicked")
        except Exception as e:
            raise Exception(f"Click failed: {e}")

        # Check block visible
        try:
            el = utils.wait_visible(driver, (By.ID, "pcom-General-contact"))
            print(el.text)
        except Exception as e:
            raise Exception(f"Block not visible: {e}")

        print("✅ TC_P_013 PASSED!")

    def test_TC_P_014(self):
        print("\n========== POSITIVE TESTS (TC_P) ==========")

        driver = self.driver

        # Open page
        try:
            driver.get("https://www.porsche.com/usa/locations-and-contact/")
        except Exception as e:
            raise Exception(f"Failed to open page: {e}")

        # Wait page load
        try:
            utils.wait_body(driver)
        except Exception as e:
            raise Exception(f"Page not loaded: {e}")

        time.sleep(3)

        # Accept cookies
        try:
            utils.accept_cookies_with_keyboard(driver)
            print("✅ Cookies accepted")
        except Exception:
            print("ℹ️ Cookies not shown")

        # Click "General contact" (shadow)
        try:
            selector = "a[href*='/usa/locations-and-contact/#General-contact']"
            clicked = utils.shadow_click(driver, selector)
            if not clicked:
                raise Exception("Link not found (shadow)")
            print("✅ General contact clicked")
        except Exception as e:
            raise Exception(f"Click failed: {e}")

        # Click contact form (shadow) and get href
        try:
            selector = "a[href*='https://forms.porsche.com/en-us/contactus/']"
            href = utils.shadow_click_and_return_href(driver, selector)
            if not href:
                raise Exception("Link not found (shadow)")
            print(f"✅ Contact form clicked. href={href}")
        except Exception as e:
            raise Exception(f"Contact form click failed: {e}")

        # Accept cookies (forms)
        try:
            utils.accept_cookies_with_keyboard(driver)
            print("✅ Cookies accepted (forms)")
        except Exception:
            print("ℹ️ Cookies not shown (forms)")

        # Check form URL
        try:
            utils.wait_url_starts(driver, "https://forms.porsche.com/en-us/contactus/")
            print(f"✅ Form URL OK: {driver.current_url}")
        except Exception as e:
            raise Exception(f"Wrong form URL. Current='{driver.current_url}'. Error: {e}")

        print("✅ TC_P_014 PASSED!")

    def test_TC_P_015(self):
        driver = self.driver

        # Open form page
        driver.get("https://forms.porsche.com/en-us/contactus/")
        utils.wait_url_contains(driver, "forms.porsche.com/en-us/contactus")
        time.sleep(7)

        # Accept cookies
        try:
            utils.accept_cookies_with_keyboard(driver)
            print("✅ Cookies accepted")
        except Exception:
            print("ℹ️ Cookies not shown")

        # Open category dropdown
        input_el = utils.wait_shadow(driver, "input#filter", timeout=20)
        driver.execute_script("arguments[0].click(); arguments[0].focus();", input_el)

        # Select first option
        opt1 = utils.wait_shadow(driver, "#option-1", timeout=20)
        driver.execute_script("arguments[0].click();", opt1)

        # Select next option (keyboard)
        try:
            utils.keyboard_select_next_option(driver)
        except Exception as e:
            print(f"Sales select failed: {e}")

        # Fill subject
        utils.fill_input(driver, (By.XPATH, "//input[@name='subject']"), "Service")

        # Fill message
        body = utils.wait_clickable(driver, (By.CSS_SELECTOR, "textarea[name='contact_message']"))
        body.send_keys("Hello!")

        # Select salutation/title (keyboard)
        try:
            utils.keyboard_select_next_option(driver)
        except Exception as e:
            print(f"Salutation select failed: {e}")

        try:
            utils.keyboard_select_next_option(driver)
        except Exception as e:
            print(f"Title select failed: {e}")

        # Fill personal data
        utils.fill_input(driver, (By.XPATH, "//input[@name='firstname']"), "David")
        utils.fill_input(driver, (By.XPATH, "//input[@name='middlename']"), "Maison")
        utils.fill_input(driver, (By.XPATH, "//input[@name='lastname']"), "Rodgers")
        utils.fill_input(driver, (By.XPATH, "//input[@name='suffix']"), "Sr")
        utils.fill_input(driver, (By.XPATH, "//input[@name='emailstandard']"), "pink@floyd.com")
        utils.fill_input(driver, (By.XPATH, "//input[@name='phone']"), "123-222-7890")

        time.sleep(3)

        # Select "No account"
        no_account_locator = (
            By.XPATH,
            "//input[@type='radio' and @name='myporscheaccount' and "
            "@aria-label='No, I do not have a My Porsche account.']"
        )
        radio = utils.wait_clickable(driver, no_account_locator)
        driver.execute_script("arguments[0].click();", radio)

        time.sleep(3)

        # Try captcha (keyboard)
        try:
            utils.keyboard_tab_times_then_space(driver, times=5)
            print("✅ Captcha try done")
        except Exception as e:
            print(f"Captcha step failed: {e}")

        time.sleep(7)

        # Click submit
        submit_locator = (
            By.XPATH,
            "//faas-p-button[contains(@class,'hydrated') and normalize-space(.)='Submit']"
        )
        submit_btn = utils.wait_clickable(driver, submit_locator, timeout=20)
        submit_btn.click()
        time.sleep(7)

        # Check success message
        success_locator = (By.CSS_SELECTOR, "div.component-formcopytext.span-4 faas-p-text.hydrated")
        el = utils.wait_visible(driver, success_locator, timeout=30)
        print(el.text)

        if "Your message has been successfully sent!" not in el.text:
            raise Exception(f"Success text not found. Actual='{el.text}'")

        print("✅ TC_P_015 PASSED!")

    # ===== NEGATIVE TESTS =====

    def test_TC_N_011(self):
        print("\n========== NEGATIVE TESTS (TC_N) ==========")

        driver = self.driver

        # Open home page
        try:
            driver.get("https://www.porsche.com/usa/")
        except Exception as e:
            raise Exception(f"Failed to open home page: {e}")

        # Wait page load
        try:
            utils.wait_body(driver)
        except Exception as e:
            raise Exception(f"Page not loaded: {e}")

        # Check title
        try:
            self.assertIn("Porsche", driver.title)
        except Exception as e:
            raise Exception(f"Title check failed. Title='{driver.title}'. Error: {e}")

        time.sleep(3)

        # Accept cookies
        try:
            utils.accept_cookies_with_keyboard(driver)
            print("✅ Cookies accepted")
        except Exception:
            print("ℹ️ Cookies not shown")

        time.sleep(3)

        # Scroll to bottom
        try:
            utils.scroll_to_bottom(driver)
            print("✅ Scrolled to bottom")
        except Exception as e:
            raise Exception(f"Scroll failed: {e}")

        # Click "Get in touch" (shadow)
        try:
            selector = "a.root[href*='locations-and-contact']"
            clicked = utils.shadow_click(driver, selector)
            if not clicked:
                raise Exception("Link not found (shadow)")
            print("✅ Get in touch clicked")
        except Exception as e:
            raise Exception(f"Click failed: {e}")

        # Check URL
        try:
            expected = "https://www.porsche.com/usa/locations-and-contact/"
            utils.wait_url_starts(driver, expected)
            print(f"✅ URL OK: {driver.current_url}")
        except Exception as e:
            raise Exception(f"Wrong URL. Current='{driver.current_url}'. Error: {e}")

        time.sleep(3)

        # Click "General contact" (shadow)
        try:
            selector = "a[href*='/usa/locations-and-contact/#General-contact']"
            clicked = utils.shadow_click(driver, selector)
            if not clicked:
                raise Exception("Link not found (shadow)")
            print("✅ General contact clicked")
        except Exception as e:
            raise Exception(f"Click failed: {e}")

        # Get section
        try:
            section = utils.wait_visible(driver, (By.ID, "pcom-General-contact"))
            print("✅ Section visible")
        except Exception as e:
            raise Exception(f"Section not visible: {e}")

        time.sleep(5)

        # Click empty space
        try:
            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", section)
            time.sleep(5)

            driver.execute_script(
                """
                const el = arguments[0];
                const r = el.getBoundingClientRect();
                const x = r.left + 20;
                const y = r.top + 20;
                document.elementFromPoint(x, y).click();
                """,
                section
            )
            print("✅ Empty space clicked")
        except Exception as e:
            raise Exception(f"Click failed: {e}")

        time.sleep(3)

        # Select all (CMD+A)
        try:
            driver.switch_to.active_element.send_keys(Keys.COMMAND, "a")
            print("✅ Select all done")
        except Exception as e:
            raise Exception(f"Select all failed: {e}")

        time.sleep(5)

        # Click contact form (shadow)
        try:
            selector = "a[href*='https://forms.porsche.com/en-us/contactus/']"
            href = utils.shadow_click_and_return_href(driver, selector)
            if not href:
                raise Exception("Link not found (shadow)")
            print(f"✅ Contact form clicked. href={href}")
        except Exception as e:
            raise Exception(f"Click failed: {e}")

        time.sleep(7)

        # Check form URL
        try:
            utils.wait_url_contains(driver, "forms.porsche.com/en-us/contactus")
            print(f"✅ Form opened: {driver.current_url}")
        except Exception as e:
            raise Exception(f"Form not opened: {e}")

        print("✅ TC_N_011 PASSED!")

    def test_TC_N_012(self):
        print("\n========== NEGATIVE TESTS (TC_N) ==========")

        driver = self.driver

        # Open form page
        try:
            driver.get("https://forms.porsche.com/en-us/contactus/")
        except Exception as e:
            raise Exception(f"Failed to open form page: {e}")

        time.sleep(3)

        # Accept cookies
        try:
            utils.accept_cookies_with_keyboard(driver)
            print("✅ Cookies accepted")
        except Exception:
            print("ℹ️ Cookies not shown")

        time.sleep(5)

        # Open category dropdown
        try:
            input_el = utils.wait_shadow(driver, "input#filter", timeout=20)
            driver.execute_script("arguments[0].click(); arguments[0].focus();", input_el)
            print("✅ Category opened")
        except Exception as e:
            raise Exception(f"Category open failed: {e}")

        # Select first option
        try:
            opt1 = utils.wait_shadow(driver, "#option-1", timeout=20)
            driver.execute_script("arguments[0].click();", opt1)
            print("✅ First option selected")
        except Exception as e:
            raise Exception(f"Option select failed: {e}")

        # Select next option (keyboard)
        try:
            utils.keyboard_select_next_option(driver)
            print("✅ Next option selected")
        except Exception as e:
            raise Exception(f"Keyboard select failed: {e}")

        # Fill subject
        try:
            utils.fill_input(driver, (By.XPATH, "//input[@name='subject']"), "Service")
            print("✅ Subject filled")
        except Exception as e:
            raise Exception(f"Subject fill failed: {e}")

        # Fill message
        try:
            body = utils.wait_clickable(driver, (By.CSS_SELECTOR, "textarea[name='contact_message']"))
            body.clear()
            body.send_keys("Hello!")
            print("✅ Message filled")
        except Exception as e:
            raise Exception(f"Message fill failed: {e}")

        # Select salutation/title (keyboard)
        try:
            utils.keyboard_select_next_option(driver)
            print("✅ Salutation selected")
        except Exception as e:
            raise Exception(f"Salutation select failed: {e}")

        try:
            utils.keyboard_select_next_option(driver)
            print("✅ Title selected")
        except Exception as e:
            raise Exception(f"Title select failed: {e}")

        # Fill personal data
        try:
            utils.fill_input(driver, (By.XPATH, "//input[@name='firstname']"), "David")
            utils.fill_input(driver, (By.XPATH, "//input[@name='middlename']"), "Maison")
            utils.fill_input(driver, (By.XPATH, "//input[@name='lastname']"), "Rodgers")
            utils.fill_input(driver, (By.XPATH, "//input[@name='suffix']"), "Sr")
            utils.fill_input(driver, (By.XPATH, "//input[@name='emailstandard']"), "pink@floyd.com")
            utils.fill_input(driver, (By.XPATH, "//input[@name='phone']"), "123-222-7890")
            print("✅ Personal data filled")
        except Exception as e:
            raise Exception(f"Personal data fill failed: {e}")

        time.sleep(3)

        # Select "No account"
        try:
            no_account_locator = (
                By.XPATH,
                "//input[@type='radio' and @name='myporscheaccount' and "
                "@aria-label='No, I do not have a My Porsche account.']"
            )
            radio = utils.wait_clickable(driver, no_account_locator)
            driver.execute_script("arguments[0].click();", radio)
            print("✅ No account selected")
        except Exception as e:
            raise Exception(f"No account select failed: {e}")

        # Leave captcha empty
        print("✅ Captcha left empty")

        time.sleep(2)

        # Click submit
        try:
            submit_locator = (
                By.XPATH,
                "//faas-p-button[contains(@class,'hydrated') and normalize-space(.)='Submit']"
            )
            submit_btn = utils.wait_clickable(driver, submit_locator, timeout=20)
            submit_btn.click()
            print("✅ Submit clicked")
        except Exception as e:
            raise Exception(f"Submit click failed: {e}")

        time.sleep(5)

        # Check validation
        try:
            success_locator = (By.CSS_SELECTOR, "div.component-formcopytext.span-4 faas-p-text.hydrated")
            try:
                el = utils.wait_visible(driver, success_locator, timeout=6)
                if "Your message has been successfully sent!" in el.text:
                    raise Exception("Unexpected success (captcha was empty).")
            except Exception:
                pass

            try:
                error_el = utils.wait_visible(
                    driver,
                    (By.XPATH, "//*[contains(text(),'Verification was not successful')]"),
                    timeout=10
                )
                print(f"✅ Validation shown: {error_el.text}")
                utils.take_screenshot(driver, folder="screenshots_Wiki")
            except Exception as e:
                raise Exception(f"Validation text not found: {e}")

        except Exception as e:
            raise Exception(f"Validation check failed: {e}")

        print("✅ TC_N_012 PASSED!")

    def test_TC_N_013(self):
        print("\n========== NEGATIVE TESTS (TC_N) ==========")

        driver = self.driver

        # Open form page
        try:
            driver.get("https://forms.porsche.com/en-us/contactus/")
        except Exception as e:
            raise Exception(f"Failed to open form page: {e}")

        time.sleep(3)

        # Accept cookies
        try:
            utils.accept_cookies_with_keyboard(driver)
            print("✅ Cookies accepted")
        except Exception:
            print("ℹ️ Cookies not shown")

        time.sleep(5)

        # Open category dropdown
        input_el = utils.wait_shadow(driver, "input#filter", timeout=20)
        driver.execute_script("arguments[0].click(); arguments[0].focus();", input_el)
        print("✅ Category opened")

        # Select first option
        opt1 = utils.wait_shadow(driver, "#option-1", timeout=20)
        driver.execute_script("arguments[0].click();", opt1)
        print("✅ First option selected")

        # Select next option (keyboard)
        utils.keyboard_select_next_option(driver)
        print("✅ Next option selected")

        # Fill subject
        utils.fill_input(driver, (By.XPATH, "//input[@name='subject']"), "Service")
        print("✅ Subject filled")

        # Fill message
        body = utils.wait_clickable(driver, (By.CSS_SELECTOR, "textarea[name='contact_message']"))
        body.clear()
        body.send_keys("Hello!")
        print("✅ Message filled")

        # Select salutation/title (keyboard)
        utils.keyboard_select_next_option(driver)
        print("✅ Salutation selected")
        utils.keyboard_select_next_option(driver)
        print("✅ Title selected")

        # Fill personal data
        utils.fill_input(driver, (By.XPATH, "//input[@name='firstname']"), "David")
        utils.fill_input(driver, (By.XPATH, "//input[@name='middlename']"), "Maison")
        utils.fill_input(driver, (By.XPATH, "//input[@name='lastname']"), "Rodgers")
        utils.fill_input(driver, (By.XPATH, "//input[@name='suffix']"), "Sr")
        utils.fill_input(driver, (By.XPATH, "//input[@name='emailstandard']"), "pink@floyd.com")
        utils.fill_input(driver, (By.XPATH, "//input[@name='phone']"), "123-222-7890")
        print("✅ Personal data filled")

        time.sleep(3)

        # Select "Yes account"
        try:
            yes_locator = (
                By.XPATH,
                "//input[@type='radio' and @name='myporscheaccount' and "
                "@aria-label='Yes, I have a My Porsche account.']"
            )
            radio = utils.wait_clickable(driver, yes_locator)
            radio.click()
            print("✅ Yes account selected")
        except Exception:
            print("ℹ️ Yes account not selected")

        # Fill Porsche ID
        try:
            porsche_id_locator = (By.XPATH, "//input[@name='porscheid']")
            utils.wait_visible(driver, porsche_id_locator, timeout=20)
            utils.fill_input(driver, porsche_id_locator, "pink@floyd.")
            print("✅ Porsche ID filled")
        except Exception as e:
            raise Exception(f"Porsche ID step failed: {e}")

        time.sleep(3)

        # Try captcha (keyboard)
        try:
            utils.keyboard_tab_times_then_space(driver, times=4)
            print("✅ Captcha try done")
        except Exception as e:
            print(f"Captcha step failed: {e}")

        time.sleep(7)

        # Click submit
        try:
            submit_locator = (
                By.XPATH,
                "//faas-p-button[contains(@class,'hydrated') and normalize-space(.)='Submit']"
            )
            submit_btn = utils.wait_clickable(driver, submit_locator, timeout=20)
            submit_btn.click()
            print("✅ Submit clicked")
        except Exception as e:
            raise Exception(f"Submit click failed: {e}")

        time.sleep(5)

        # Check validation
        try:
            success_locator = (By.CSS_SELECTOR, "div.component-formcopytext.span-4 faas-p-text.hydrated")

            try:
                el = utils.wait_visible(driver, success_locator, timeout=6)
                if "Your message has been successfully sent!" in el.text:
                    utils.take_screenshot(driver, folder="screenshots_Wiki")
                    raise Exception("Unexpected success in negative test.")
            except Exception as e:
                if "Unexpected success" in str(e):
                    raise
                print("✅ Success not shown")

            try:
                utils.take_screenshot(driver, folder="screenshots_Wiki")

                if "error" in driver.current_url.lower():
                    print(f"✅ Error page opened: {driver.current_url}")
                else:
                    invalid_mark = driver.find_elements(
                        By.XPATH,
                        "//input[@name='porscheid' and "
                        "(@aria-invalid='true' or contains(@class,'error') or contains(@class,'invalid'))]"
                    )
                    described_by = driver.find_elements(
                        By.XPATH,
                        "//input[@name='porscheid' and string-length(@aria-describedby) > 0]"
                    )

                    if len(invalid_mark) > 0 or len(described_by) > 0:
                        print("✅ Porsche ID validation shown")
                    else:
                        raise Exception("No Porsche ID validation found")
            except Exception as e:
                utils.take_screenshot(driver, folder="screenshots_Wiki")
                raise Exception(f"Porsche ID validation missing: {e}")

        except Exception as e:
            raise Exception(f"Validation check failed: {e}")

        print("✅ TC_N_013 PASSED!")

    def test_TC_N_014(self):
        print("\n========== NEGATIVE TESTS (TC_N) ==========")

        driver = self.driver

        # Open form page
        try:
            driver.get("https://forms.porsche.com/en-us/contactus/")
        except Exception as e:
            raise Exception(f"Failed to open form page: {e}")

        time.sleep(3)

        # Accept cookies
        try:
            utils.accept_cookies_with_keyboard(driver)
            print("✅ Cookies accepted")
        except Exception:
            print("ℹ️ Cookies not shown")

        time.sleep(5)

        # Open category dropdown
        input_el = utils.wait_shadow(driver, "input#filter", timeout=20)
        driver.execute_script("arguments[0].click(); arguments[0].focus();", input_el)
        print("✅ Category opened")

        # Select first option
        opt1 = utils.wait_shadow(driver, "#option-1", timeout=20)
        driver.execute_script("arguments[0].click();", opt1)
        print("✅ First option selected")

        # Select next option (keyboard)
        utils.keyboard_select_next_option(driver)
        print("✅ Next option selected")

        # Fill subject (bad)
        utils.fill_input(driver, (By.XPATH, "//input[@name='subject']"), "!!!@@@###")
        print("✅ Subject filled (bad)")

        # Fill message (bad)
        body = utils.wait_clickable(driver, (By.CSS_SELECTOR, "textarea[name='contact_message']"))
        body.clear()
        body.send_keys("1")
        print("✅ Message filled (bad)")

        # Select salutation/title (keyboard)
        utils.keyboard_select_next_option(driver)
        print("✅ Salutation selected")
        utils.keyboard_select_next_option(driver)
        print("✅ Title selected")

        # Fill personal data (bad)
        utils.fill_input(driver, (By.XPATH, "//input[@name='firstname']"), "12345")
        utils.fill_input(driver, (By.XPATH, "//input[@name='middlename']"), "!!!")
        utils.fill_input(driver, (By.XPATH, "//input[@name='lastname']"), "@@@")
        utils.fill_input(driver, (By.XPATH, "//input[@name='suffix']"), "%%%%")
        utils.fill_input(driver, (By.XPATH, "//input[@name='emailstandard']"), "pink@")
        utils.fill_input(driver, (By.XPATH, "//input[@name='phone']"), "abc")
        print("✅ Personal data filled (bad)")

        time.sleep(2)

        # Select "No account"
        no_account_locator = (
            By.XPATH,
            "//input[@type='radio' and @name='myporscheaccount' and "
            "@aria-label='No, I do not have a My Porsche account.']"
        )
        radio = utils.wait_clickable(driver, no_account_locator)
        driver.execute_script("arguments[0].click();", radio)
        print("✅ No account selected")

        time.sleep(2)

        # Try captcha (keyboard)
        try:
            utils.keyboard_tab_times_then_space(driver, times=5)
            print("✅ Captcha try done")
        except Exception as e:
            print(f"Captcha step failed: {e}")

        time.sleep(7)

        # Click submit
        submit_locator = (
            By.XPATH,
            "//faas-p-button[contains(@class,'hydrated') and normalize-space(.)='Submit']"
        )
        submit_btn = utils.wait_clickable(driver, submit_locator, timeout=20)
        submit_btn.click()
        print("✅ Submit clicked")

        time.sleep(4)

        # Check validation
        try:
            success_locator = (By.CSS_SELECTOR, "div.component-formcopytext.span-4 faas-p-text.hydrated")
            try:
                el = utils.wait_visible(driver, success_locator, timeout=4)
                if "Your message has been successfully sent!" in el.text:
                    raise Exception("Unexpected success with bad data.")
            except Exception:
                pass

            invalid_fields = driver.find_elements(By.CSS_SELECTOR, "[aria-invalid='true']")

            validation_text_el = None
            try:
                validation_text_el = utils.wait_visible(
                    driver,
                    (By.XPATH,
                     "//*[contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'email') "
                     "or contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'phone') "
                     "or contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'invalid')]"),
                    timeout=6
                )
            except Exception:
                pass

            if len(invalid_fields) == 0 and validation_text_el is None:
                raise Exception("No validation shown")

            if len(invalid_fields) > 0:
                print(f"✅ Invalid fields: {len(invalid_fields)}")

            if validation_text_el is not None:
                print(f"✅ Validation text: {validation_text_el.text}")

            utils.take_screenshot(driver, folder="screenshots_Wiki")

        except Exception as e:
            raise Exception(f"Validation check failed: {e}")

        print("✅ TC_N_014 PASSED!")

    def test_TC_N_015(self):
        print("\n========== NEGATIVE TESTS (TC_N) ==========")

        driver = self.driver

        # Open form page
        try:
            driver.get("https://forms.porsche.com/en-us/contactus/")
        except Exception as e:
            raise Exception(f"Failed to open form page: {e}")

        time.sleep(3)

        # Accept cookies
        try:
            utils.accept_cookies_with_keyboard(driver)
            print("✅ Cookies accepted")
        except Exception:
            print("ℹ️ Cookies not shown")

        time.sleep(5)

        # Select "No account"
        try:
            no_account_locator = (
                By.XPATH,
                "//input[@type='radio' and @name='myporscheaccount' and "
                "@aria-label='No, I do not have a My Porsche account.']"
            )
            radio = utils.wait_clickable(driver, no_account_locator)

            driver.execute_script("arguments[0].scrollIntoView({block:'center'});", radio)
            time.sleep(1)
            driver.execute_script("window.scrollBy(0, -120);")

            driver.execute_script("arguments[0].click();", radio)
            print("✅ No account selected")
        except Exception as e:
            raise Exception(f"No account select failed: {e}")

        time.sleep(5)

        # Try captcha (keyboard)
        try:
            utils.keyboard_tab_times_then_space(driver, times=4)
            print("✅ Captcha try done")
        except Exception as e:
            print(f"⚠️ Captcha step failed (ignored): {e}")

        time.sleep(5)

        # Click submit
        try:
            submit_locator = (
                By.XPATH,
                "//faas-p-button[contains(@class,'hydrated') and normalize-space(.)='Submit']"
            )
            submit_btn = utils.wait_clickable(driver, submit_locator, timeout=10)
            submit_btn.click()
            print("✅ Submit clicked")
        except Exception as e:
            raise Exception(f"Submit click failed: {e}")

        time.sleep(5)

        # Check validation
        try:
            success_locator = (By.CSS_SELECTOR, "div.component-formcopytext.span-4 faas-p-text.hydrated")
            try:
                el = utils.wait_visible(driver, success_locator, timeout=4)
                if "Your message has been successfully sent!" in el.text:
                    raise Exception("Unexpected success with empty fields.")
            except Exception:
                pass

            invalid_fields = driver.find_elements(By.CSS_SELECTOR, "[aria-invalid='true']")

            required_text_el = None
            try:
                required_text_el = utils.wait_visible(
                    driver,
                    (By.XPATH,
                     "//*[contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'required') "
                     "or contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'please fill') "
                     "or contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'mandatory')]"),
                    timeout=8
                )
            except Exception:
                pass

            if len(invalid_fields) == 0 and required_text_el is None:
                raise Exception("No validation shown")

            if len(invalid_fields) > 0:
                print(f"✅ Invalid fields: {len(invalid_fields)}")

            if required_text_el is not None:
                print(f"✅ Required text: {required_text_el.text}")

            utils.take_screenshot(driver, folder="screenshots_Wiki")

        except Exception as e:
            raise Exception(f"Validation check failed: {e}")

        print("✅ TC_N_015 PASSED!")



if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports')
    )



# if __name__ == "__main__":
#     suite = unittest.TestSuite()
#     suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(FirefoxDriverPorsche))
#
#     runner = HtmlTestRunner.HTMLTestRunner(output="HtmlReports", report_title="Porsche - Firefox")
#     runner.run(suite)


# if __name__ == "__main__":
#     unittest.main(AllureReports)








