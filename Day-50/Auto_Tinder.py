# Imports
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

# CONSTANTS
CHROME_WEB_DRIVER = r"YOUR_CHROME_DRIVER"
FB_USERNAME = ""
FB_PASSWORD = ""
PHONE_NUMBER = ""
URL = "https://tinder.com/"

# Web Driver
driver = webdriver.Chrome(executable_path=CHROME_WEB_DRIVER)

# Get the base URL
driver.get(url=URL)

time.sleep(5)

# Login to Tinder
login_button = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
login_button.click()

time.sleep(5)
fb_login = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()

# Facebook Login
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

username_field = driver.find_element_by_xpath('//*[@id="email"]')
username_field.send_keys(FB_USERNAME)
password_field = driver.find_element_by_xpath('//*[@id="pass"]')
password_field.send_keys(FB_PASSWORD)
password_field.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)

time.sleep(5)

# Manage Popups
allow_location_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

notifications_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

cookies = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

# Send 100 Likes
for n in range(100):
    time.sleep(5)

    try:
        like_button = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()
        
        except NoSuchElementException:
            time.sleep(5)

# Close Driver
driver.close()


