import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import csv

### подключение 
chrome_options = Options()
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--disable-gpu")  
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://nylottery.ny.gov/")
time.sleep(5)
page_source = driver.page_source
soup = BeautifulSoup(page_source, "html.parser")
###

### take5
numbers_div = soup.find_all("div", class_="Win4Oval__Oval-sc-1h2ouqz-0 MultiResultsContainer__SmallerOval-sc-1n5wrs2-3 iXzysl dGNhLw")
take5_numb_list = []

for numbers in numbers_div:
    take5_numb_list.append(numbers.text)

print("Take5:","\n    evening: "," ".join(take5_numb_list[0:5]),"\n    midday :"," ".join(take5_numb_list[5:12]))
###

### Win4
win4_numbers_div = soup("div",class_="Win4Oval__Oval-sc-1h2ouqz-0 iXzysl")
win4_numb_list = []
for win4_numbers in win4_numbers_div:
    win4_numb_list.append(win4_numbers.text)
print("Win4:","\n    evening: "," ".join(win4_numb_list[0:4]),"\n    midday :"," ".join(win4_numb_list[4:8]))
###

### Numbers
numbers_numbers_div = soup("div", class_="Win4Oval__Oval-sc-1h2ouqz-0 iXzysl")
numbers_numb_list = []
for numbers_numbers in numbers_numbers_div:
    numbers_numb_list.append(numbers_numbers.text)
print("Numbers:","\n    evening: "," ".join(numbers_numb_list[0:3]),"\n    midday :"," ".join(numbers_numb_list[3:6]))
###

driver.quit()






