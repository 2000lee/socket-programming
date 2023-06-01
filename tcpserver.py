import socket
import threading

HOST=  '192.168.56.1'
PORT = 9999
addr= (HOST,PORT)
server =socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(addr)
server.listen()

clients=[]
nicknames=[]

def broadcast(message):
    for client in clients:
        client.send(message)
        
def handle(client):
    while True:
        try:
            message=clients.recv(1024)
            broadcast(message) 
        except:
            index=clients.index(client)   
            clients.remove(client)
            client.close()
            nickname =nicknames[index]   
            broadcast('{}left'.format(nickname).encode('ascii')) 
            nicknames.remove(nickname)
            break
        
def receive():
    while True:
        client,address=server.accept()
        print("Connected with {}".format(str(address)))
        
        client.send('NICK'.encode('ascii'))
        nickname=client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)
        
        print("Nickname is {}".format(nickname))
        broadcast("{}joined!".format(nickname).encode('ascii'))
        client.send('connected to server!'.encode('ascii'))
        
        thread =threading.Thread(target=handle ,args=(client))
        thread.start()
        
receive()        
                