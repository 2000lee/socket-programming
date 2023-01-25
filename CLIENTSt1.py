import socket



HEADER=64  ##the first megssege of message sent should be at least 64 bytes that would carry the length of the message that would be next
PORT =8080
SERVER= socket.gethostbyname(socket.gethostname())
ADDR=(SERVER , PORT)
FORMAT='utf-8'
DISCONNECT_MESSAGE="!DISCONNECTED"

client=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message=msg.encode(FORMAT)
    msg_length=len(message)
    send_length=str(msg_length).encode(FORMAT)
    send_length +=b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

send("hello there!")
send("hi tim")

