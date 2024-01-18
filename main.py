from selenium import webdriver
from selenium.webdriver.common.by import By

import time
url = input("URL: ")
price_min = input("Min price: ")
price_max = input("Max price: ")

driver = webdriver.Firefox()
driver.get(url)
time.sleep(2)

price_min_field = driver.find_element(By.ID, "f_o_8_min")
price_max_field = driver.find_element(By.ID, "f_o_8_max")
price_min_field.send_keys(price_min)
price_max_field.send_keys(price_max)

