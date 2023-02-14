""" напишите программу которая создает папку task4 и записывает текст "я выполнил задание" в файл answer.txt
"""

import os

os.mkdir(r"C:\Users\Рената\OneDrive\Рабочий стол\Бабчёнок Олег\target")
os.chdir(r"C:\Users\Рената\OneDrive\Рабочий стол\Бабчёнок Олег\target")

for i in range(1, 11):
    os.mkdir(f"{i}")