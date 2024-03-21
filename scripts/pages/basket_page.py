from scripts.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class BasketPageLocators:
    BASKET_IS_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEMS_SECTION = (By.CSS_SELECTOR, ".basket-items")


class BasketPage(BasePage):
    def should_be_basket_is_empty_text(self):
        basket_is_empty_text = self.driver.find_element(*BasketPageLocators.BASKET_IS_EMPTY_TEXT).text
        assert "Your basket is empty" in basket_is_empty_text, "No basket is empty text"

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS_SECTION), \
            "Basket items section is not empty"
