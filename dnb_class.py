from selenium import webdriver
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, WebDriverException
from selenium.webdriver.common.keys import Keys
import time
import os
import sys
import json

class testpy():
	def __init__(self):
		self.l = 1
		self.info = {}
		self.m = 0
		self.grid = 0
		self.rows = []
		self.company_name = []
		self.city = []
		self.no_of_employee = []
		self.turnover_range = []
		self.doc = []
		self.max_pages = 50
		self.check = 1
	def setUp(self):
		self.driver = webdriver.PhantomJS()
		self.myfile = open("dnb_class.json","w")

	def firstStep(self, m=0):
		if m:
			self.driver.get('http://www.dnb.co.in/SMEs/company_listing.asp?PageNo='+str(m)+'&q=alphabetical&r=')
			self.secondStep()
		else:
			for self.m in range(1,self.max_pages):
				if self.check:
					self.driver.get('http://www.dnb.co.in/SMEs/company_listing.asp?PageNo='+str(self.m)+'&q=alphabetical&r=')
					self.secondStep()
				else:
					break
	def secondStep(self):
		self.grid = self.driver.find_element_by_xpath('/html/body/table/tbody/tr[4]/td/table/tbody/tr[3]/td/table')	
		self.rows = self.grid.find_elements_by_tag_name('tr')
		self.scrape()

	def scrape(self):
		if len(self.rows)<3:
			self.check = 0
		 	return
			
		else:	
			for row in self.rows[1:]:
				td = row.find_elements_by_tag_name('td')			
				if len(td)>2:
					self.info['sno'] = td[0].text
					self.info['company_name'] = td[1].text
					self.info['city/district'] = td[2].text
					self.info['no_of_employee'] = td[3].text
					self.info['turnover_range'] = td[4].text
					self.company_name.append(self.info['company_name'])
					self.city.append(self.info['city/district'])
					self.no_of_employee.append(self.info['no_of_employee'])
					self.turnover_range.append(self.info['turnover_range'])
					self.doc.append(self.info.copy())
			
	def desc(self):
		return self.doc

	def func_no_of_employee(self):
		return self.no_of_employee

	def func_comp_name(self):
		return self.company_name

	def func_city(self):
		return self.city

	def func_turnover_range(self):
		return self.turnover_range

	def tearDown(self):
		self.driver.close()
		self.myfile.write(json.dumps(self.doc))


if __name__ == '__main__':

	newObj = testpy()
	newObj.setUp()
	newObj.firstStep() #for all pages scrape
	#newObj.firstStep('1') # or for a single page scrape data
	for i, j in enumerate(newObj.comp_name()):
		print i, ': ', j
	newObj.tearDown()