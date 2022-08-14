# асинхронность = кооперативная многозадачность. Речь идёт про 1 процесс и 1 поток.

# Типы задач: CPU / GPU и IO-bound

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("localhost", 5000))
server_socket.listen()  # слушаем входящие соединения

while True:
    print("Before .accept()")
    client_socket, addr = server_socket.accept()
    print("Connection from", addr)

    while True:
        print("Before .recv()")
        request = client_socket.recv(4096)

        if not request:
            break
        else:
            response = "Hello, World!\n".encode()
            client_socket.send(response)


# что важно понимать:
