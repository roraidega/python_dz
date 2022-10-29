"""
Функция sorted принимает в качестве дополнительного параметра key(Можете почитать документацию).
С помощью lambda-функции отсортируйте этот список словарей по именам
"""


grades = [{'name': 'Renata', 'final': 95}, {'name': 'Lera', 'final': 92}, {'name': 'Ann', 'final': 98}]
print(sorted(grades, key=lambda x: x['name']))