"""
Задание 1
Напишите функцию, которая возвращает название валюты (поле ‘Name’) с максимальным значением курса
с помощью сервиса https://www.cbr-xml-daily.ru/daily_json.js
"""
import requests


def my_func():
    res = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
    result = res.json()
    print(max([(el["Name"], el["Value"]) for el in result["Valute"].values()], key=lambda x: x[1]))


"""
Задание 2
Добавьте в класс Rate параметр diff (со значениями True или False), который в случае значения True в методах курсов
валют (eur, usd и т.д.) будет возвращать не курс валюты, а изменение по сравнению в прошлым значением. 
Считайте, self.diff будет принимать значение True только при возврате значения курса. 
При отображении всей информации о валюте он не используется.
"""


class Rate:
    def __init__(self):
        self.diff = False

    def get_rates(self):
        res = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
        return res.json()

    def usd(self):
        current = self.get_rates()["Valute"]["USD"]["Value"]
        previous = self.get_rates()["Valute"]["USD"]["Previous"]
        if self.diff:
            return current - previous
        return current

    def eur(self):
        current = self.get_rates()["Valute"]["EUR"]["Value"]
        previous = self.get_rates()["Valute"]["EUR"]["Previous"]
        if self.diff:
            return current - previous
        return current


rate = Rate()
print(rate.usd())
