"""напишите программу-вирус которая переименовывает папки c четными номерами в ранее созданной папке target,
новые имена придумайте самостоятельно.
"""

import os

list_1 = (os.listdir(r"C:\Users\Рената\OneDrive\Рабочий стол\Бабчёнок Олег\target"))

for i in list_1:
    if int(i) % 2 == 0:
    os.rename(fr"C:\Users\Рената\OneDrive\Рабочий стол\Бабчёнок Олег\target\{i}", fr"C:\Users\Рената\OneDrive\Рабочий стол\Бабчёнок Олег\target\{i}")