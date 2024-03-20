from scripts.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
    SUCCESS_TEXT_ITEM_NAME = (By.CSS_SELECTOR, "#messages .alertinner strong")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_TOTAL_TEXT = (By.CSS_SELECTOR, ".alertinner p strong")


class ProductPage(BasePage):
    def add_to_cart(self):
        cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        cart_button.click()

    def should_be_basket_total_text(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        basket_total_text = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_TEXT).text
        assert item_price == basket_total_text, "Item prices are not the same."

    def should_be_item_added_successfully_text(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        success_text_item_name = self.browser.find_element(*ProductPageLocators.SUCCESS_TEXT_ITEM_NAME).text
        assert item_name == success_text_item_name, "Item names are not the same."

    def should_not_be_item_added_successfully_text(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_TEXT_ITEM_NAME), \
            "Success message is present, but should not be"
