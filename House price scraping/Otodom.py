from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

from selenium.common.exceptions import NoSuchElementException

class Otodom:

    prices_list = []
    addresses_list = []
    links_list = []

    def __init__(self):
        self.open_otodom()

    def open_otodom(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.chrome_options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get("https://www.otodom.pl/")

        time.sleep(2)

        self.accept_cookies = self.driver.find_element(By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
        self.accept_cookies.click()

        time.sleep(2)

    def go_through_details(self):

        try:
            time.sleep(0.5)
            self.search_text = self.driver.find_element(By.CLASS_NAME, value='ekudn6m0.css-16294r4')
            self.wait = WebDriverWait(self.search_text, timeout=2)
            self.wait.until(lambda d: self.search_text.is_displayed())

            print("check!")
        except NoSuchElementException:
            time.sleep(0.5)
            self.go_through_details()

    def start_scraping_data(self):
        self.property_prices = self.driver.find_elements(By.CLASS_NAME, value='css-2bt9f1.evk7nst0')
        for price in self.property_prices:
            price_without_spacer = price.text.replace(" ", "")
            price_without_comas = price_without_spacer.replace(",", ".")
            price_without_zl = price_without_comas[:-2]
            try:
                price_float = float(price_without_zl)
            except ValueError:
                price_float = str("Brak ceny")
            self.prices_list.append(price_float)

        self.property_addresses = self.driver.find_elements(By.CLASS_NAME, value='css-42r2ms.eejmx80')
        for address in self.property_addresses:
            self.addresses_list.append(address.text)

        self.property_links = self.driver.find_elements(By.CLASS_NAME, value='css-16vl3c1.e17g0c820')
        for link in self.property_links:
            self.links_list.append(link.get_attribute('href'))

        try:
            if self.driver.find_element(By.XPATH, value='//*[@title="Go to next Page"]').is_displayed():
                self.driver.find_element(By.XPATH, value='//*[@title="Go to next Page"]').click()
                time.sleep(2)
                self.start_scraping_data()
            else:
                pass
        except NoSuchElementException:
            pass

