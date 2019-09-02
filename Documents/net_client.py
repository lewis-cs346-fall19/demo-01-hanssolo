import socket

print('This is the Client')

while True:

    sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    addr = ("127.0.0.1",12349)
    sock1.connect(addr)
    
    msg = raw_input("Favorite Band?: ")
    sock1.sendall(msg.encode())
    
    mesg = sock1.recv(1024).decode()
    print(mesg)
    sock1.close()
