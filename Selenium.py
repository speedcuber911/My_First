import time
import math
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, WebDriverException
from selenium.webdriver.common.keys import Keys
flag =1;
target = open("names.txt" , "w");   
driver = webdriver.Firefox() 
driver.get('http://www.bits-pilani.ac.in:12349/StudentSearch.aspx');
driver.find_element_by_name("idnoTxt").send_keys("2013B1" , Keys.RETURN);
elements = driver.find_elements_by_tag_name('td');
for a in elements:
    target.write(a.text)
    if(flag!=4 and a.text[0]== '2'):
        flag=flag+1
        target.write("\t");
    else:
        flag = 1;
        target.write("\n");
driver.quit()
target.close();
print("hello");

