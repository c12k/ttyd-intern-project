import pytest
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
opts = FirefoxOptions()
opts.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=opts)
driver.get('http://172.28.5.1:3000')
print(driver.title)
print(driver.current_url)
assert "test project" in driver.title
driver.find_element_by_xpath("//button[text()='Sign Up']").click()
print(driver.title)
print(driver.current_url)
assert "register" in driver.current_url
assert driver.find_element_by_class_name("register-form")
driver.close()
