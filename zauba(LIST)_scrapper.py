from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#Importing all the required packages
driver = webdriver.PhantomJS()
target = open("total_zauba.txt","a+")#This is the file which stores the URL's of all compamies on Zauba
url = "https://www.zaubacorp.com/company-list/p-"
n = 0;
for i in range(31580,40001):#Zauba has 52,045 pages ecah having around 25 pages the loop limits represent pages we use to store URL's
    n = n+1
    url = "https://www.zaubacorp.com/company-list/p-"
    url = url + str(i) + "-company.html"
    driver.get(url)
    liste = driver.find_elements_by_xpath("//*[@id='table']//a")#Accessing the links of all companies on a particular page
    for l in liste:
        print l.text;
        target.write(l.get_attribute("href") + "\n");#Writing to the file
    print "Currently at page no." + str(i)
    if n ==95:
        driver.close()
        driver = webdriver.PhantomJS();
        n = 0
target.close();
