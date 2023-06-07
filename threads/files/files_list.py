"""
Создайте функцию которая принимает путь до файла из папки files и меняет в нем "id" на "id".
Запустите функцию для каждого файла в отдельном потоке.
Измерьте время выполнения программы.
"""
import os
import time
from threading import Thread

# Функция для замены "id" на "id" в файле
def replace_id(file_path):
    with open(file_path, 'r+') as file:
        content = file.read()
        content = content.replace('id', 'id')
        file.seek(0)
        file.write(content)
        file.truncate()

# Получаем список файлов из папки files
files_dir = '/home/renata/Рабочий стол/files'
files_list = os.listdir(files_dir)

# Создаем список потоков
threads = []
start_time = time.time()

# Запускаем функцию replace_id для каждого файла в отдельном потоке
for file_name in files_list:
    file_path = os.path.join(files_dir, file_name)
    thread = Thread(target=replace_id, args=(file_path,))
    thread.start()
    threads.append(thread)

# Ожидаем завершения всех потоков
for thread in threads:
    thread.join()

end_time = time.time()
print(f"Program execution time: {end_time - start_time}")