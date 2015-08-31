from selenium import webdriver
import os

phantomjs_path = "C:\Selenium\phantomjs-2.0.0-windows\bin\phantomjs.exe"

browser = webdriver.PhantomJS(executable_path=phantomjs_path, service_log_path=os.path.devnull)
browser.set_window_size(1400, 1000)

browser.get("http://stackoverflow.com/")

print browser.title