import pytest
from steam_store_page import SteamStorePage


class TestCart:
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_add_to_cart(self, browser):
        page = SteamStorePage(browser)
        page.search_for_product("Hollow Knight")
        page.click_first_match()
        page.add_to_cart(0)
        page.search_for_product("Baldur's Gate 3")
        page.click_first_match()
        page.select_age_year("2000")
        page.view_product_page()
        page.add_to_cart(0)
        cart_value = page.get_cart_item_count()
        assert cart_value == "2"

    @pytest.mark.regression
    def test_add_the_same_product_twice(self, browser):
        page = SteamStorePage(browser)
        page.search_for_product("Hollow Knight")
        page.click_first_match()
        page.add_to_cart(0)
        page.search_for_product("Hollow Knight")
        page.click_first_match()
        page.add_to_cart(0)
        cart_value = page.get_cart_item_count()
        assert cart_value == "1"

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_remove_from_cart(self, browser):
        page = SteamStorePage(browser)
        page.search_for_product("Minecraft")
        page.click_first_match()
        page.add_to_cart(0)
        page.search_for_product("Red Dead Redemption 2")
        page.click_first_match()
        page.add_to_cart(0)
        page.search_for_product("Victoria 3")
        page.click_first_match()
        page.add_to_cart(0)

        # removing the second item from the cart
        page.remove_from_cart(1)
        cart_value = page.get_cart_item_count()
        assert cart_value == "2"

        # using the -1 index will click the "Remove all" button
        page.remove_from_cart(-1)
        page.confirm()
        page.assert_cart_button_not_visible()
