import socket

HOST = 'localhost'
PORT = 1025 

conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = (HOST, PORT)
conn.settimeout(2)
ip = input('IP: ')

while True:
    conn.sendto (ip.encode(), server)
    try:
        ip, _ = conn.recvfrom(1024)
        print(ip.decode())
    except:
        pass
    ip = input('IP: ')

conn.close()
