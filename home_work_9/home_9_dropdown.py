from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(2)
driver.get('https://www-archive.mozilla.org/projects/ui/accessibility/unix/testcase/html/')

combobox = driver.find_element(By.ID, "options")  # find element with tag "select"

dropdown = Select(combobox)
# dropdown.select_by_index(2)
# dropdown.select_by_value('stock')  # atribute "value"
dropdown.select_by_visible_text('option4')
