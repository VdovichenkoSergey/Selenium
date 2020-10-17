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
driver.implicitly_wait(5)
driver.get('https://www-archive.mozilla.org/projects/ui/accessibility/unix/testcase/html/')

button = driver.find_element(By.NAME, 'B1')
#
print(button.location)


position = driver.execute_script("return arguments[0].getBoundingClientRect();", button)
print(position)
print(round(position['left']), round(position['top']))

driver.close()