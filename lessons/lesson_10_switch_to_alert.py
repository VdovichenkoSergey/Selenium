from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://www-archive.mozilla.org/projects/ui/accessibility/unix/testcase/html/')

button = driver.find_element(By.NAME, 'B1')
button.click()

alert = driver.switch_to.alert
alert_text = alert.text  # save alert text
alert.accept()  # imitate [OK]
alert.dismiss()  # imitate [Cancel]

# button2 = driver.find_element(By.NAME, 'B2')
# button.click()
