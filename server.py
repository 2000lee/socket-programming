import socket
import threading


HEADER=64
PORT =8080
SERVER= socket.gethostbyname(socket.gethostname())
ADDR=(SERVER , PORT)
FORMAT='utf-8'
DISCONNECT_MESSAGE="!DISCONNECTED"

server=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn,addr):##individual conection
    print(f"[NEW CONECTION]{addr}connected")
    connected= True
    while connected:
        msg_length=conn.recv(HEADER).decode(FORMAT)
        if msg_length:
           msg_length=int(msg_length)
           msg=conn.recv(msg_length).decode(FORMAT)
           if msg==DISCONNECT_MESSAGE:
               conected =False
           print(f"[{addr}]{msg}")

        conn.close()
     
def start():  ##all cnew clients and how sto distrubute them
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn,addr=server.accept()
        thread=threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS]{threading.active_Count() -1}")
print("[STARTING]server is starting....")
start()

