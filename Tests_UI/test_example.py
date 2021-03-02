from ShopMainPages import searchHelper

import time


def test_shearch(browser):
    shop_main_page = searchHelper(browser)
    shop_main_page.go_to_site()
    shop_main_page.enter_word_field_search("Платье нарядное")
    shop_main_page.click_search_button()
    time.sleep(5)
