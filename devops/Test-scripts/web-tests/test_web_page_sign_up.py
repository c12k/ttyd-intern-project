import pytest
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
opts = FirefoxOptions()
opts.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=opts)
# Get the homepage
driver.get("http://172.28.5.1:3000")
# Click the signup button and check we're in the register page
driver.find_element_by_xpath("//button[text()='Sign Up']").click()
print(driver.title)
print(driver.current_url)
assert "register" in driver.current_url
print("Entering username")
username_elem = driver.find_element_by_id("username")
username_elem.send_keys("testuser")
print("Entering password")
password_elem = driver.find_element_by_id("register_password")
password_elem.send_keys("secure")
# This should have some sort of error message if passwords don't match but ignoring for now
retype_pw_elem = driver.find_element_by_xpath("//input[@name='rpassword']")
retype_pw_elem.send_keys("secure")
print("Entering email")
email_elem = driver.find_element_by_id("email")
email_elem.send_keys("mygmail@gmail.com")
print("Clicking submit")
submit_btn_elem = driver.find_element_by_id("register-submit-btn")
submit_btn_elem.submit()
try:
    element = WebDriverWait(driver, 10).until(
        EC.title_is("test project")
    )
finally:
    driver.quit()
driver.close()
