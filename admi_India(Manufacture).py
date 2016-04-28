from selenium import webdriver

driver = webdriver.PhantomJS()
lists = []
info = {"Details": "" ,"Position":"" }
target = open("admi_India.csv" , "w+")
url = "http://www.admi-india.org/admi_member_list_manufacturers.html"
driver.get(url)
positions = driver.find_elements_by_xpath("//table[@class = 'paraLEFTnospTABLE']//tr[@bgcolor = '#FFFFFF']//td[2]");
details = driver.find_elements_by_xpath("//table[@class = 'paraLEFTnospTABLE']//tr[@bgcolor = '#FFFFFF']//td[1]");
for detail,position in zip(positions,details):
    info["Details"] = detail.text.encode('utf-8')
    info["Position"]= position.text.encode('utf-8')
    info["Details"] = info["Details"].replace("\n"," ")
    info["Position"] = info["Position"].replace("\n","\t")
    info["Position"] = info["Position"].replace(",","-")
    target.write(info["Details"] + ",")
    target.write(info["Position"] + "\n")
driver.quit();
