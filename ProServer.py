import socket
from _thread import start_new_thread


def threaded(c):
    global connections
    while True:
        try:
            data = c.recv(2048)
        except:
            break
        if not data:
            for i in range(len(connections)):
                if str(connections[i]) == str(c):
                    connections.pop(i)
            print('Bye')
            break
        data = data.decode().split('//')
        if 'update' != data[1]:
            try:
                commit = open(data[0] + '.txt', 'a+')
                commit.write(data[1] + '\n')
                commit.close()
            except FileNotFoundError:
                commit = open(data[0] + '.txt', 'w')
                commit.write(data[1] + '\n')
                commit.close()
        allch = open(data[0] + '.txt', 'r')
        all_chat = allch.read()
        allch.close()
        c.send(str('\nstart\n' + all_chat + 'end\n').encode())
    for i in range(len(connections)):
        if str(connections[i]) == str(c):
            connections.pop(i)
    print('Bye')
    c.close()


def wait_input():
    while True:
        server_mes = 'Ureshipan:  ' + input()
        if server_mes == 'Ureshipan:  up':
            allch = open('log.txt', 'r')
            all_chat = allch.read()
            allch.close()
            print(all_chat)
        else:
            commit = open('log.txt', 'a+')
            commit.write(server_mes + '\n')
            commit.close()


host = "0.0.0.0"
port = 27735
connections = []

start_new_thread(wait_input, ())
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print('Хостинг')
s.bind((host, port))
print('Ожидание')
s.listen(5)
while True:
    sock, addr = s.accept()
    connections.append(sock)
    print('Connected to :', addr[0], ':', addr[1])
    start_new_thread(threaded, (sock,))
