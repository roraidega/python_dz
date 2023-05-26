import requests
from bs4 import BeautifulSoup
import json

url = 'https://music.yandex.ru/chart'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

chart = {}
counter = 1
for item in soup.find_all('div', class_='chart-track__name'):
    artist = item.find('a', class_='chart-track__artists').text.strip()
    track = item.find('a', class_='chart-track__title').text.strip()
    chart[counter] = (artist, track)
    counter += 1

with open('chart.json', 'w', encoding='utf-8') as file:
    json.dump(chart, file, ensure_ascii=False, indent=4)

print('Данные сохранены в файл chart.json')