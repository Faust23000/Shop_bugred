from BaseApp import BasePage
from selenium.webdriver.common.by import By
import time


class SeacrhLocators:
    LOCATOR_SEARCH_FIELD = (By.NAME, "q")
    LOCATOR_SEARCH_BUTTON = (By.XPATH, "//button[text()='Найти']")

    LOCATOR_SEARCH_FIELD_INPUT1_FORM_ = (By.NAME, "price_from")
    LOCATOR_SEARCH_FIELD_INPUT2_FORM_ = (By.NAME, "price_to")
    LOCATOR_SEARCH_BUTTON_FORM = (By.XPATH, "//form/p/button[text()='Найти']")

    LOCATOR_FILTER_CHECK_BLACK = (By.XPATH, "//form/p[2]/input")
    LOCATOR_CHOICE_ITEAMS = (By.XPATH, "//div[@class='col-md-4']/a")
    LOCATOR_NAVBAR_ENTER = (By.XPATH, "//div[@id='navbarSupportedContent']//a[text()='Вход ']")

    LOCATOR_ENTER_INPUT_FIELD_EMAIL = (By.ID, "exampleInputEmail1")
    LOCATOR_ENTER_INPUT_FIELD_PASSWORD = (By.ID, "exampleInputPassword1")
    LOCATOR_ENTER_BTN_ENTER = (By.NAME, "_csrf")



class searchHelper(BasePage):

    def enter_word_field_search(self, word):
        search_field = self.find_element(SeacrhLocators.LOCATOR_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_search_button(self):
        return self.find_element(SeacrhLocators.LOCATOR_SEARCH_BUTTON, time=3).click()

    def input_price_from(self, word):
        search_field = self.find_element(SeacrhLocators.LOCATOR_SEARCH_FIELD_INPUT1_FORM_)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def input_price_to(self, word):
        search_field = self.find_element(SeacrhLocators.LOCATOR_SEARCH_FIELD_INPUT2_FORM_)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_search_button_form(self):
        return self.find_element(SeacrhLocators.LOCATOR_SEARCH_BUTTON_FORM, time=3).click()

    def navbar_click_to_enter(self):
        return self.find_element(SeacrhLocators.LOCATOR_NAVBAR_ENTER).click()

    def input_creds_mail(self, email):
        search_field = self.find_element(SeacrhLocators.LOCATOR_ENTER_INPUT_FIELD_EMAIL, time=2)
        search_field.click()
        search_field.send_keys(email)
        return search_field

    def input_creds_pass(self, password):
        search_field = self.find_element(SeacrhLocators.LOCATOR_ENTER_INPUT_FIELD_PASSWORD, time=2)
        search_field.click()
        search_field.send_keys(password)
        return search_field

    def input_creds_btn(self, password):
        search_field = self.find_elements(SeacrhLocators.LOCATOR_ENTER_BTN_ENTER).click()
        return search_field
