from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://www.softaculous.com/softaculous/demos/Oxwall')

frame = driver.find_element(By.NAME, "demoheader")
driver.switch_to.frame(frame)

frame1 = driver.find_element(By.ID, "adminurl")
frame1.click()

driver.switch_to.parent_frame()  # switch to frame on one level higher
# driver.switch_to.default_content()  # switch to frame on the highest level
