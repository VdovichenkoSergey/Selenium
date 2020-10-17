import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(2)
driver.get('https://rozetka.com.ua/')

button = driver.find_element(By.XPATH, '//div[@class="menu-outer js-rz-fat-menu"]/button[@class="menu-toggler"]')
button.click()

menu_block = driver.find_element(By.XPATH, '//ul[@class="menu-categories"]/li/a['
                                           '@href="https://rozetka.com.ua/instrumenty-i-avtotovary/c4627858/"]')
submenu = driver.find_element(By.XPATH, '//a[@href="https://rozetka.com.ua/jigsaws/c152505/" and @class="menu__link"]')

action = ActionChains(driver)
action.move_to_element(menu_block)
action.click(submenu)
action.perform()