from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import time

dr = webdriver.Chrome()
dr.get("https://www-archive.mozilla.org/projects/ui/accessibility/unix/testcase/html/#DropdownListbox_Test_Cases")

el = dr.find_element(By.NAME, "DropdownListbox_Test_Cases")

position = dr.execute_script("return arguments[0].getBoundingClientRect();", el)
print(el.location)
print(round(position["top"]))
print(round(position["left"]))
print(dr.get_window_size())

# Всё таки метод ниже не совсем заменяет JS код выше.
# Т.к. перед тем как вернуть нам положение элемента, здесь есть действие скроллинга.
# А если нам нужно выяснить где находится элемент от действий, которые мы совершили ранее,
# то этот метод нам ответ не даст, т.к. он еще и сначала прокрутит к этому элементу
print(el.location_once_scrolled_into_view)


# el = dr.find_element(By.NAME, "end")
# print(el.location)
# print(el.location_once_scrolled_into_view)
# window_size = dr.get_window_size()
# print(window_size)
# print(el.size["height"] < window_size["height"])
# assert el.size["height"] < window_size["height"]
