import pytest
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
opts = FirefoxOptions()
opts.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=opts)
driver.get('http://192.168.99.100:3000')
print(driver.title)
assert "test project" in driver.title
driver.close()
