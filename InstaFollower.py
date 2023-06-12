from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.common.exceptions import NoSuchElementException
import time


# A bot that logs into Instagram and follows an account's followers.
class InstaFollowerBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def scroll(self):
        """A function that scrolls the followers list so they load."""
        scroll_origin = ScrollOrigin.from_viewport(500, 500)
        ActionChains(self.driver).scroll_from_origin(scroll_origin, 0, 400).perform()

    def login(self, username, password):
        """A function that logs in using credentials provided"""
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(1)

        inputs = self.driver.find_elements(By.CSS_SELECTOR, '._aa48 input')
        inputs[0].send_keys(username)
        time.sleep(1)
        inputs[1].send_keys(password)
        time.sleep(1)

        log_in_button = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        log_in_button.click()

        time.sleep(5)

    def follow(self, account):
        """A function that follows 100 followers of a given account."""
        self.driver.get(f"https://www.instagram.com/{account}/")

        time.sleep(2)

        followers_button = self.driver.find_element(By.CSS_SELECTOR, '.x78zum5 li a')
        followers_button.click()

        time.sleep(1)

        # Number of accounts at a time (in this case 5)
        beginning = 0
        end = beginning + 5

        # Twenty times attempt to follow 5 accounts at a time while scrolling
        for i in range(20):
            for number in range(beginning, end):
                followers = self.driver.find_elements(By.CSS_SELECTOR, '.x1i10hfl button')
                if followers[number].text == "Follow":
                    followers[number].click()
                    time.sleep(1)
            beginning = end + 1
            end = beginning + 5
            self.scroll()

        print("Finished.")

