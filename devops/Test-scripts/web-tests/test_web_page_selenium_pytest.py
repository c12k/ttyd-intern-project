import pytest
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.common.exceptions import NoSuchElementException
opts = FirefoxOptions()
opts.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=opts)
# Get the homepage
driver.get("http://172.28.5.1:3000")
print(driver.title)
print(driver.current_url)
assert "test project" in driver.title
assert driver.find_element_by_class_name("login-content")
# Click the signup button and check we're in the register page
driver.find_element_by_xpath("//button[text()='Sign Up']").click()
print(driver.title)
print(driver.current_url)
assert "register" in driver.current_url
# Click the back button and make sure we're back on the home page
assert driver.find_element_by_class_name("register-form")
driver.find_element_by_id("register-back-btn").click()
# We expect this to fail at the moment
with pytest.raises(NoSuchElementException):
    driver.find_element_by_class_name("login-content")

driver.close()
