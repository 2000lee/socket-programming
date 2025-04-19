import socket
import threading
import os


HEADER=64
PORT =9690
SERVER= socket.gethostbyname(socket.gethostname())   
ADDR=(SERVER , PORT) 
FORMAT='utf-8'
DISCONNECT_MESSAGE="!OUT"
DELETE_COMMAND ="!DEL"
FILE_TO_DELETE ="official123server.py"
server=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn,addr):##individual connection
    print(f"[NEW CONNECTION]{addr}connected")
    connected= True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
           msg_length = int(msg_length.strip())
           msg = conn.recv(msg_length).decode(FORMAT)
           if msg == DISCONNECT_MESSAGE:
               connected =False
               print(f"[{addr}]{msg}")
           
          # elif msg == DELETE_COMMAND:
           
            #   if os.path.exists(FILE_TO_DELETE):
             #      try:
              #         os.remove(FILE_TO_DELETE)
               #        print(f"[{addr}] File '{FILE_TO_DELETE}' deleted successfully")
                #       conn.send(f"file'{FILE_TO_DELETE}'deleted".encode(FORMAT))
                 #  except Exception as e:
                  #     conn.send(f"ERROR DELETEING FILE: {str(e)}".encode(FORMAT))
              # else:
               #    conn.send(f"File '{FILE_TO_DELETE}' not found.".encode(FORMAT))
           else:
               print(f"[{addr}] {msg}")
               conn.send(f"Received: {msg}".encode(FORMAT))
               

    conn.close()
     
def start():  ##all new clients and how sto distrubute them
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn,addr=server.accept()
        thread=threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS]{threading.active_count() -1}")
print("[STARTING]server is starting....")
start()

