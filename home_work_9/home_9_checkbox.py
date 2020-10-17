from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(2)
driver.get('https://www-archive.mozilla.org/projects/ui/accessibility/unix/testcase/html/')

checkbox = driver.find_element(By.ID, "checkbox2")

if checkbox.get_attribute('type') == 'checkbox':
    print('element is checkbox')
else:
    print('element is not checkbox')

print(checkbox.is_enabled())
print(checkbox.is_displayed())

checkbox.click()

print(checkbox.is_selected())
