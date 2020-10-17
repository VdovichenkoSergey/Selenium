from selenium import webdriver
from selenium.webdriver.common.by import By

dr = webdriver.Chrome()
dr.get('https://demo.oxwall.com/')

dr.save_screenshot("filename.png")  # create screenshot of all page

element = dr.find_element(By.ID, 'B1')
element.screenshot('filename.png')  # create screenshot of found element
