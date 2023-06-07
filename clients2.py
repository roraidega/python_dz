import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((socket.gethostname(), 55555))

path_message=input('Введите название файла')

path_file = '/home/renata/Рабочий стол'+path_message

with open(path_file, "r") as f:
    text_file = f.read()
    sock.send(text_file.encode())
data = sock.recv(1024).decode()
print(data)