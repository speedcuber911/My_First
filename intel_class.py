from selenium import webdriver
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.keys import Keys
import time
import os
import sys
import json

class testpy():
	def __init__(self):
		self.l = 1
		self.info = {}
		self.doc = []
		self.detail = []
		self.address = []
		self.phone = []
		self.site = []

	def setUp(self):
		self.driver = webdriver.PhantomJS()
		self.myfile = open("intel_class.json","w")

	def firstStep(self):
		self.driver.get('http://locator.intel.in/find-reseller/')
		self.loadPage()

	def loadPage(self):
		m = 0
		for s in range(3):
			x = 1
			while x:
				try:
					load_more = self.driver.find_element_by_id('load-more-results')
					load_more.click()
					print 'Waiting to load more fpr %d time %d !!' % (m, s)
					time.sleep(4)
					m +=1
				except NoSuchElementException:
					print 'error'
					x = 0
		self.scrape()

	def scrape(self):
		self.reseller = self.driver.find_elements_by_class_name('reseller')
						
		for i in self.reseller:
			details = i.find_element_by_tag_name('h4').text
			company_address = i.find_element_by_class_name('company_address')
			dd = i.find_elements_by_tag_name('dd')
			if len(dd) >1:
				phone = dd[0].text
				site = dd[1].text
			else:
				phone = dd[0].text
				site = 'Not Available'

			self.info['sno'] = self.l
			self.info['details'] = details
			self.info['address'] = company_address.text
			self.info['phone'] = phone
			self.info['site'] = site
			self.doc.append(self.info.copy())
			self.detail.append(self.info['details'])
			self.address.append(self.info['address'])
			self.phone.append(self.info['phone'])
			self.site.append(self.info['site'])
			
			self.l+=1
	def desc(self):
		return self.doc

	def details(self):
		return self.detail

	def func_address(self):
		return self.address

	def func_phone(self):
		return self.phone

	def func_site(self):
		return self.tsite

	def tearDown(self):
		self.driver.quit()
		self.myfile.write(json.dumps(self.doc))


if __name__ == '__main__':

	newObj = testpy()
	newObj.setUp()
	newObj.firstStep() 
	for i, j in enumerate(newObj.details()):
		print i, ': ', j
	newObj.tearDown()