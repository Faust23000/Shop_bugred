import pytest
from selenium import webdriver

from Tests_API.client import ShopBugredClient


@pytest.fixture(scope="session")
def client():
    client = ShopBugredClient("http://shop.bugred.ru")
    client.authorize("test@mail.com", "1")
    return client

@pytest.fixture(scope="session") #Функция будет исполнятся только 1 раз тестовую сессию
def browser():
    driver = webdriver.Chrome(executable_path="../chromedriver.exe")
    yield driver

    driver.quit()