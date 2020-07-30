import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((UDP_IP, UDP_PORT))

while True:
    host = input('IP: ')
    try:
        nh2 = socket.gethostbyaddr(host)
        print('Namehost 2: ', nh2)
    except:
        print('None')

    nh1 = socket.getfqdn(host)
    nh = socket.gethostbyname(host)
    print('Namehost: ', nh)
    print('Namehost 1: ', nh1)

