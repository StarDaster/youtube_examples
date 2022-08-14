# генераторы для асинхронности
from select import select
from time import time
import socket


# простой генератор
def gen(s):
    for i in s:
        yield i


# g = gen("1234")
# print(next(g))


def gen_filename():
    while True:
        pattern = "file-{}.jpeg"
        t = int(time() * 1000)
        yield pattern.format(str(t))

        summa = 234 + 234
        print(summa)


def gen2(n):
    for i in range(n):
        yield i


# g1 = gen("Nikolai")
# g2 = gen2(10)
# tasks = [g1, g2]

# while tasks:
#     task = tasks.pop(0)
#
#     try:
#         i = next(task)
#         print(i)
#         tasks.append(task)
#     except StopIteration:
#         pass

# ключевая особенность генератора - сохранение своего состояния

# асинхронность по принципу round robin - выстраиваем всё в очередь


tasks = []

# ключом тут будет сокет, а значением - генератор
to_read = {}
to_write = {}


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("localhost", 5000))
    server_socket.listen()  # слушаем входящие соединения

    while True:
        yield "read", server_socket
        client_socket, addr = server_socket.accept()  # read
        print("Connection from", addr)
        tasks.append(client(client_socket))


def client(client_socket):
    while True:
        yield "read", client_socket
        request = client_socket.recv(4096)  # read

        if not request:
            break
        else:
            response = "Hello, World!\n".encode()
            yield "write", client_socket
            client_socket.send(response)  # write
        client_socket.close()


server()

# задачи:
# - какие сокеты готовы для чтения или записи и вызвать соответствующие методы
# - механизм для переключения между функциями


def event_loop():
    while any([tasks, to_read, to_write]):
        while not tasks:
            ready_to_read, ready_to_write, _ = select(to_read, to_write, [])

            for sock in ready_to_read:
                tasks.append(to_read.pop(sock))

            for sock in ready_to_write:
                tasks.append(to_write.pop(sock))

        try:
            task = tasks.pop(0)

            reason, sock = next(task)

            if reason == "read":
                to_read[sock] = task
            if reason == "write":
                to_read[sock] = task
        except StopIteration:
            print("Done")


tasks.append(server())
event_loop()