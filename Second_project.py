from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import string 
import re


companies = []
driver = webdriver.Firefox();
url = "https://www.facebook.com";
driver.get(url);
"""throw = open("credaincr.txt" , "r+" );
a = []
for line in throw:
	a.append(line)
for i in range(0,15):
	stri = a[i];
	stri = stri[1:]
	a[i]= stri;
	elem = driver.find_element_by_id('mcaname').send_keys(a[i] , Keys.RETURN);
	try:
		 driver.find_element_by_find"""
email = driver.find_element_by_id("email");
email.send_keys("mgmohitgawande" );
passi = driver.find_element_by_id("pass");
passi.send_keys("9406924711" , Keys.RETURN);
driver.get("https://www.google.com")
a[i] = elem.text;
print a[i];
driver.navigate().back();
#driver.quit();