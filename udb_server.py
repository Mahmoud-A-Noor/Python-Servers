from socket import socket,AF_INET , SOCK_DGRAM

sobj = socket(AF_INET,SOCK_DGRAM)


ip = '127.0.0.1'
port = 20000

sobj.bind((ip,port))

while True:
    msg = sobj.recvfrom(2048)
    print(msg)
    