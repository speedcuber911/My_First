import time
import math
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, WebDriverException
from selenium.webdriver.common.keys import Keys
driver = webdriver.PhantomJS();
driver.get('http://www.bits-pilani.ac.in:12349/StudentSearch.aspx');
driver.find_element_by_name("idnoTxt").send_keys("2013B1" , Keys.RETURN);

ide = driver.find_elements_by_xpath("//*[@id='searchResultGridView']/tbody/tr/td[1]");
for i in ide:
    ider = i.text
    a = ider[0:4]
    b = ider [8:11]
    ider = "f" + a + b + "@pilani.bits-pilani.ac.in"
    print ider
