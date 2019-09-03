import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = ("127.0.0.1", 12349)
sock.bind(addr)

sock.listen(5)

print('This is the Server')

while True:
    (connectedSock, clientAddress) = sock.accept()
    try:
        msg = connectedSock.recv(1024).decode()
    except:
        connectedSock.close()        
    message = "The band " + msg + " Sucks"

    connectedSock.sendall(message.encode())
    



