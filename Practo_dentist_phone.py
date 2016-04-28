from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()
target = open("practo_detist_call.csv","a+")
opener = open("practo_datac.txt","r")
info = {"Name":"","phone":""}
for line in opener:
    driver.get(opener);
    info["Name"] = driver.find_element_by_tag_name("h1").text.encode('utf-8');
    print info["Name"];
    e = driver.find_element_by_class_name("book-toggle");
    e.click();
    try:
        driver.find_element_by_class_name("phone");
        info['phone']=driver.find_element_by_class_name("phone").text.encode('utf-8');
    except: NoSuchElementException
    target.write(info["Name"] + ",");
    target.write(info["phone"] + "\n");
