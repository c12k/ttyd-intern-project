import pytest
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
opts = FirefoxOptions()
opts.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=opts)
# Get the homepage
driver.get("http://172.28.5.2:80")
print(driver.title)
print(driver.current_url)
assert "Data API test harness" in driver.title
print("Clicking init button")
init_elem = driver.find_element_by_xpath("//input[@name='init']")
init_elem.click()
assert "init" in driver.current_url
assert "csv loaded" in driver.page_source
for i in range(0, 9):
    print("Clicking listCust button")
    cust_elem = driver.find_element_by_xpath("//input[@name='listCust']")
    cust_elem.click()
    assert "listCust" in driver.current_url
    assert "customer" in driver.find_element_by_xpath("/html/body/pre/code/span[4]").text
    print("Clicking listProd button")
    prod_elem = driver.find_element_by_xpath("//input[@name='listProd']")
    prod_elem.click()
    assert "listProd" in driver.current_url
    assert "product" in driver.find_element_by_xpath("/html/body/pre/code/span[4]").text
    print("Clicking listTotal button")
    total_elem = driver.find_element_by_xpath("//input[@name='listTotal']")
    total_elem.click()
    assert "listTotal" in driver.current_url
    assert "Australia" in driver.find_element_by_xpath("/html/body/pre/code/span[5]").text
driver.close()
