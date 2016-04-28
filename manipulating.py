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

url = "https://www.practo.com/delhi/diagnostics/tests"
g_url = "https://www.google.co.in/search?q=diagnostic+labs+in+delhi&gws_rd=ssl#q=diagnostic+labs+in+delhi&tbm=lcl"


def list_str(liste):
	new_liste =[]
	
	for elem in liste:
		try:
			new_liste.append(str(elem.text))
		except:
			new_liste.append(elem.text)
	return new_liste
		
driver = webdriver.Firefox()

comp_name = []
comp_address = []
prices = []
phone_no = []

driver.get(url)
number = int(str(driver.find_element_by_xpath('//h4[@style="display:inline;"]').text).split(' ')[0])
new_url = "https://www.practo.com/delhi/diagnostics/tests?sort_by=relavence&filters[min_fee]=0&filters[max_fee]=1000&page="
for i in xrange(1,(number/10) + 1):
	url = new_url + str(i)
	driver.get(url)
	clickable = driver.find_elements_by_class_name("button-text")
	print len(clickable)
	for i in xrange(len(clickable)):
		clickable[i].click()
		WebDriverWait(driver,10)
		phone_no = list_str(driver.find_elements_by_xpath('//div[@class="phone_and_ext"]/span[2]/b'))

	WebDriverWait(driver,2)
	
	comp_names = list_str(driver.find_elements_by_xpath('//h2[@itemprop="name"]'))
	
	prices = list_str(driver.find_elements_by_class_name("diag-price"))

	comp_address = list_str(driver.find_elements_by_xpath('//span[@class="centre-address"]/a'))

	print zip(comp_names,comp_address,phone_no)

driver.quit()