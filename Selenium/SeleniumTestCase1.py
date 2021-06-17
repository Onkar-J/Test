import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver_win32\chromedriver.exe')

driver.get("https://artoftesting.com/sampleSiteForSelenium")
print(driver.title)
time.sleep(5)

driver.find_element_by_id("fname").send_keys("Onkar Jadhav")

time.sleep(10)

driver.quit()
