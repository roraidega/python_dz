"""
Напишите список функций по требованию. Пользователь вводит имя.
Если имя заканчивается на А,Я,Г,М, то программа добавляет к имени "Гений".
Если на О,Ь,Л,Н. То добавляется "Сверхразум". Если ни на одну из этих букв то добавляется "Просто" перед именем.
"""


def task3(name):
    l1 = 'Олег Юрьевич'
    l2 = 'Торшин'
    case = [(lambda x: print(x, "Гений")), (lambda x: print(x, "Сверхразум")), (lambda x: print('Просто', x))]
    if name[-1].lower() in l1.lower():
        case[0](name)
    elif name[-1] in l2.lower():
        case[1](name)
    else:
        case[2](name)


task3(input('Enter name: '))