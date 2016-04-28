from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import csv
driver = webdriver.Firefox();
fs = open("totalpracto.csv","a+");#opens the csv file to which data is to be written to
reader = open("practo(LIST).txt","r");#This is the list of primary urls from which data is to be scrapped
info = {"Name":"","Phone":"","Location":"","Services":"","Specilaisations":"","Education":"","Experience":"","Membership":""};
for url in reader:#The main loop
    services = ""
    specialaities = ""
    Qualifications = ""
    Experiences = ""
    Memberships = ""
    driver.get(url);
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.TAG_NAME,"h1")))#waits for the presence of top most element indicated by h1
    info["Name"] = driver.find_element_by_tag_name("h1").text.encode('utf-8')#write to dictionary
    print info["Name"];#prinitng the name
    try:
        # driver.implicitly_wait(10);
        info['Location'] = driver.find_element_by_class_name("clinic-address").text.encode('utf-8')
        info["Location"] = info["Location"].replace(",","-");
        info["Location"] = info["Location"].replace("\n"," ");#changing , to - to prevent column delimiter
    except NoSuchElementException:
        info['Location'] = "No adress given"#If no adress given
        e = driver.find_element_by_class_name("book-toggle");#
    e.click();
    try:
        driver.find_element_by_class_name("Phone");
        info['Phone']=driver.find_element_by_class_name("Phone").text.encode('utf-8');#picking the phone no.
    except NoSuchElementException:
        info["Phone"] = "N/A"
    try:
        e = driver.find_element_by_id("moreServices");
        e.click();
        facility = driver.find_elements_by_class_name("service-cell");
        for s in facility:
            services = services + s.text.encode('utf-8') + "-";
        info['Services'] = services
    except NoSuchElementException:
        facility = driver.find_elements_by_class_name("service-cell");
        for s in facility:
            services = services + s.text.encode('utf-8') + "-";
        info['Services'] = services
    try:
        driver.find_element_by_id("moreSpecialties").click();
        facility = driver.find_elements_by_class_name("specialty-row");
        for s in facility:
            specialaities = specialaities + s.text.encode('utf-8') + "-"
        info['Specialisations']= specialaities;
    except NoSuchElementException:
        facility = driver.find_elements_by_class_name("specialty-row");
        for s in facility:
            specialaities = specialaities + s.text.encode('utf-8') + "-"
        info['Specialisations']= specialaities;
    try:
        driver.find_element_by_id("moreQualifications").click();
        facility = driver.find_elements_by_class_name("qualification-row");
        for s in facility:
            Qualifications = Qualifications + s.text.encode('utf-8') + "-"
        info["Education"] = Qualifications;
        info["Education"] = info["Education"].replace(",","-");
    except NoSuchElementException:
        facility = driver.find_elements_by_class_name("qualification-row");
        for s in facility:
            Qualifications = Qualifications + s.text.encode('utf-8') + "-"
        info["Education"] = Qualifications;
        info["Education"] = info["Education"].replace(",","-");
    try:
        driver.find_element_by_id("moreOrganizations").click();
        facility = driver.find_elements_by_class_name("exp-details");
        for s in facility:
            Experiences = Experiences + s.text.encode('utf-8') + "-"
        info["Experience"] = Experiences;
        info["Experience"] = info["Experience"].replace(",","-");
    except NoSuchElementException:
        facility = driver.find_elements_by_class_name("exp-details");
        for s in facility:
            Experiences = Experiences + s.text.encode('utf-8') + "-"
        info["Experience"] = Experiences;
        info["Experience"] = info["Experience"].replace(",","-");
    try:
        facility = driver.find_elements_by_class_name("membership-row");
        for s in facility:
            Memberships = Memberships + s.text.encode('utf-8') + "-"#Memeberships array to which
        info["Membership"] = Memberships;
    except NoSuchElementException:
        fs.write(info["Name"] + ",");
        fs.write(info["Location"] + ",");
        fs.write(info["Phone"] + ", ");
        fs.write(info["Services"] + ",");
        fs.write(info["Education"] + ",");
        fs.write(info["Experience"] + ",");
        fs.write(info["Membership"] + "," + "\n");
