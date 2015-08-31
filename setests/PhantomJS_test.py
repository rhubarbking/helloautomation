from selenium import webdriver
import os

driver = webdriver.PhantomJS("phantomjs.exe")
driver.set_window_size(1400, 1000)

driver.get("http://stackoverflow.com/")

print driver.title