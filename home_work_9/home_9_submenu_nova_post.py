from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(2)
driver.get('https://novaposhta.ua/')

menu = driver.find_element(By.XPATH, '//ul/li/a[@href="http://novaposhta.ua/international_delivery"]')

action = (
    ActionChains(driver)
        .move_to_element(menu)
        .perform()
)

wait = WebDriverWait(driver, 5)
submenu = wait.until(expected_conditions.element_to_be_clickable(
    (By.XPATH, '//ul/li/a[@href="http://novaposhta.ua/international_delivery/chastnym_klientam_md"]'))
)
submenu.click()
