from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# driver = webdriver.Firefox()
cap = DesiredCapabilities().FIREFOX
cap["marionette"] = False
driver = webdriver.Firefox(capabilities=cap, executable_path=r'/home/daffolap-101/Downloads/geckodriver')
driver.get("https://www.instagram.com/accounts/login/")
# driver.get("http://www.python.org")
# elem = driver.find_element_by_id("f37ed25e4e5efec")
# elem.clear()
# elem.send_keys("user1")
# elem.send_keys(Keys.RETURN)
elem = driver.find_element_by_name('password')
elem.clear()
elem.send_keys("password")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source