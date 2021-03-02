from ShopMainPages import searchHelper

import time


def test_search(browser):
    shop_main_page = searchHelper(browser)
    shop_main_page.go_to_site()
    shop_main_page.input_price_from("2")
    shop_main_page.input_price_to("10")
    shop_main_page.click_search_button_form()
    time.sleep(5)
