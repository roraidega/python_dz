import os
import queue
import threading

# Функция для создания пути до файла и добавления его в очередь
def create_file_path(name, q):
    file_path = os.path.join('/home/renata/Рабочий стол/files', f"{name}.txt")
    q.put(file_path)

# Функция для создания файла по пути из очереди
def create_file(q):
    while not q.empty():
        file_path = q.get()  # получаем путь до файла из очереди
        with open(file_path, 'w') as file:
            file.write("Hello, world!")

# Создаем очередь и заполняем ее путями до файлов
q = queue.Queue()
with open('/home/renata/Рабочий стол/files/Names.txt', 'r') as file:
    names = file.read().splitlines()
for name in names:
    create_file_path(name, q)

# Создаем список потоков и запускаем их
threads = []
for i in range(5):
    thread = threading.Thread(target=create_file, args=(q,))
    thread.start()
    threads.append(thread)

# Ожидаем завершения всех потоков
for thread in threads:
    thread.join()

print("All files created!")