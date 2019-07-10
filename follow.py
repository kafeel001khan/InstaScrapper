from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
# import pandas as pd
try:
    option = webdriver.ChromeOptions()
    option.add_argument(" --incognito")
    driver = webdriver.Chrome(executable_path="//home/daffolap-101/chromedriver", chrome_options=option)
    driver.get("https://www.instagram.com/accounts/login/?hl=en")
    sleep(5)
    username = driver.find_elements_by_tag_name('input')
    print (len(username), username)
    username[0].send_keys('shifaaindia')
    username[1].send_keys('Shifaa@#$%^&*')
    butten = driver.find_element_by_xpath("//button[contains(.,'Log In')]")
    print('hello ---->',butten.click())
    print('\n\nbutton --->', butten )
    sleep(5)
    butten = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]')
    print('hello ---->',butten.click())
    searchbox = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Search']")
    )
    )

    # send search into input

    searchbox.send_keys('unicefindia')
    sleep(2)
    # searchbox.submit()

    searchbox.send_keys(Keys.ENTER)
    sleep(1)
    searchbox.send_keys(Keys.ENTER)
        
    sleep(5)
    fo_list = driver.find_elements_by_xpath("//a[contains(.,' followers')]")
    if type(fo_list) == list:
        print(fo_list[0].click())
    else:
        print(fo_list.click())
    sleep(40)
    following_list = driver.find_elements_by_xpath("//button[contains(.,'Following')]")
    print ('following list --------->',len(following_list))
    follower_list = driver.find_elements_by_xpath("//button[contains(.,'Follow')]")
    ul_list = driver.find_elements_by_tag_name('ul')
    print('ul---->', len(ul_list))
    scr1 = driver.find_elements_by_xpath('/html/body/div[3]/div/div[2]')
    print ("scr ---->", scr1)
    print(driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1))
    for follow in follower_list:
        if 'Following' not in follow.get_attribute('innerHTML'):
            driver.execute_script("arguments[0].click();", follow)
            print('hello ----->')
    sleep(30)
    driver.close()
except Exception as e:
    print('\n\n in exception:--->{} \n\sn'.format(e))
    driver.close()
