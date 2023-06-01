import socket

HOST= socket.gethostbyname(socket.gethostname())
PORT=9090
ADDR= (HOST,PORT)
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()

while True:
   print (f"[LISTENING] to {HOST}")
   communication_socket,addr=server.accept() 
   print(f"connected to{addr}")
   message= communication_socket.recv(1024).decode('utf-8')##buffer size 1024
   print(f"[CLIENT:]{message}")
   communication_socket.send (f"got your message".encode('utf-8'))
   communication_socket.close()
   print(f"connection with {addr}ended!")
        