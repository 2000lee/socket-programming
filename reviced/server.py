import socket
import threading
HEADER=64
PORT =9690
SERVER= socket.gethostbyname(socket.gethostname())   
ADDR=(SERVER , PORT) 
FORMAT='utf-8'
DISCONNECT_MESSAGE="!OUT"

server=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn,ADDR):##individual connection
    print(f"[NEW CONNECTION]{ADDR}connected")
    connected= True
    while connected:
        msg_length=conn.recv(HEADER).decode(FORMAT)
        if msg_length:
           msg_length=int(msg_length)
           msg=conn.recv(msg_length).decode(FORMAT)
           if msg==DISCONNECT_MESSAGE:
               connected =False
           print(f"[{ADDR}]{msg}")

    conn.close()
     
def start():  ##all new clients and how sto distrubute them
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn,ADDR=server.accept()
        thread=threading.Thread(target=handle_client,args=(conn,ADDR))
        thread.start()
        print(f"[ACTIVE CONNECTIONS]{threading.active_count() -1}")
print("[STARTING]server is starting....")
start()

