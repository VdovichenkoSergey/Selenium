from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://www.softaculous.com/softaculous/demos/Oxwall')

frame = driver.find_element(By.NAME, "demoheader")
driver.switch_to.frame(frame)

sign_in = driver.find_element(By.ID, "adminurl")
sign_in.click()