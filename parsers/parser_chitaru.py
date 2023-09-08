from bs4 import BeautifulSoup
import requests

link = requests.get("https://www.chita.ru/text/")
soup = BeautifulSoup(link.content, "html.parser")
under_title = soup.find_all("div", class_="TdYOd")
title = soup.find_all("h2", class_="h9Jmx")
under_title_text_list = []

for div_element in under_title:
    tit = div_element.find_all("a")
    for name in tit:
        under_title_text_list.append(name.text)

for title_text, under_title_text in zip(title,under_title_text_list):
        print("\n\n", title_text.text, "      |||     ", under_title_text, "\n\n")
