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
    data_dict = json.dumps(data_ak, ensure_ascii=False, indent=2)
    with open('ak-47.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_m4a4, ensure_ascii=False, indent=2)
    with open('m4a4.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_m4a1s, ensure_ascii=False, indent=2)
    with open('m4a1-s.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_aug, ensure_ascii=False, indent=2)
    with open('aug.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_sg553, ensure_ascii=False, indent=2)
    with open('sg-553.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_galil, ensure_ascii=False, indent=2)
    with open('galil.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_famas, ensure_ascii=False, indent=2)
    with open('famas.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_awp, ensure_ascii=False, indent=2)
    with open('awp.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_ssg08, ensure_ascii=False, indent=2)
    with open('ssg-08.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_scar, ensure_ascii=False, indent=2)
    with open('scar-20.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_g3sg1, ensure_ascii=False, indent=2)
    with open('g3sg1.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_sawed, ensure_ascii=False, indent=2)
    with open('sawed-off.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_mag7, ensure_ascii=False, indent=2)
    with open('mag-7.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_nova, ensure_ascii=False, indent=2)
    with open('nova.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_xm, ensure_ascii=False, indent=2)
    with open('xm1014.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_negev, ensure_ascii=False, indent=2)
    with open('negev.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_m249, ensure_ascii=False, indent=2)
    with open('m249.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_p90, ensure_ascii=False, indent=2)
    with open('p90.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_ump45, ensure_ascii=False, indent=2)
    with open('ump45.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_mac10, ensure_ascii=False, indent=2)
    with open('mac-10.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_mp7, ensure_ascii=False, indent=2)
    with open('mp7.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_mp9, ensure_ascii=False, indent=2)
    with open('mp9.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_mp5sd, ensure_ascii=False, indent=2)
    with open('mp5-sd.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_bizon, ensure_ascii=False, indent=2)
    with open('pp-bizon.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_usp, ensure_ascii=False, indent=2)
    with open('usp-s.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_glock18, ensure_ascii=False, indent=2)
    with open('glock18.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_deagle, ensure_ascii=False, indent=2)
    with open('deagle.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_p250, ensure_ascii=False, indent=2)
    with open('p250.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_fiveseven, ensure_ascii=False, indent=2)
    with open('five-seven.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_cz75, ensure_ascii=False, indent=2)
    with open('cz75-auto.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_p2000, ensure_ascii=False, indent=2)
    with open('p2000.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_tec9, ensure_ascii=False, indent=2)
    with open('tec9.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_revolver, ensure_ascii=False, indent=2)
    with open('revolver.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_berettas, ensure_ascii=False, indent=2)
    with open('dual-berettas.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_kukri, ensure_ascii=False, indent=2)
    with open('kukri.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_karambit, ensure_ascii=False, indent=2)
    with open('karambit.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_m9bayonet, ensure_ascii=False, indent=2)
    with open('m9-bayonet.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_butterfly, ensure_ascii=False, indent=2)
    with open('butterfly-knife.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_talon, ensure_ascii=False, indent=2)
    with open('talon-knife.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_skeleton, ensure_ascii=False, indent=2)
    with open('skeleton-knfe.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_classic, ensure_ascii=False, indent=2)
    with open('classic-knife.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_bayonet, ensure_ascii=False, indent=2)
    with open('bayonet.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_stiletto, ensure_ascii=False, indent=2)
    with open('stiletto-knife.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_ursus, ensure_ascii=False, indent=2)
    with open('ursus.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_paracord, ensure_ascii=False, indent=2)
    with open('paracord.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_nomad, ensure_ascii=False, indent=2)
    with open('nomad.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_survival, ensure_ascii=False, indent=2)
    with open('survival.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_huntsman, ensure_ascii=False, indent=2)
    with open('huntsman.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_flip, ensure_ascii=False, indent=2)
    with open('flip-knife.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_bowie, ensure_ascii=False, indent=2)
    with open('bowie.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_falchion, ensure_ascii=False, indent=2)
    with open('falchion.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_gut, ensure_ascii=False, indent=2)
    with open('gut-knife.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_navaja, ensure_ascii=False, indent=2)
    with open('navaja.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_shadow_daggers, ensure_ascii=False, indent=2)
    with open('shadow-daggers.json', 'w') as file:
        json.dump(data_dict, file)

def cases_parser(headers):
    local_url = "https://wiki.cs.money/ru/cases"
    responce = requests.get(local_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml")
    data = soup.find_all("div", class_="kxmatkcipwonxvwweiqqdoumxg")
    list_item = []
    for i in data:
        sleep(0.4)
        price = i.find("div", class_="ribvzntfjepldppjrgkwabviqq")
        name = i.find("div", class_="szvsuisjrrqalciyqqzoxoaubw").text
        list_item.append((name, price))
    data_cases = dict(list_item)
    data_dict = json.dumps(data_cases, ensure_ascii=False, indent=2)
    with open('cases.json', 'w') as file:
        json.dump(data_dict, file)

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
    data_dict = json.dumps(data_gloves, ensure_ascii=False, indent=2)
    with open('gloves.json', 'w') as file:
        json.dump(data_dict, file)
