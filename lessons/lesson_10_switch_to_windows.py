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

link = driver.find_element(By.XPATH, '//li/a[@href="#Button_Test_Cases"]')

action = (
    ActionChains(driver)
        .move_to_element(link)
        .key_down(Keys.CONTROL)
        .click(link)
        .key_up(Keys.CONTROL)
        .perform()
)

time.sleep(2)

print(driver.window_handles)  # IDs of all opened browser windows
print(driver.current_window_handle)  # ID of current window

driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
driver.close()