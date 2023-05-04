from socket import *
import threading
import sys


FLAG = False  # это переменная флага для проверки завершения работы

# функция для получения сообщения от клиента
def send_to_server(clsock):
    global FLAG
    while True:
        if FLAG == True:
            break
        send_msg = input('')
        clsock.sendall(send_msg.encode())

# функция для получения сообщения от сервера
def recv_from_server(clsock):
    global FLAG
    while True:
        data = clsock.recv(1024).decode()
        if data == 'q':
            print('Замыкающее соединение')
            FLAG = True
            break
        print('Сервер: ' + data)

# это основная функция
def main():
    threads = []
    # TODO (1) - определите имя хоста, это будет IP-адрес или "localhost" 
    HOST = 'localhost'  # Имя хоста или IP-адрес сервера
    # TODO (2) - определите номер ПОРТА (1 строка) (Google, какой должна быть допустимая точка
    PORT = 6789        # Порт, используемый сервером

    # Создайте TCP-клиентский сокет
    #(AF_INET используется для протоколов IPv4)
    #(SOCK_STREAM используется для TCP)
    # TODO (3) - СОЗДАЙТЕ сокет для TCP-соединения IPv4 (1 строка)
    clientSocket = socket(AF_INET, SOCK_STREAM)

    # запрос на подключение отправляется на сервер, определенный хостом и ПОРТОМ
    # TODO (4) - запросить подключение к серверу (1 строка)
    clientSocket.connect((HOST, PORT))
    print('Клиент подключен к серверу чата!\n')



    # вызовите функцию для отправки сообщения на сервер
    #send_to_server(clientSocket)
    t_send = threading.Thread(target=send_to_server, args=(clientSocket,))
    # вызовите функцию для получения сообщений сервером
    #recv_from_server(clientSocket)
    t_rcv = threading.Thread(target=recv_from_server, args=(clientSocket,))
    threads.append(t_send)
    threads.append(t_rcv)
    t_send.start()
    t_rcv.start()

    t_send.join()
    t_rcv.join()

    print('выходящий')
    sys.exit()

# Здесь начинается программа
if __name__ == '__main__':
    main()


