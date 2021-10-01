from socket import socket,AF_INET , SOCK_DGRAM

sobj = socket(AF_INET,SOCK_DGRAM)


ip = '127.0.0.1'
port = 20000

msg = "Hello World"
sobj.sendto(msg.encode(),(ip,port))