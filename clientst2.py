import socket

HOST= socket.gethostbyname(socket.gethostname())
PORT=9090

socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST,PORT))
socket.send("hello world now".encode('utf-8'))
print(socket.recv(1024))
