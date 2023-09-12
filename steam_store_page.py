from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class SteamStorePage:
    def __init__(self, driver):
        self.driver = driver
        self.accept_cookies_button = (By.CSS_SELECTOR, "#acceptAllButton")
        self.search_input = (By.CSS_SELECTOR, "#store_nav_search_term")
        self.match_name_link = (By.CSS_SELECTOR, ".match_name:first-child")
        self.add_to_cart_button = (By.CSS_SELECTOR, "[id^='btn_add_to_cart']")
        self.remove_from_cart_button = (By.CSS_SELECTOR, ".remove_link")
        self.age_year_select = (By.CSS_SELECTOR, "select#ageYear")
        self.view_product_page_button = (By.CSS_SELECTOR, "#view_product_page_btn")
        self.cart_item_count = (By.CSS_SELECTOR, "#cart_item_count_value")
        self.confirm_button = (By.CLASS_NAME, "btn_green_steamui")

    def accept_cookies(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.accept_cookies_button)).click()

    def search_for_product(self, product_name):
        search_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.search_input))
        search_input.send_keys(product_name)

    def click_first_match(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.match_name_link)).click()

    def add_to_cart(self, index):
        buttons_list = (WebDriverWait(self.driver, 10).
                        until(EC.visibility_of_all_elements_located(self.add_to_cart_button)))
        buttons_list[index].click()

    def remove_from_cart(self, index):
        buttons_list = (WebDriverWait(self.driver, 10).
                        until(EC.visibility_of_all_elements_located(self.remove_from_cart_button)))
        buttons_list[index].click()

    def select_age_year(self, year):
        select = Select(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.age_year_select)))
        select.select_by_value(year)

    def view_product_page(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.view_product_page_button)).click()

    def get_cart_item_count(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.cart_item_count)).text

    def assert_cart_button_not_visible(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(self.cart_item_count))
        except TimeoutException:
            assert False, "Cart button is still visible."

    def confirm(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.confirm_button)).click()
