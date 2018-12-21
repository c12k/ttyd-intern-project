import pytest
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
opts = FirefoxOptions()
opts.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=opts)
# Get the homepage
driver.get("http://172.28.5.5:8081")
print(driver.title)
print(driver.current_url)
assert "Chat API test harness" in driver.title
print("Clicking submit button")
submit_elem = driver.find_element_by_xpath("//input[@name='submit']")
submit_elem.click()
print("Checking result")
assert "blah blah" in driver.find_element_by_xpath("/html/body/pre[1]/code/span[9]").text
assert "'UserID'" in driver.find_element_by_xpath("/html/body/pre[2]/code/span[5]").text
assert "'Hello'" in driver.find_element_by_xpath("/html/body/pre[2]/code/span[9]").text
print("Entering new user")
user_entry_elem = driver.find_element_by_xpath("/html/body/form/input[1]")
user_entry_elem.send_keys("101")
message_entry_elem = driver.find_element_by_xpath("/html/body/form/input[2]")
message_entry_elem.send_keys("222")
# Need to refind this each time the page refreshes
submit_elem = driver.find_element_by_xpath("//input[@name='submit']")
submit_elem.click()
print("Checking new result")
assert "blah blah" in driver.find_element_by_xpath("/html/body/pre[1]/code/span[9]").text
assert "'UserID101'" in driver.find_element_by_xpath("/html/body/pre[2]/code/span[5]").text
assert "'Hello222'" in driver.find_element_by_xpath("/html/body/pre[2]/code/span[9]").text
print("Checking old result moved down")
assert "'UserID'" in driver.find_element_by_xpath("/html/body/pre[4]/code/span[5]").text
assert "'Hello'" in driver.find_element_by_xpath("/html/body/pre[4]/code/span[9]").text
driver.close()