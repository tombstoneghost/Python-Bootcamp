# Imports
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

# CONSTANTS
CHROME_WEB_DRIVER = r"YOUR_CHROME_DRIVER"
INSTAGRAM_USERNAME = ""
INSTAGRAM_PASSWORD = ""
SIMILAR_ACCOUNT = ""

class InstagramFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_WEB_DRIVER)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")

        time.sleep(5)

        username_field = self.driver.find_element_by_name("username")
        password_field = self.driver.find_element_by_name("password")

        username_field.send_keys(INSTAGRAM_USERNAME)
        password_field.send_keys(INSTAGRAM_PASSWORD)
        password_field.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(url=f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(5)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(5)

        modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')

        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(5)

    def follow(self):
        all_buttons = self.driver.find_element_by_css_selector("li button")

        for button in all_buttons:
            try:
                button.click()
                time.sleep(5)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstagramFollower()
bot.login()
bot.find_followers()
bot.follow()

