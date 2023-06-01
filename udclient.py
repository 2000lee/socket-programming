import socket
import threading
import random

HOST=socket.gethostbyname(socket.gethostname())
PORT=9999
client= socket.socKet(socket.AF_INET,socket.SOCK_DGRAM)
client.bind((HOST,random.randint(8000,9000)))

name=input("nickname:")

def receive():
    while True:
        try:
            message,_ =client.recvfrom(1024)
            print(message.decode())
        except:
            pass
        
t=threading.Thread(target=receive)
t.start()

client.sendto(f"SIGNUP:{name}".encode(),(HOST,PORT))    

while True:
    message=input("")
    if message=="!q":
        exit() 
        
    else:
        client.sendto(f"{name}:{message}".encode(),(HOST,PORT))           
        