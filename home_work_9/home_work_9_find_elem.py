import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(2)
driver.get('https://rozetka.com.ua/')


button = driver.find_element(By.XPATH, '//div[@class="menu-outer js-rz-fat-menu"]/button[@class="menu-toggler"]')
button.click()
# time.sleep(2)
element = driver.find_element(By.XPATH, '//a[@href="https://hard.rozetka.com.ua/monitors/c80089/" and '
                                        '@class="menu__link"]')
element.click()
# time.sleep(3)
monitor = driver.find_element(By.XPATH, '//a[@href="https://hard.rozetka.com.ua/aoc_c24g1/p58430061/"]/span['
                                        '@class="goods-tile__title"]')
# time.sleep(2)
monitor.click()
