from scripts.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form .btn-add-to-basket")
    BASKET_TOTAL_TEXT = (By.CSS_SELECTOR, ".alertinner p strong")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    SUCCESS_TEXT_ITEM_NAME = (By.CSS_SELECTOR, "#messages .alertinner strong")


class ProductPage(BasePage):
    LINK_CITY_AND_STARS = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    LINK_CODERS_AT_WORK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    def add_to_cart(self):
        cart_button = self.driver.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        cart_button.click()

    def should_have_basket_total_text(self):
        item_price = self.driver.find_element(*ProductPageLocators.ITEM_PRICE).text
        basket_total_text = self.driver.find_element(*ProductPageLocators.BASKET_TOTAL_TEXT).text
        assert item_price == basket_total_text, "Item prices are not the same."

    def should_have_item_added_successfully_text(self):
        item_name = self.driver.find_element(*ProductPageLocators.ITEM_NAME).text
        success_text_item_name = self.driver.find_element(*ProductPageLocators.SUCCESS_TEXT_ITEM_NAME).text
        assert item_name == success_text_item_name, "Item names are not the same."

    def should_have_no_item_added_successfully_text(self):
        assert self.verify_element_absent(*ProductPageLocators.SUCCESS_TEXT_ITEM_NAME), \
            "Success message is present, but should not be."
