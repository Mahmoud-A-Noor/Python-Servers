from socket import AF_INET,SOCK_STREAM,socket

sobj = socket(AF_INET,SOCK_STREAM)
sobj.bind(('127.0.0.1',12345))
sobj.listen(1)

client , addr = sobj.accept()
print("the ip is connected to server ",addr)

while(True):
    
    message = input()
    if(message == "exit"):
        client.close()
        break
    else:
        client.send(message.encode())
    
    
