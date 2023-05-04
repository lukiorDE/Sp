# Импорт модуля сокета
from socket import *
import threading
import sys # Для того, чтобы завершить работу программы

FLAG = False  # это переменная флага для проверки завершения работы

# функция для получения сообщения от клиента
def recv_from_client(conn):
    global FLAG
    try:
        # Получает сообщение с запросом от клиента
        while True:
            if FLAG == True:
                break
            message = conn.recv(1024).decode()
            # если 'q' получен от клиента, сервер завершает работу
            if message == 'q':
                conn.send('q'.encode())
                print('Закрытие соеденения')
                conn.close()
                FLAG = True
                break
            print('Клиент: ' + message)
    except:
        conn.close()


# функция для получения сообщения от клиента
def send_to_client(conn):
    global FLAG
    try:
        while True:
            if FLAG == True:
                break
            send_msg = input('')
            # сервер может предоставить "q" в качестве входных данных, если он хочет завершить работу
            if send_msg == 'q':
                conn.send('q'.encode())
                print('Закрытие соеденения')
                conn.close()
                FLAG = True
                break
            conn.send(send_msg.encode())
    except:
        conn.close()


# это основная функция
def main():
    threads = []
    global FLAG

    # TODO (1) - определите имя хоста, это будет IP-адрес или 'localhost' (1 строка)
    HOST = 'localhost'
    # TODO (2) - определите номер ПОРТА (1 строка) (Google, каким должен быть допустимый номер порта)
    # убедитесь, что порты не используются ни для какого другого приложения
    serverPort = 6789

    # Создайте сокет TCP-сервера
    #(AF_INET используется для протоколов IPv4)
    #(SOCK_STREAM используется для TCP)
    # TODO (3) - СОЗДАЙТЕ сокет для TCP-соединения IPv4 (1 строка)
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Привязать сокет к адресу сервера и порту сервера
    # TODO (4) - привязать сокет к порту хоста и сервера (1 строка)
    serverSocket.bind((HOST, serverPort))

    # Прослушивайте не более 1 соединения одновременно
    # TODO (5) - прослушивание и ожидание запроса от клиента (1 строка)
    serverSocket.listen(1)

    # Сервер должен быть запущен и прослушивать входящие подключения
    print('Сервер чата готов к подключению к чат-клиенту')
    # TODO (6) - принимать любой запрос на подключение от клиента (1 строка)
    connectionSocket, addr = serverSocket.accept()
    print('Сервер подключен к чат-клиенту\n')

    t_rcv = threading.Thread(target=recv_from_client, args=(connectionSocket,))
    t_send = threading.Thread(target=send_to_client, args=(connectionSocket,))
    # вызовите функцию для получения сообщений сервером
    #recv_from_server(clientSocket)
    threads.append(t_rcv)
    threads.append(t_send)
    t_rcv.start()
    t_send.start()

    t_rcv.join()
    t_send.join()


    # закрытие serversocket перед выходом
    print('выходящий')
    serverSocket.close()
    #Завершите работу программы после отправки соответствующих данных
    sys.exit()


# Здесь начинается программа
if __name__ == '__main__':
    main()