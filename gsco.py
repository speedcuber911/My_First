from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()
driver.get("https://www.google-melange.com/gsoc/org/list/public/google/gsoc2015")
driver.find_element_by_class_name("ui-pg-selbox").click()
