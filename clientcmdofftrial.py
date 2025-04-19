import socket

HEADER = 64
PORT = 9690
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!OUT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send_command(command):
    # Send the command length
    command_encoded = command.encode(FORMAT)
    command_length = len(command_encoded)
    send_length = str(command_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(command_encoded)

    # Receive the response length
    response_length = client.recv(HEADER).decode(FORMAT)
    if response_length:
        response_length = int(response_length.strip())
        # Receive the response
        response = client.recv(response_length).decode(FORMAT)
        print(f"[SERVER RESPONSE]\n{response}")


# Interactive command input
print("Enter commands to execute on the server (type '!DISCONNECTED' to exit):")
while True:
    command = input("> ")
    if command == DISCONNECT_MESSAGE:
        send_command(DISCONNECT_MESSAGE)
        print("[CLIENT] Disconnected from the server.")
        break
    send_command(command)

