import os
import socket
import struct
def send_file(sck: socket.socket, filename):
    # Получение размера файла.
    filesize = os.path.getsize(filename)
    # В первую очередь сообщим серверу, 
    # сколько байт будет отправлено.
    sck.send(("file$"+filename).encode())
    # sck.send(filename.encode())
    sck.send(struct.pack("<Q", filesize))
    # Отправка файла блоками по 1024 байта.
    with open(filename, "rb") as f:
        while read_bytes := f.read(1024):
            sck.send(read_bytes)
with socket.create_connection(("localhost", 6190)) as conn:
    print("Подключение к серверу.")
    print("Передача файла...")
    send_file(conn, "image.png")
    print("Отправлено.")
print("Соединение закрыто.")