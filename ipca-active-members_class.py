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
		self.company_name = []
		self.contacts = []
		self.address = []
		self.phone_fax = []
		self.email_site = []
		self.doc = []
	def setUp(self):
		self.driver = webdriver.PhantomJS()
		self.myfile = open("ipca-active-members_class.json","w")

	def firstStep(self, m=0):
			if m:
				self.driver.get('http://ipca.org.in/active-members/'+str(m)+'/')
				self.scrape()
			else:
				for self.m in range(1,62):
					self.driver.get('http://ipca.org.in/active-members/'+str(self.m)+'/')
					self.scrape()

	def scrape(self):
		grid = self.driver.find_elements_by_class_name('box4')
		for i in grid:
			j = i.find_elements_by_tag_name('tbody')
			if(j):
				self.info['sno'] = self.l
				self.info['company_name'] = j[1].text
				self.info['address'] = j[3].text
				self.info['phone_fax'] = j[4].text
				self.info['email_site'] = j[5].text
				self.info['contacts'] = j[6].text
				self.doc.append(self.info.copy())
				self.l += 1

				self.company_name.append(self.info['company_name'])
				self.address.append(self.info['address'])
				self.phone_fax.append(self.info['phone_fax'])
				self.email_site.append(self.info['email_site'])
				self.contacts.append(self.info['contacts'])
			
	def desc(self):
		return self.doc

	def comp_name(self):
		return self.company_name
	
	def func_contacts(self):
		return self.contacts

	def func_address(self):
		return self.address

	def func_phone_fax(self):
		return self.phone_fax

	def func_email_site(self):
		return self.email_site

	def tearDown(self):
		self.driver.quit()
		self.myfile.write(json.dumps(self.doc))


if __name__ == '__main__':

	newObj = testpy()
	newObj.setUp()
	newObj.firstStep() #for all pages scrape
	#newObj.firstStep(1) # or for a single page scrape data
	for i, j in enumerate(newObj.comp_name()):
		print i, ': ', j
	newObj.tearDown()