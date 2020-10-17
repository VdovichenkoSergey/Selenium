from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(2)
driver.get('https://www-archive.mozilla.org/projects/ui/accessibility/unix/testcase/html/')

radiobutton = driver.find_element(By.ID, "rbutton1")

print(radiobutton.is_enabled())
print(radiobutton.is_displayed())

if radiobutton.get_attribute('type') == 'radio':
    print('it is radiobutton')
else:
    print('it is not radiobutton')

print(radiobutton.is_selected())

radiobutton.click()

print(radiobutton.is_selected())