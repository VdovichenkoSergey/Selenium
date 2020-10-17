from selenium import webdriver
from selenium.webdriver.common.by import By


dr = webdriver.Chrome()
dr.get("https://www-archive.mozilla.org/projects/ui/accessibility/unix/testcase/html/")

button = dr.find_element(By.NAME, "B1")
button.click()

alert = dr.switch_to.alert
print(alert.text)
alert.accept()

button2 = dr.find_element(By.NAME, "B2")
button2.click()
