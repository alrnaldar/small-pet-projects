from bs4 import BeautifulSoup
import requests
page = 1
total_results = 0
link = "https://auto.drom.ru/lexus/all/"
while True:
    response = requests.get(link)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text,"html.parser")
        car_title = soup.find_all("div", class_="css-l1wt7n e3f4v4l2")
        price = soup.find_all("span", class_="css-46itwz e162wx9x0")
        price_quality = soup.find_all("div", class_="css-11m58oj evjskuu0")
        total_results += len(car_title)
        car_link = soup.find_all("a",class_="css-xb5nz8 e1huvdhj1")

        for car_title_text, price_text,car_link_text,price_quality_text in zip(car_title,price,car_link,price_quality):
            print(car_title_text.text, "  |||   ", price_text.text,"  |||   ",price_quality_text.text, "  ||| ", car_link_text.get("href"))
        next_page = soup.find("a",class_='css-4gbnjj e24vrp30')
        if next_page:
            link = next_page.get("href")
        else: 
            print("no more pages")
    else:
        print("error")
