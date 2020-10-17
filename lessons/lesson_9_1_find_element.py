from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

dr = webdriver.Opera()

# dr.implicitly_wait(5)  # неявная задержка: ждать до 5 секунд (будет применяться ко всем find_ ... в последующих
# строках кода)
dr.get('https://duckduckgo.com/')


# el = dr.find_element_by_name('q')
# el2 = dr.find_element(By.NAME, 'q')


# e = dr.find_elements(By.CSS_SELECTOR, ".js-search-input.search__input--adv")
# if len(e) == 0:
#     print('no such elements')
# else:
#     print("element found")


def is_element_present(driver, by, value):
    e = driver.find_elements(by, value)
    if len(e) == 0:
        return True
    else:
        return False


print(is_element_present(dr, By.CSS_SELECTOR, ".js-search-input.search__input--adv"))

el3 = dr.find_element(By.CSS_SELECTOR, ".js-search-input.search__input--adv")
el3.send_keys('python')

button = dr.find_element_by_id('search_button_homepage')

time.sleep(2)  # задержка на 2 минуты (для дебага)

button.click()

time.sleep(2)

wait = WebDriverWait(dr, 5)
res = wait.until(
    expected_conditions.visibility_of_all_elements_located((By.PARTIAL_LINK_TEXT, 'Python'))
)  # так же заменяет следующую строку (ее уже можно не писать)

# link = dr.find_elements_by_partial_link_text('python')

res[2].click()

time.sleep(4)

dr.quit()  # close all tab of browser
# dr.close() - close current tab
