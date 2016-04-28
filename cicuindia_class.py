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
		self.alp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
		self.l = 1
		self.pageno = []
		self.company_name = set()
		self.manufacture = set()
		self.name_designation_no = set()
		self.contact = set()
		self.data = []
		self.m = ''
	def setUp(self):
		self.driver = webdriver.PhantomJS()
		self.myfile = open("cicuindia_class.json","w")

	def firstStep(self, m=0):
		if m:
			self.driver.get('http://www.cicuindia.org/show_member_directory.php?s=0&ii=1&q='+ m)
			self.pageno.append(self.driver.find_elements_by_id('aa'))
		else:
			for self.m in self.alp:
				self.driver.get('http://www.cicuindia.org/show_member_directory.php?s=0&ii=1&q='+ self.m)
				self.pageno.append(self.driver.find_elements_by_id('aa'))
				self.pages()		

	def pages(self):
	 	alphabets = 0
		for page in range(0, len(self.pageno[alphabets])*20+1, 20):
			self.driver.get('http://www.cicuindia.org/show_member_directory.php?s='+str(page)+'&ii=1&q='+self.m)
			self.secondStep()
			alphabets += 1

	def secondStep(self):
		self.data = self.driver.find_elements_by_class_name('dir')
		self.scrape()

	def scrape(self):
		for i in self.data:
			j = i.find_elements_by_class_name('shortdes')
			if(j):
				self.info['company_name'] = i.find_element_by_class_name('heading1').text
				self.info['sno'] = self.l
				self.info['manufacture'] = j[0].text
				self.info['name_designation_no.'] = j[1].text
				self.info['contact'] = j[2].text

				self.company_name.add(self.info['company_name'])
				self.manufacture.add(self.info['manufacture'])
				self.name_designation_no.add(self.info['name_designation_no.'])
				self.contact.add(self.info['contact'])
				#print self.info
				self.l+=1
				self.doc.append(self.info.copy())
			else:
				print 'empty'	

	def desc(self):
		return self.doc

	def comp_name(self):
		return self.company_name

	def func_manufacture(self):
		return self.manufacture

	def func_name_designation_no(self):
		return self.name_designation_no

	def tearDown(self):
		self.driver.close()
		self.myfile.write(json.dumps(self.doc))

if __name__ == '__main__':

	newObj = testpy()
	newObj.setUp()
	newObj.firstStep() #for all letters scrape
	#newObj.firstStep('A') # or for a single letter scrape data
	newObj.pages()
	for i, j in enumerate(newObj.comp_name()):
		print i, ': ', j
	newObj.tearDown()