import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            for line in file:
                command = line.strip()
                if command:
                    print("Выполнение команды:", command)
    except FileNotFoundError:
        print("Файл не найден")
else:
    print("Вы не ввели имя файла")