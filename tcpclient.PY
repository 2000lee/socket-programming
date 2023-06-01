import socket
import threading

HOST= "192.168.56.1"
PORT= 9696

nickname=input("Choose your nickname")
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST,PORT))

def receive():
    while True:
        try:
            message=client.recv(1024).decode('ascii')
            if message =='NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("AN error has occured")
            client.close()
            break        

def write():
    while True:
        message='{}:{}'.format(nickname,input(''))
        client.send(message.encode('ascii'))
        
receive_thread=threading.Thread(target=receive)
receive_thread.start()

write_thread=threading.Thread(target=write)
write_thread.start()                        
       