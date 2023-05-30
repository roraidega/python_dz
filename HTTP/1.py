"""
Изучите API сервиса cataas.com: https://cataas.com/#/
Реализуйте функции которые сохраняют:
2 картинки случайных котиков
2 картинки в оригинальном размере
2 пиксельных картинки
PS: Картинки пишутся как обычный файл открытый на запись в бинарном режиме
"""
import os
import requests


os.mkdir("cats")
os.chdir(r"cats/")


for i in range(1115):

    r = requests.get("https://cataas.com/cat")

    with open(f"Cat{i}.jpg", "wb") as f:
        f.write(r.content)

    if i % 100 == 0:
        print(f"Downloaded {i} images")