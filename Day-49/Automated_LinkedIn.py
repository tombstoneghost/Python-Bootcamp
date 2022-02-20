# Imports
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# CONSTANTS
CHROME_WEB_DRIVER = r"C:\Users\singh\Documents\ChromeWebDriver\chromedriver.exe"
USERNAME = ""
PASSWORD = ""
PHONE_NUMBER = ""
URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"

# Web Driver
driver = webdriver.Chrome(executable_path=CHROME_WEB_DRIVER)

# Get URL
driver.get(url=URL)

# Login to LinkedIn
driver.find_element_by_link_text("Sign in").click()

time.sleep(5)

username_field = driver.find_element_by_id("username")
username_field.send_keys(USERNAME)
password_field = driver.find_element_by_id("password")
password_field.send_keys(PASSWORD)
password_field.send_keys(Keys.ENTER)

# Apply to the Job
time.sleep(5)

apply_button = driver.find_element_by_class_name("jobs-apply-button")
apply_button.click()

time.sleep()
phone_number = driver.find_element_by_class_name("fb-single-line-text__input")

if phone_number.text == "":
    phone_number.send_keys(PHONE_NUMBER)

while driver.find_element_by_id("ember343"):
    next_button = driver.find_element_by_id("ember343")
    next_button.click()

review_button = driver.find_element_by_id("ember356")
review_button.click()

submit_button = driver.find_element_by_id("ember357")
submit_button.click()

time.sleep(5)

# Quit Driver
driver.quit()

