import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get('https://www.google.com')
title=driver.title
print('Page Title:', title)
print("URL",driver.current_url)
source=driver.page_source
print('source length',len(source))
driver.maximize_window()
driver.back()
driver.forward()
time.sleep(2)
driver.quit