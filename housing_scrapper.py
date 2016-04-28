from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
letsventure = {"Name" : "", "location" : "" , "Services" : "" , "Funding" : "" , "Website" : ""}
target = open("letsventure.csv" , "w+")
driver = webdriver.Firefox()
username = "akashbansal@gmail.com"
passw = "zoukzouk"
driver.get("https://letsventure.com/signin")
driver.find_element_by_id("email").send_keys(username);
driver.find_element_by_id("password").send_keys(passw , Keys.RETURN);
time.sleep(10)
driver.get("https://letsventure.com/startups")
time.sleep(5)
driver.get("https://letsventure.com/startups?tab=all&locations=Delhi, India&page=1")
tabs = driver.find_elements_by_xpath("//*[@id='searchFilter']/div[2]/ul/li")
for tab in tabs:
    tab.click()
    letsventure["Name"] = driver.find_element_by_tag_name("h3").text.encode('utf-8')
    letsventure["location"] = driver.find_element_by_class_name("media-body").text.encode('utf-8')
    letsventure["Services"] = driver.find_element_by_class_name("sector-icon").text.encode('utf-8')
    letsventure["Funding"] = "funding"
    letsventure["Website"] = driver.find_element_by_class_name("exec-brief-long-url").text.encode('utf-8')
    print letsventure["Name"]
    print letsventure["location"]
    print letsventure["Services"]
    print letsventure["Funding"]
    print letsventure["Website"]
    driver.get("https://letsventure.com/startups?tab=all&locations=Delhi, India&page=1")
