import socket
HEADER=64
PORT =9690
SERVER= socket.gethostbyname(socket.gethostname())
ADDR=(SERVER ,PORT)
FORMAT='utf-8'
DISCONNECT_MESSAGE="!OUT"

client=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message=msg.encode(FORMAT)
    msg_length=len(message)
    send_length=str(msg_length).encode(FORMAT)
    send_length +=b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    
def start():
    while True:
        msg =input("You:")
        if msg == DISCONNECT_MESSAGE:
        
            send(msg)
            print("Disconnecting...")
            break
        
        else:
    
            send(msg)
            print(f"sent: {msg}")


start()
client.close()


