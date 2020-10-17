from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

dr = webdriver.Chrome()
dr.get('https://demo.oxwall.com/')

wait = WebDriverWait(dr, 10)


# def presence_of_elements_more_than_10(driver):
#     print("new try")
#     els = driver.find_elements(By.CLASS_NAME, "ow_newsfeed_item")
#     if len(els) > 10:
#         return els
#     else:
#         return False

class presence_of_elements_number:
    def __init__(self, locator, number):
        self.locator = locator
        self.number = number

    def __call__(self, driver):
        print("new try")
        els = driver.find_elements(By.CLASS_NAME, "ow_newsfeed_item")
        if len(els) > self.number:
            return els


results = wait.until(presence_of_elements_number((By.CLASS_NAME, "ow_newsfeed_item"), 9), message="Less than 9")
print(len(results))

# wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "ow_newsfeed_item")), message="")
