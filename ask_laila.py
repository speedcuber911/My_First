from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string
import time
info = {"Name":"","function":"","Phone":"","adress":"","email":""}
links =[]
link = ""
n = 1;
driver = webdriver.Firefox();
target = open("ask_laila.txt" , "r")
for url in iter(target):
    driver.get(url);
    try:
        driver.find_element_by_class_name("glyphicon-chevron-down").click()
    except NoSuchElementException:
        pass
    time.sleep(5)
    liste = driver.find_elements_by_xpath("/html/body/div[3]/div[1]/div[6]/ul/li")
    if len(liste) >= 3:
        for i in range(1,len(liste)-2):
            if i ==1:
                driver.get(url)
            else:
                link = string.replace(url ,"?" , str((i-1)*10))
                driver.get(link)

    for elem in liste:
        elem.click();
        links = driver.find_elements_by_link_text(str(n))
        for link in links:
            link.get_attribute("href")
            driver.get(link)
            n =  n + 1




























        page = url.replace("?" , str(n) + "?")
        listed = driver.find_elements_by_class_name("nos");
        print page
        driver.get(page)
        n  = n +  10
        cards = driver.find_elements_by_xpath("//a[contains(@href,'http://www.asklaila.com/listing/Delhi-NCR')]")
        for anchor in cards:
            a = anchor.get_attribute("href").encode('utf-8','unicode')
            if a[11:19] == "asklaila":
                print a
        n = n+10;
        datas = driver.find_elements_by_class_name("cardElement")
        for data in datas:
            print data
driver.quit()
