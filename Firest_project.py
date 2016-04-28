from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import re
import time
import os
import sys
import json

def writer(clicker):

	clicker.click();
	# WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))
	mems = driver.find_elements_by_xpath('//table[@class = "table table-striped"]');
	for a in mems:
		target.write(a.text + "\n");

url = "http://www.credaincr.org/4_subdivision_members.php";


if __name__ == '__main__':
	target = open("credaincr.txt" , "a") 
	target.truncate()
	driver = webdriver.Firefox()
	driver.get(url)	
	# mems = driver.find_elements_by_xpath('//table[@class = "table table-striped"]')
	# for a in mems:
	# 	target.write(a.text + "\n")
	# 	print (a.text);
	# clicker = driver.find_element_by_xpath('//a[@href = "#collapseTwo"]');
	# writer(clicker);
	# clicker = driver.find_element_by_xpath('//a[@href = "#collapseThree"]');
	# writer(clicker);
	# clicker = driver.find_element_by_xpath('//a[@href = "#collapsefour"]');
	# writer(clicker);
	# clicker = driver.find_element_by_xpath('//a[@href = "#collapsefive"]');
	# writer(clicker);
	mems = driver.find_elements_by_xpath('//table[@class = "table table-striped"]')
	for mem in mems:
		print(mem.text);
		target.write(mem.text);
	mems = 	driver.find_elements_by_xpath('//a[href = "collapseTwo"]//table[@class = "table table-striped"]')
	for mem in mems:
		print(mem.text);
		target.write(mem.text);

# with open("fileaname.txt","a+") as f:






#driver.quit();