import socket

HOST = 'localhost'
PORT = 1025 

conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = (HOST, PORT)
conn.bind(server)

while True:
    msg, client = conn.recvfrom(1024)
    msg = socket.getfqdn(msg.decode())
    conn.sendto(msg.encode(), client)

conn.close()
