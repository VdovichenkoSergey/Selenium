from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(2)
driver.get('https://novaposhta.ua/')

menu = driver.find_element(By.XPATH, '//ul/li/a[@href="http://novaposhta.ua/international_delivery"]')
submenu = driver.find_element(By.XPATH, '//ul/li/a[@href="http://novaposhta.ua/international_delivery'
                                        '/chastnym_klientam_md"]')

action = (
    ActionChains(driver)
        .move_to_element(menu)
        .pause(1)
        .click(submenu)
        .perform()
)
