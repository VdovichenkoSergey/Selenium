import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()

driver.maximize_window()
driver.minimize_window()

driver.get_window_size()  # you can get size of current browser window
driver.set_window_size(1280, 720)

driver.get_window_position()
driver.set_window_position(0, 0)