from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from datetime import datetime
import urllib.request
import json


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://komikindo.co/jojo-no-kimyou-na-bouken-jojorion-official-colored-chapter-1/")

manga = []
i = 1

now = datetime.now()
waktu = now.strftime("%d %B %Y %H:%M:%S")

while i <= 150:   
    for parrent in driver.find_elements_by_tag_name("p"):
        print(parrent.text.split("\n"))
        for img in parrent.find_elements_by_tag_name("img"):
            print(img.get_attribute("src")) 
            urllib.request.urlretrieve(img.get_attribute("src"), str(i)+".png")
            i = i+1
            manga.append({
                "Image": img.get_attribute("src"),
                "Waktu_scrapping":waktu
            })

    try:
        driver.find_element_by_class_name("desc").find_element_by_partial_link_text("Next").click()
    except NoSuchElementException as e:
        break

hasil_scraping = open("hasilscraping_jojo.json", "w")
json.dump(manga, hasil_scraping, indent = 6)
hasil_scraping.close()
driver.quit()
