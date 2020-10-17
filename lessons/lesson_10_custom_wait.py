from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

dr = webdriver.Chrome()
dr.get('https://demo.oxwall.com/')


wait = WebDriverWait(dr, 10)


def presence_of_elements_more_than_10(driver):
    print("new try")
    els = driver.find_elements(By.CLASS_NAME, "ow_newsfeed_item")
    if len(els) > 10:
        return els
    else:
        return False


results = wait.until(presence_of_elements_more_than_10, message="Less than 10")
print(results)


# wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "ow_newsfeed_item")), message="")