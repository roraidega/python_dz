"""
Реализовать чат,
который позволит обмениваться сообщениями только между клиентом и сервером.
Клиент должен получать сообщения сервера в том числе. Сигналом окончания связи служит слово "Пока".
"""

import socket

# создаем сокет для подключения к серверу
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# привязываем сокет к адресу и порту
sock.bind(("localhost", 55000))

# начинаем прослушивание подключений, максимальное количество клиентов - 10
sock.listen(10)

# инициализируем переменную для хранения полученных данных
data = ''

# ждем подключения клиента и выводим информацию о подключении
conn, addr = sock.accept()
print(f"Подключен: {addr}")

# цикл обмена сообщениями
while data != "пока":
    # принимаем данные от клиента и декодируем их
    data = conn.recv(1024).decode()

    # выводим полученные данные на экран
    print(str(data))

    # запрашиваем новые данные для отправки клиенту
    requests = input("Введите сообщение: ")

    # отправляем запрошенные данные клиенту, предварительно закодировав их
    conn.send(bytes(requests, encoding="UTF-8"))

    # переводим запрос и полученные данные в нижний регистр для удобства сравнения
    requests.lower()
    data.lower()

    # проверяем, не является ли запрос или полученные данные сигналом окончания связи
    if requests == "пока" or data == "пока":
        break
    else:
        continue

# закрываем соединение с клиентом
conn.close()