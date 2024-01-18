from selenium import webdriver
from selenium.webdriver.common.by import By

import time
input_url = input("URL: ")
price_min = input("Min price: ")
price_max = input("Max price: ")

page = 1
listings = []

driver = webdriver.Firefox()
driver.get(input_url)
try:
    price_min_field = driver.find_element(By.ID, "f_o_8_min")
    price_max_field = driver.find_element(By.ID, "f_o_8_max")
    price_min_field.send_keys(price_min)
    price_max_field.send_keys(price_max)
    price_max_field.submit()
except:
    pass

time.sleep(2)
url = driver.current_url

while True:
    driver.get(str(url + "page" + str(page) + ".html"))
    if "Sludinājumi dotajā kategorijā nav atrasti" in driver.page_source:
        break
    else:
        time.sleep(2)
        table_heading = driver.find_element(By.ID, "head_line")
        next_listing = table_heading.find_element(By.XPATH, "following-sibling::*")
        while True:
            try:
                next_listing = next_listing.find_element(By.XPATH, "following-sibling::*")
            except:
                break
            if next_listing.get_attribute("id") == "tr_bnr_712":
                break
            ad_id = next_listing.get_attribute("id")[3:]
            ad_url = next_listing.find_element(By.ID, str("dm_" + ad_id)).get_attribute("href")
            listings.append(ad_url)
        page = page + 1
print(listings)
input("Finished")
driver.quit()