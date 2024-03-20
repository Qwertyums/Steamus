#Рабочий парсер v0
from bs4 import BeautifulSoup
import requests
from time import sleep

list = []
url = "https://wiki.cs.money/ru/cases"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0"}

responce = requests.get(url, headers=headers)
soup = BeautifulSoup(responce.text, "lxml")
data = soup.find_all("div", class_ ="kxmatkcipwonxvwweiqqdoumxg")
for i in data:
    sleep(1)
    name = i.find("div", class_="fncfqbivscnlbuqjlutbztsinz pnajptgpdtumbbliiuwzldaynb").text.replace("Копировать", "")
    price = i.find("div", class_="mrjvncygbzujwvgxbpfjowvujl").text
    list.append([name, price])
