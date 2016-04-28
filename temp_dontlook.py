from selenium import webdriver
driver = webdriver.Firefox();
driver.get("https://www.google.co.in");
print driver.find_element_by_id("lst-ib").get_attribute('type')
driver.quit();
