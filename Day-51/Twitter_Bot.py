# Imports
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# CONSTANTS
CHROME_WEB_DRIVER = r"YOUR_CHROME_DRIVER"
TWITTER_USERNAME = ""
TWITTER_PASSWORD = ""
MIN_SPEED_DOWN = 120
MIN_SPEED_UP = 10

# Internet Speed Bot
class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_WEB_DRIVER)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(url="https://www.speedtest.net/")

        time.sleep(5)

        # Click on Go
        go_button = self.driver.find_element_by_class_name("start-text")
        go_button.click()

        time.sleep(60)

        # Get Speed
        download_speed = self.driver.find_element_by_class_name("download-speed").text
        upload_speed = self.driver.find_element_by_class_name("upload-speed").text

        self.down = download_speed
        self.up = upload_speed

        # Close Driver
        self.driver.close()

    def tweet_at_provider(self):
        self.driver.get(url="https://twitter.com/login")


        time.sleep(5)

        # Login to Twitter
        username_field = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
        password_field = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')

        username_field.send_keys(TWITTER_USERNAME)
        password_field.send_keys(TWITTER_PASSWORD)
        password_field.send_keys(Keys.ENTER)

        time.sleep(5)

        # Compose Tweet
        tweet_compose = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        tweet = f"Hey ISP, my internet speed is not as promised. It's currently giving {self.down} DOWN and {self.up} UP. "
        tweet_compose.send_keys(tweet)

        time.sleep(5)

        # Click Tweet
        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()



# Main
bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()

