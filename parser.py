from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from time import sleep
import json


main_url = "https://wiki.cs.money"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0"}

def ak47_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/ak-47"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_ak = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\ak-47.json', 'w') as file:
        json.dump(data_ak, file, indent=4)

def m4a4_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/m4a4"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_m4a4 = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\m4a4.json', 'w') as file:
        json.dump(data_m4a4, file, indent=4)

def m4a1_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/m4a1-s"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_m4a1s = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\m4a1-s.json', 'w') as file:
        json.dump(data_m4a1s, file, indent=4)

def aug_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/aug"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_aug = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\aug.json', 'w') as file:
        json.dump(data_aug, file, indent=4)

def sg553_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/sg-553"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_sg553 = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\sg-553.json', 'w') as file:
        json.dump(data_sg553, file, indent=4)

def galil_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/galil-ar"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_galil = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\galil.json', 'w') as file:
        json.dump(data_galil, file, indent=4)

def famas_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/famas"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_famas = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\famas.json', 'w') as file:
        json.dump(data_famas, file, indent=4)

def awp_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/awp"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_awp = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\awp.json', 'w') as file:
        json.dump(data_awp, file, indent=4)

def ssg08_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/ssg-08"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_ssg08 = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\ssg-08.json', 'w') as file:
        json.dump(data_ssg08, file, indent=4)

def scar_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/scar-20"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_scar = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\scar-20.json', 'w') as file:
        json.dump(data_scar, file, indent=4)

def g3sg1_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/g3sg1"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_g3sg1 = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\g3sg1.json', 'w') as file:
        json.dump(data_g3sg1, file, indent=4)

def sawedoff_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/sawed-off"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_sawed = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\sawed-off.json', 'w') as file:
        json.dump(data_sawed, file, indent=4)

def mag7_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/mag-7"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_mag7 = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\mag-7.json', 'w') as file:
        json.dump(data_mag7, file, indent=4)

def nova_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/nova"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_nova = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\nova.json', 'w') as file:
        json.dump(data_nova, file, indent=4)

def xm1014_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/xm1014"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_xm = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\xm1014.json', 'w') as file:
        json.dump(data_xm, file, indent=4)

def negev_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/negev"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_negev = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\negev.json', 'w') as file:
        json.dump(data_negev, file, indent=4)

def m249_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/m249"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_m249 = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\m249.json', 'w') as file:
        json.dump(data_m249, file, indent=4)

def p90_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/p90"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_p90 = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\p90.json', 'w') as file:
        json.dump(data_p90, file, indent=4)

def ump45_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/ump-45"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_ump45 = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\ump45.json', 'w') as file:
        json.dump(data_ump45, file, indent=4)

def mac10_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/mac-10"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_mac10 = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\mac-10.json', 'w') as file:
        json.dump(data_mac10, file, indent=4)

def mp7_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/mp7"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_mp7 = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\mp7.json', 'w') as file:
        json.dump(data_mp7, file, indent=4)

def mp9_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/mp9"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_mp9 = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\mp9.json', 'w') as file:
        json.dump(data_mp9, file, indent=4)

def mp5sd_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/mp5-sd"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_mp5sd = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\mp5-sd.json', 'w') as file:
        json.dump(data_mp5sd, file, indent=4)

def ppbizon_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/pp-bizon"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_bizon = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\pp-bizon.json', 'w') as file:
        json.dump(data_bizon, file, indent=4)

def usp_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/usp-s"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_usp = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\usp-s.json', 'w') as file:
        json.dump(data_usp, file, indent=4)

def glock18_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/glock-18"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_glock18 = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\glock18.json', 'w') as file:
        json.dump(data_glock18, file, indent=4)

def deagle_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/desert-eagle"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_deagle = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\deagle.json', 'w') as file:
        json.dump(data_deagle, file, indent=4)

def p250_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/p250"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_p250 = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\p250.json', 'w') as file:
        json.dump(data_p250, file, indent=4)

def fiveseven_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/five-seven"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_fiveseven = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\five-seven.json', 'w') as file:
        json.dump(data_fiveseven, file, indent=4)

def cz75_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/cz75-auto"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_cz75 = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\cz75-auto.json', 'w') as file:
        json.dump(data_cz75, file, indent=4)

def p2000_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/p2000"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_p2000 = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\p2000.json', 'w') as file:
        json.dump(data_p2000, file, indent=4)

def tec9_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/tec-9"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_tec9 = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\tec9.json', 'w') as file:
        json.dump(data_tec9, file, indent=4)

def revolver_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/r8-revolver"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_revolver = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\revolver.json', 'w') as file:
        json.dump(data_revolver, file, indent=4)

def berettas_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/dual-berettas"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_berettas = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\dual-berettas.json', 'w') as file:
        json.dump(data_berettas, file, indent=4)

def kukri_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/kukri-knife"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_kukri = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\kukri.json', 'w') as file:
        json.dump(data_kukri, file, indent=4)

