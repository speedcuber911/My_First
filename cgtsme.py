#scarp cgtsme.com
from selenium import webdriver
driver = webdriver.Firefox();
url = "https://www.cgtmse.in/List_Of_MLIs.aspx";
driver.get(url)
target = open("cgtsme.csv","w+")
data = driver.find_elements_by_tag_name("tr")
for rows in data:
    print rows.find_element_by_tag_name("td").text
driver.quit()
