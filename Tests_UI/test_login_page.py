from ShopMainPages import searchHelper
import time


def test_login(browser):
    shop_login_page = searchHelper(browser)
    shop_login_page.go_to_site()
    shop_login_page.navbar_click_to_enter()
    shop_login_page.input_creds_mail("test@mail.com")
    shop_login_page.input_creds_pass("1")
    shop_login_page.input_creds_btn()
    time.sleep(5)



