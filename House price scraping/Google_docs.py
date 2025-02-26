from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Google_docs:
    def __init__(self):
        self.open_google_docs()

    def open_google_docs(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.chrome_options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeeaqnurHOUBHsqfZFdf3eRrKybtFvYq2_Fr7ZKLfhvhWkGuA/viewform?usp=sf_link")

    def fill_question(self, property_address, property_price, property_link):
        self.first_question = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        self.first_question.send_keys(property_address)

        self.second_question = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        self.second_question.send_keys(property_price)

        self.second_question = self.driver.find_element(By.XPATH,
                                                        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        self.second_question.send_keys(property_link)

        self.send_button = self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
        self.send_button.click()

        time.sleep(1)

        self.send_again = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        self.send_again.click()

        time.sleep(1)

