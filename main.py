from selenium import webdriver
import time
url = input("URL: ")

driver = webdriver.Firefox()
driver.get(url)
