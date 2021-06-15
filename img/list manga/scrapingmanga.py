from selenium import webdriver
import urllib.request
from selenium.common.exceptions import NoSuchElementException
import json

path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://myanimelist.net/topmanga.php")

mangalist = []

i = 1
while i<=100:
    for manga in driver.find_elements_by_class_name("ranking-list"):
        print(manga.text.split("\n"))
        for img in manga.find_elements_by_tag_name("img"):
            print(img.get_attribute("src"))
            urllib.request.urlretrieve(img.get_attribute("src"), str(i)+".png")
            i = i+1
            mangalist.append(
                {"Rank" : manga.text.split("\n")[0],
                 "Judul" : manga.text.split("\n")[1],
                 "Tahun Rilis" : manga.text.split("\n")[3]. split(" -")[0],
                 "Members" : manga.text.split("\n")[4],
                 "Rating" : manga.text.split("\n")[5].split()[0],
                 "Image" : img.get_attribute("src")
                 }
                )

    try:
        driver.find_element_by_class_name("pagination").find_element_by_partial_link_text("Next").click()
    except NoSuchElementException as e:
        break;
    
hasil_scraping = open("hasilscrapingmanga.json", "w")
json.dump(mangalist, hasil_scraping, indent = 6)
hasil_scraping.close()

driver.quit()
