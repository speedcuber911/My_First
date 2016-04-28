from selenium import webdriver
driver = webdriver.PhantomJS()
lists = []
info = {"Details": "" ,"Position":"" }#dictionary for storing the name and designation of Director(equivalent) , Details include email,phone ,adress
target = open("admi_India(Distributor).csv" , "w+")
url = "http://www.admi-india.org/admi_member_list_distributors.html"
driver.get(url)#open the url to be scraped
positions = driver.find_elements_by_xpath("//table[@class = 'paraLEFTnospTABLE']//tr[@bgcolor = '#FFFFFF']//td[2]");#accessing second column of the table
details = driver.find_elements_by_xpath("//table[@class = 'paraLEFTnospTABLE']//tr[@bgcolor = '#FFFFFF']//td[1]");#accessing first column of the table
for detail,position in zip(positions,details):
    info["Details"] = detail.text.encode('utf-8')#Encoding from unicode and storing in dictionary
    info["Position"]= position.text.encode('utf-8')
    info["Details"] = info["Details"].replace("\n"," ")#replacing line breaks with soace
    info["Position"] = info["Position"].replace("\n","\t")#reolacing line breaks with tabs
    info["Position"] = info["Position"].replace(",","-")#replacing commas with dashes
    target.write(info["Details"] + ",")#writing as columns of excel file
    target.write(info["Position"] + "\n")
driver.quit();
