import socket
import signal
import sys

HOST = '127.0.0.1'
PORT = 9009 
CONN = (HOST, PORT)

ALLOWED_METHODS = ['GET', 'POST', 'PUT']

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(CONN)
server.listen(1)

print('Server ready at {}:{}'.format(HOST, PORT))

messages = []

def GET():
    print(messages)
    return '\n'.join(messages)

def POST(message):
    print('posting', message)
    messages.append(message)

def signal_handler(sig, frame):
    server.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

while True:
    print('Waiting for clients')
    client_socket, client_addr = server.accept()
    try:
        print('client_socket established with client: ', client_addr)
        while True:
            raw = client_socket.recv(1024).decode()
            print(raw)
            if (len(raw) > 3):
                method, message = raw.split(':')
            else:
                method = raw
            try:
                print(method, message)
                index = ALLOWED_METHODS.index(method)
                if index is 0:
                    client_socket.sendall(GET().encode())
                elif index is 1:
                    print(message)
                    POST(message)
            except ValueError as e:
                print('METHOD NOT ALLOWED')
                client_socket.close()
    finally:
        print('Closing Server at {}:{}'.format(HOST, PORT))
        server.close()

signal.pause()
