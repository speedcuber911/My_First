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
		self.x = 0
		self.box = []
		self.rows = []
		self.company_name = []
		self.address = []
		self.mobile = []
		self.landline = []
		self.email = []
		self.website = []
		self.deals_in = []
		self.doc = []
		self.alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'L', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

	def setUp(self):
		self.driver = webdriver.PhantomJS()
		self.myfile = open("ssia_class.json","w")

	def firstStep(self, m='', x=0):
		if m:
				for self.x in range(0, 121, 30): 
					self.driver.get('http://www.ssia.co.in/members-'+ m +'-'+str(self.x)+'.html')
					self.secondStep()
		else:
			for self.m in self.alp:
					for self.x in range(0, 121, 30): 
						self.driver.get('http://www.ssia.co.in/members-'+ self.m +'-'+str(self.x)+'.html')
						self.secondStep()

	def secondStep(self):
		self.box = self.driver.find_elements_by_class_name('address')
		self.scrape()
						
	def scrape(self):

			for i in self.box:
				self.info = {'Address:':'', 'Mobile No:':'', 'LandLine No:':'', 'Email ID:': '', 'Website:': '', 'Deals in :': ''}
				try:
					h5 = i.find_elements_by_tag_name('h5')
					p = i.find_elements_by_tag_name('p')
					self.info['company_name'] = i.find_element_by_tag_name('h4').text
					self.info['sno'] = self.l
					for v in range(len(p)):	
						self.info[h5[v].text] = p[v].text
					print self.info
					self.doc.append(self.info.copy())
					self.l+=1
					self.company_name.append(self.info['company_name'])
					self.address.append(self.info['Address:'])
					self.mobile.append(self.info['Mobile No:'])
					self.landline.append(self.info['LandLine No:'])
					self.email.append(self.info['Email ID:'])
					self.website.append(self.info['Website:'])
					self.deals_in.append(self.info['Deals in :'])
			
					
				except NoSuchElementException:
					self.x = 1000	
					return
	
	def desc(self):
		return self.doc

	def comp_name(self):
		return self.company_name
	def func_address(self):
		return self.address
	def func_mobile(self):
		return self.mobile
	def func_landline(self):
		return self.landline
	def func_email(self):
		return self.email
	def func_website(self):
		return self.website
	def func_deals_in(self):
		return self.deals_in

	def tearDown(self):
		self.driver.quit()
		self.myfile.write(json.dumps(self.doc))

if __name__ == '__main__':

	newObj = testpy()
	newObj.setUp()
	newObj.firstStep() #for all pages scrape
	#newObj.secondStep('a') # or for a single page scrape data
	for i, j in enumerate(newObj.comp_name()):
		print i, ': ', j
	newObj.tearDown()