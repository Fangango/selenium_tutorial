import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def browser():
    chrome_obj = Service('drivers/chromedriver.exe')
    driver = webdriver.Chrome(service=chrome_obj)
    return driver
