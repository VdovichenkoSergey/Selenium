from selenium import webdriver
from selenium.webdriver.common.by import By

dr = webdriver.Chrome()

dr.get("https://www.softaculous.com/softaculous/demos/Oxwall")
dr.implicitly_wait(5)
frame_element = dr.find_element(By.NAME, "demoheader")
dr.switch_to.frame(frame_element)

sign_in = dr.find_element(By.ID, "adminurl")
sign_in.click()

dr.switch_to.parent_frame()
