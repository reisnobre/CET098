import socket
import io

HOST = '127.0.0.1'
PORT = 9009 
CONN = (HOST, PORT)

ALLOWED_METHODS = ['GET', 'POST', 'PUT']

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.settimeout(2)
server.connect(CONN)

print('Server ready at {}:{}'.format(HOST, PORT))
print('Inform connection method and message as it follows ~> METHOD:MESSAGE\n')

try:
    while True:
        raw = input('')
        if (len(raw) > 3):
            method, message = raw.split(':')
            print(method, message)
        else:
            method = raw
        try:
            index = ALLOWED_METHODS.index(method)
            if index is 0:
                server.sendall('{}'.format(method).encode())
                print('response:\n', server.recv(1024).decode())
            elif index is 1:
                server.sendall('{}:{}'.format(method, message).encode())
        except ValueError as e:
            print('METHOD NOT ALLOWED')
finally:
    print('Closing Server at {}:{}'.format(HOST, PORT))
    server.close()
