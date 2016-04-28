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
		self.doc = []
		self.info = {}
		self.alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
		self.l = 1
		self.data = []
		self.m = ''
		self.company_name = []
		self.honary_memeber = []
		self.contact_person = []
		self.reference_person = []
		self.address = []
		self.pcode = []
		self.state = []
		self.mobile = []
		self.std_code = []
		self.phone = []
		self.fax = []
		self.residential_phone = []
		self.email = []
		self.site = []
		self.nature_of_business = []
		self.product_details = []
				
	def setUp(self):
		self.driver = webdriver.PhantomJS()
		self.myfile = open("ipcaonline_class.json","w")

	def firstStep(self, m=0):
		if m:
			self.driver.get('http://www.ipcaonline.com/members/members-list-'+m+'.html')
			time.sleep(4)
			self.secondStep()
		else:
			for self.m in self.alp:
				self.driver.get('http://www.ipcaonline.com/members/members-list-'+ self.m +'.html')
				time.sleep(4)
				self.secondStep()		

	def secondStep(self):
		self.grid = self.driver.find_elements_by_class_name('MsoNormalTable')
		try:
			self.scrape()
		except StaleElementReferenceException:
			time.sleep(3)
			self.scrape()
	def scrape(self):
		
		for i in self.grid:
			j = i.find_elements_by_tag_name('td')
			if(j):
				self.info['sno'] = self.l
				self.info['honary_memeber'] = j[1].text
				self.info['company_name'] = j[3].text
				self.info['contact_person'] = j[5].text
				self.info['reference_person'] = j[7].text
				self.info['address'] = j[9].text
				self.info['pcode'] = j[11].text
				self.info['state'] = j[13].text
				self.info['mobile'] = j[15].text
				self.info['std_code'] = j[17].text
				self.info['phone'] = j[19].text
				self.info['fax'] = j[21].text
				self.info['residential_phone'] = j[23].text
				self.info['email'] = j[25].text
				self.info['site'] = j[27].text
				self.info['nature_of_business'] = j[29].text
				self.info['product_details'] = j[31].text
				#print self.info
				self.doc.append(self.info.copy())
				self.l+=1

			self.honary_memeber.append(self.info['honary_memeber'])
			self.company_name.append(self.info['company_name'])
			self.contact_person.append(self.info['contact_person'])
			self.reference_person.append(self.info['reference_person'])
			self.address.append(self.info['address'])
			self.pcode.append(self.info['pcode'])
			self.state.append(self.info['state'])
			self.mobile.append(self.info['mobile'])
			self.std_code.append(self.info['std_code'])
			self.phone.append(self.info['phone'])
			self.fax.append(self.info['fax'])
			self.residential_phone.append(self.info['residential_phone'])
			self.email.append(self.info['email'])
			self.site.append(self.info['site'])
			self.nature_of_business.append(self.info['nature_of_business'])
			self.product_details.append(self.info['product_details'])
			print self.info['company_name']
		
	def desc(self):
		return self.doc

	def comp_name(self):
		return self.company_name

	def func_honary_memeber(self):
		return self.honary_memeber
	def func_contact_person(self):
		return self.contact_person
	def func_reference_person(self):
		return self.reference_person
	def func_address(self):
		return self.address
	def func_pcode(self):
		return self.pcode
	def func_state(self):
		return self.state
	def func_mobile(self):
		return self.mobile
	def func_std_code(self):
		return self.std_code
	def func_phone(self):
		return self.phone
	def func_fax(self):
		return self.fax
	def func_residential_phone(self):
		return self.residential_phone
	def func_email(self):
		return self.email
	def func_site(self):
		return self.site
	def func_nature_of_business(self):
		return self.nature_of_business
	def func_product_details(self):
		return self.product_details

	def tearDown(self):
		self.driver.quit()
		self.myfile.write(json.dumps(self.doc))

if __name__ == '__main__':

	newObj = testpy()
	newObj.setUp()
	newObj.firstStep() #for all letters scrape
	#newObj.firstStep('a') # or for a single letter scrape data
	for i, j in enumerate(newObj.comp_name()):
		print i, ': ', j
	newObj.tearDown()