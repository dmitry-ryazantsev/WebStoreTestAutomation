import math
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default ")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class BasePage:
    # the driver (browser) is called from conftest.py
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_basket(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def is_element_present(self, attribute, locator):
        try:
            self.browser.find_element(attribute, locator)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, attribute, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((attribute, locator)))
        except TimeoutException:
            return True

        return False

    def open(self):
        self.browser.get(self.url)

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not present"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")