import socket
import sys

HOST = 'localhost'
PORT = 5000

conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = (HOST, PORT)
conn.bind(server)

while True:
    msg, client = conn.recvfrom(int(sys.argv[1]))
    print(msg, client)
    # msg, client = conn.recvfrom(1024)
    msg = msg.decode()
    if(msg == 'ping'):
        msg = 'pong'
        conn.sendto(msg.encode(), client)
    else:
        conn.sendto(''.encode(), client)

conn.close()
