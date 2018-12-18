import pytest
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
opts = FirefoxOptions()
opts.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=opts)
driver.get('http://172.28.5.3:5000')
print(driver.current_url)
assert driver.find_element_by_tag_name("body").text == "hello from Rasa NLU: 0.13.7"
