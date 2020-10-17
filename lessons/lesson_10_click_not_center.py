import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

dr = webdriver.Chrome()
dr.get('https://demo.oxwall.com/')

sign_up = dr.find_element(By.CLASS_NAME, 'ow_console_item_link')
print(sign_up.size)

action_chain = (
    ActionChains(dr)
        .move_to_element_with_offset(sign_up, sign_up.size['width'] - 2, sign_up.size['height'] / 2)
        .click()
        .perform()
)
