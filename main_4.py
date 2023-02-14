""" напишите программу которая создает папку task4 и записывает текст "я выполнил задание" в файл answer.txt
"""
import os

os.mkdir(r"C:\Users\Рената\OneDrive\Рабочий стол\Бабчёнок Олег\task_4")
os.chdir(r"C:\Users\Рената\OneDrive\Рабочий стол\Бабчёнок Олег\task_4")
text_file = open('answer.txt', 'w')
text_file.write('Я выполнила задания')