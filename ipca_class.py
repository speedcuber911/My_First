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
		self.line_of_business = []
		self.location = []
		self.address = []
		self.pcode = []
		self.phone = []
		self.fax = []
		self.email = []
		self.site = []
		self.contact_person = []
		self.doc = []
		self.alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'L', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

	def setUp(self):
		self.driver = webdriver.PhantomJS()
		self.myfile = open("ipca_class.json","w")

	def firstStep(self):
			self.driver.get('http://www.ipcaindia.org/AllSearch.aspx?SearchString=all')
			
	def secondStep(self, alph=0):
		if alph:
			a = self.driver.find_element_by_id('btn_' + alph)
			a.click()
			time.sleep(4)
			self.scrape()
		else:
			for self.m in self.alp:
				y=1
				while y:
					try:
						a = self.driver.find_element_by_id('btn_' + self.m)
						a.click()
						time.sleep(4)
						self.scrape()
						y = 0
					except StaleElementReferenceException:
						time.sleep(2)

						
	def scrape(self):

			grid = self.driver.find_element_by_id('GridView1')
			block = self.driver.find_elements_by_class_name('style2')
					
			for i in block:
				j = i.find_elements_by_class_name('style6')
				if(j):
					self.info['sno'] = self.l
					self.info['company_name'] = j[0].text
					self.info['line_of_business'] = j[1].text
					self.info['location'] = j[2].text
					self.info['address'] = j[3].text
					self.info['pcode'] = j[4].text
					self.info['phone'] = j[5].text
					self.info['fax'] = j[6].text
					self.info['email'] = j[7].text
					self.info['site'] = j[8].text
					self.info['contact_person'] = j[9].text
					self.doc.append(self.info.copy())
					self.l+=1

					self.company_name.append(self.info['company_name'])
					self.line_of_business.append(self.info['line_of_business'])
					self.location.append(self.info['location'])
					self.address.append(self.info['address'])
					self.pcode.append(self.info['pcode'])
					self.phone.append(self.info['phone'])
					self.fax.append(self.info['fax'])
					self.email.append(self.info['email'])
					self.site.append(self.info['site'])
					self.contact_person.append(self.info['contact_person'])

	def desc(self):
		return self.doc

	def comp_name(self):
		return self.company_name
	def func_no_of_employee(self):
		return self.no_of_employee
	def func_line_of_business(self):
		return self.line_of_business
	def func_location(self):
		return self.location
	def func_address(self):
		return self.address
	def func_pcode(self):
		return self.pcode
	def func_phone(self):
		return self.phone
	def func_fax(self):
		return self.fax
	def func_email(self):
		return self.email
	def func_site(self):
		return self.site
	def func_contact_person(self):
		return self.contact_person
	
	def tearDown(self):
		self.driver.quit()
		self.myfile.write(json.dumps(self.doc))


if __name__ == '__main__':

	newObj = testpy()
	newObj.setUp()
	newObj.firstStep() #for all pages scrape
	newObj.secondStep()
	#newObj.secondStep('a') # or for a single page scrape data
	for i, j in enumerate(newObj.comp_name()):
		print i, ': ', j
	newObj.tearDown()