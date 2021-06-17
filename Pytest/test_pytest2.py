import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_SeleniumTest():
    driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
    driver.get("https://google.com")
    assert driver.title == "Google"
    time.sleep(5)
    driver.quit()





