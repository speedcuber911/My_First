from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.PhantomJS();
target = open("justdial_dietician.txt","a+")
url = "http://www.justdial.com/Delhi-NCR/Dietitians/ct-458653/page-";
for i in range(1,51):
    url = url + str(i)
    driver.get(url);
    list = driver.find_elements_by_xpath("//span[@class = 'jcn']/a");
    for l in list:
        print l.get_attribute("href");
        target.write(l.get_attribute("href"));
target.close();
