import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, WebDriverException
from selenium.webdriver.common.keys import Keys
f1 = open("C:\Python34\login.txt", "r");
credentials = []
for line in f1:
    credentials.append(line);
print(credentials);   
driver = webdriver.Chrome() 
driver.get('http://www.bits-pilani.ac.in:12349/Login.aspx');
driver.find_element_by_name("email").send_keys(credentials[0]);
driver.find_element_by_name("pass").send_keys(credentials[1] , Keys.RETURN);
#driver.find_element_by_name("pass").send_keys(keys.RETURN);
time.sleep(5);
driver.close()
print("hello");

