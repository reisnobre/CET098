import socket
import sys

HOST = 'localhost'
PORT = 5000 

conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = (HOST, PORT)
conn.settimeout(2)

def communicate():
    msg = input('Message: ')
    conn.sendto(msg.encode(), server)
    try: 
        msg, _ = conn.recvfrom(int(sys.argv[1]))
        print(msg.decode())
    except:
        print('Request Timeout')

def main():    
    if(sys.argv[2] == 'code'):
        while True: communicate()
    else:
        for i in range(int(sys.argv[2])):
            communicate()

    conn.close()


if __name__ == '__main__':
    main()
