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

driver.get('http://localhost/ampps/index.php?act=demos&soft=258')

frame = driver.find_element(By.NAME, 'demobody')
driver.switch_to.frame(frame)

wait = WebDriverWait(driver, 15)
sign_in = wait.until(expected_conditions.element_to_be_clickable(
    (By.XPATH, '//span[@class="ow_signin_label"]'))
)

sign_in.click()

username = driver.find_element(By. NAME, "identity")
password = driver.find_element(By. NAME, "password")
sign = driver.find_element(By. NAME, "submit")

action = (
    ActionChains(driver)
        .move_to_element(username)
        .click(username)
        .send_keys('admin')
        .move_to_element(password)
        .click(password)
        .send_keys('pass')
        .click(sign)
        .perform()
)