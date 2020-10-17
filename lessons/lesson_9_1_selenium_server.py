from selenium import webdriver
from selenium.webdriver.common.by import By
import time


dr = webdriver.Remote(
    desired_capabilities=webdriver.DesiredCapabilities.CHROME,
    command_executor="http://127.0.0.1:4444/wd/hub"
)
dr.get('https://duckduckgo.com/')

# el = dr.find_element_by_name('q')
el2 = dr.find_element(By.NAME, 'q')
el2.send_keys('python')
# el2.send_keys(Keys.ENTER)

button = dr.find_element_by_id('search_button_homepage')

time.sleep(2)

button.click()

time.sleep(2)

link = dr.find_elements_by_partial_link_text('python')


link[3].click()

dr.quit()  # close all tab of browser
# dr.close() - close current tab
