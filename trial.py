import string
from selenium import webdriver
urlext = []
n=0;
i=0;
a = ""
ext = open("ask_ext.txt","a+")
target = open("ask_laila.txt","r")
driver = webdriver.Firefox()
for line in target:
        n=n+1
        driver.get(line);
        liste = driver.find_elements_by_xpath("/html/body/div[3]/div[1]/div[6]/ul/li/a")
        print len(liste)

        cards = driver.find_elements_by_xpath("//a[contains(@href,'http://www.asklaila.com/listing/Delhi-NCR')]")#picks cards from the page
        for card in cards:
            i = i+1
            if i%2==0:
                a = card.get_attribute("href")
                a.encode('utf-8')
                if a[11:19] == "asklaila":
                    ext.write(a + "\n")
                    print a
        if n ==95:
            driver.close()
            driver = webdriver.PhantomJS();
            n = 0


"""    liste = driver.find_elements_by_xpath("/html/body/div[3]/div[1]/div[6]/ul/li")
    print len(liste)
    ext.write(str(len(liste)) +"/n")
    urlext.append(len(liste))"""

"""
for url in target:
    linker = url
    if int(urlext[i]) == 0
        driver.get(linker)
        cards = driver.find_elements_by_xpath("//a[contains(@href,'http://www.asklaila.com/listing/Delhi-NCR')]")
        for card in cards:
            card.click();
            #scrape data
    else:
        for n in range(1,int(urlext[i])-1):
            link = string.replace(linker , "?" , str((i-1)*10) + "?")
            driver.get(link)
            cards = driver.find_elements_by_xpath("//a[contains(@href,'http://www.asklaila.com/listing/Delhi-NCR')]")
            for card in cards:
                card.click();

                    #scrape data
"""
