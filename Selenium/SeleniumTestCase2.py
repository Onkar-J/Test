import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver_win32\chromedriver.exe')

driver.get("https://artoftesting.com/sampleSiteForSelenium")
print(driver.title)

driver.find_element_by_xpath('//*[@id="post-1089"]/div/div/form[2]/input[1]').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="post-1089"]/div/div/p[4]/a').click()

time.sleep(5)
driver.quit()
