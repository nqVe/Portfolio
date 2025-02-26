from Otodom import Otodom
from Ui import Ui
from Google_docs import Google_docs
import time

otodom = Otodom()
ui = Ui()
otodom.go_through_details()
time.sleep(2)
otodom.start_scraping_data()
print(otodom.prices_list)
print(otodom.addresses_list)
print(otodom.links_list)
print(len(otodom.prices_list))
google_docs = Google_docs()
time.sleep(2)


for property in range(len(otodom.prices_list)):
    google_docs.fill_question(otodom.addresses_list[property], otodom.prices_list[property], otodom.links_list[property])

