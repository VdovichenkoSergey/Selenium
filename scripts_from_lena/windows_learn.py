import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


dr = webdriver.Chrome()
dr.get("https://www-archive.mozilla.org/projects/ui/accessibility/unix/testcase/html/")
dr.maximize_window()

actions = ActionChains(dr)
link = dr.find_element(By.LINK_TEXT, "Link to the end")
link.location_once_scrolled_into_view  # This line fix problem with Firefox scrolling

actions.key_down(Keys.CONTROL)
actions.click(link)
actions.key_up(Keys.CONTROL)
actions.perform()

time.sleep(2)

print(dr.window_handles)
print(dr.current_window_handle)

dr.switch_to.window(dr.window_handles[1])
dr.close()
print(dr.current_window_handle)

dr.switch_to.window(dr.window_handles[0])
print(dr.current_window_handle)

link = dr.find_element(By.LINK_TEXT, "Text Area Test Cases")
link.click()
