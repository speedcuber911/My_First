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
		self.tbody = []
		self.doc = []
		self.company_name_address = []
		self.email = []
		self.site = []
		self.cell = []
		self.fax = []
		self.o = []
		self.r = []
	def setUp(self):
		self.driver = webdriver.PhantomJS()
		self.myfile = open("lmtma_class.json","w")

	def firstStep(self, m=0):
		if m:
			self.driver.get('http://www.lmtma.org/Member/index_'+str(m)+ '.html')
			self.secondStep()
		else:
			for self.m in range(0, 241, 5):
				self.driver.get('http://www.lmtma.org/Member/index_'+str(self.m)+ '.html')
				self.secondStep()
	def secondStep(self):
		self.tbody = self.driver.find_elements_by_xpath('.//*[contains(@bgcolor, "#FFFFFF")]')
		self.scrape()

	def scrape(self):

		for i in self.tbody[1:]:
			j = i.find_elements_by_tag_name('td')
			a = j[0].find_elements_by_tag_name('a')	
			tr = j[1].find_elements_by_tag_name('tr')
			if(j):
				self.info['sno'] = self.l
				
				self.info['company_name_address'] = j[0].text
				if len(a)>1:
					self.info['email'] = a[1].get_attribute('href')
					self.info['site'] = a[0].get_attribute('href')
				elif len(a) == 1:
					self.info['email'] = a[0].get_attribute('href')
					self.info['site'] = ''
				self.info['cell'] = tr[4].text
				self.info['fax'] = tr[2].text
				self.info['(o)'] = tr[1].text
				self.info['(r)'] = tr[3].text			
				self.doc.append(self.info.copy())
				self.l+=1
				
				self.company_name_address.append(self.info['company_name_address'])
				self.email.append(self.info['email'])
				self.site.append(self.info['site'])
				self.cell.append(self.info['cell'] )
				self.fax.append(self.info['fax'] )
				self.o.append(self.info['(o)'])
				self.r.append(self.info['(r)'])

	def desc(self):
		return self.doc
	def company_name_addresss(self):
		return self.company_name_address
	def func_email(self):
		return self.email
	def func_site(self):
		return self.site
	def func_cell(self):
		return self.cell
	def func_fax(self):
		return self.fax
	def func_o(self):
		return self.o
	def func_r(self):
		return self.r

	def tearDown(self):
		self.driver.quit()
		self.myfile.write(json.dumps(self.doc))


if __name__ == '__main__':

	newObj = testpy()
	newObj.setUp()
	newObj.firstStep() #for all pages scrape
	#newObj.firstStep(1) # or for a single page scrape data
	for i, j in enumerate(newObj.company_name_addresss()):
		print i, ': ', j
	newObj.tearDown()