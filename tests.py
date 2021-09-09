import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get('http://google.com')
print('Title: %s' % browser.title)
time.sleep(2)
browser.quit()