def karambit_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/karambit"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_karambit = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\karambit.json', 'w') as file:
        json.dump(data_karambit, file, indent=4)

def m9bayonet_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/m9-bayonet"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_m9bayonet = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\m9-bayonet.json', 'w') as file:
        json.dump(data_m9bayonet, file, indent=4)

def butterfly_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/butterfly-knife"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_butterfly = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\butterfly-knife.json', 'w') as file:
        json.dump(data_butterfly, file, indent=4)

def talon_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/talon-knife"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_talon = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\talon-knife.json', 'w') as file:
        json.dump(data_talon, file, indent=4)

def skeleton_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/skeleton-knife"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_skeleton = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\skeleton-knfe.json', 'w') as file:
        json.dump(data_skeleton, file, indent=4)

def classic_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/classic-knife"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_classic = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\classic-knife.json', 'w') as file:
        json.dump(data_classic, file, indent=4)

def bayonet_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/bayonet"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_bayonet = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\bayonet.json', 'w') as file:
        json.dump(data_bayonet, file, indent=4)

def stiletto_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/stiletto-knife"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_stiletto = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\stiletto-knife.json', 'w') as file:
        json.dump(data_stiletto, file, indent=4)

def ursus_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/ursus-knife"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_ursus = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\ursus.json', 'w') as file:
        json.dump(data_ursus, file, indent=4)

def paracord_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/paracord-knife"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_paracord = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\paracord.json', 'w') as file:
        json.dump(data_paracord, file, indent=4)

def nomad_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/nomad-knife"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_nomad = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\nomad.json', 'w') as file:
        json.dump(data_nomad, file, indent=4)

def survival_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/survival-knife"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_survival = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\survival.json', 'w') as file:
        json.dump(data_survival, file, indent=4)

def huntsman_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/huntsman-knife"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_huntsman = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\huntsman.json', 'w') as file:
        json.dump(data_huntsman, file, indent=4)

def flip_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/flip-knife"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_flip = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\flip-knife.json', 'w') as file:
        json.dump(data_flip, file, indent=4)

def bowie_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/bowie-knife"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_bowie = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\bowie.json', 'w') as file:
        json.dump(data_bowie, file, indent=4)

def falchion_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/falchion-knife"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_falchion = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\falchion.json', 'w') as file:
        json.dump(data_falchion, file, indent=4)

def gut_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/gut-knife"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_gut = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\gut-knife.json', 'w') as file:
        json.dump(data_gut, file, indent=4)

def navaja_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/navaja-knife"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_navaja = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\navaja.json', 'w') as file:
        json.dump(data_navaja, file, indent=4)

def shadowdaggers_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/weapons/shadow-daggers"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        if len(quality) == len(price):
            price[0] = price[0].text
            for g in range(1, len(price)):
                quality[g] = quality[g].text
                price[g] = price[g].text
                price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        else:
            price[0] = price[0].text
            price[len(price) // 2] = price[len(price) // 2].text
            for g in range(1,len(price)):
                if g == len(price) // 2:
                    dict_item[price[0]] = price_dict
                    price_dict = {}
                elif g < len(price) // 2:
                    quality[g] = quality[g].text
                    price[g] = price[g].text
                    price_dict[quality[g]] = price[g]
                else:
                    price[g] = price[g].text
                    price_dict[quality[g-(len(price)//2)]] = price[g]
            dict_item[price[len(price) // 2]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_shadow_daggers = dict(list_item)
    with open('D:\\PythonProject\\Steamus\\data_price\\shadow-daggers.json', 'w') as file:
        json.dump(data_shadow_daggers, file, indent=4)

def gloves_parser(url, headers):
    local_url = "https://wiki.cs.money/ru/gloves"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list = []
    list_nametag = []
    list_item = []
    for i in data:
        sleep(0.4)
        addit_url = i.find("a", class_="blzuifkxmlnzwzwpwjzrrtwcse")
        name = i.find("div", class_="zhqwubnajobxbgkzlnptmjmgwn").text
        list_nametag.append(name)
        list.append(url + addit_url["href"])
    k = 0
    for i in list:
        driver = webdriver.Chrome()
        driver.get(i)
        sleep(1)
        additional_soup = BeautifulSoup(driver.page_source, "lxml")
        name = list_nametag[k]
        quality = additional_soup.find_all("th", class_="uwvszmlahnnwcljdblhvydcsfx")
        price = additional_soup.find_all("td", class_="cbwkznqqznnkaacmmnkbomescp")
        price_dict = {}
        dict_item = {}
        price[0] = price[0].text
        for g in range(1, len(price)):
            quality[g] = quality[g].text
            price[g] = price[g].text
            price_dict[quality[g]] = price[g]
            dict_item[price[0]] = price_dict
        driver.close()
        driver.quit()
        list_item.append((name, dict_item))
        k += 1
    data_gloves = dict(list_item)
    with open('gloves.json', 'w') as file:
        json.dump(data_gloves, file, indent=4)
