from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('promo_offer', range(10))
def test_guest_can_add_product_to_basket(driver, promo_offer):
    link = ProductPage.LINK_CODERS_AT_WORK + f"?promo=offer{promo_offer}"
    page = ProductPage(driver, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_have_item_added_successfully_text()
    page.should_have_basket_total_text()


def test_guest_can_go_to_login_page_from_product_page(driver):
    page = ProductPage(driver, ProductPage.LINK_CITY_AND_STARS)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(driver, driver.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(driver):
    page = ProductPage(driver, ProductPage.LINK_CITY_AND_STARS)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(driver, driver.current_url)
    basket_page.should_have_no_items_in_basket()
    basket_page.should_have_empty_basket_text()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
    page = ProductPage(driver, ProductPage.LINK_CITY_AND_STARS)
    page.open()
    page.add_to_cart()
    page.should_have_no_item_added_successfully_text()


def test_guest_cant_see_success_message(driver):
    page = ProductPage(driver, ProductPage.LINK_CITY_AND_STARS)
    page.open()
    page.should_have_no_item_added_successfully_text()


def test_guest_should_see_login_link_on_product_page(driver):
    page = ProductPage(driver, ProductPage.LINK_CITY_AND_STARS)
    page.open()
    page.should_be_login_link()
