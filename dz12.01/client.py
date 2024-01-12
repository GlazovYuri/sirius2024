import socket
import sys

filename = sys.argv[1]

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect(("localhost", 25565))
    client_socket.sendall(filename.encode('utf-8'))
    response = client_socket.recv(4096)
    print(response.decode('utf-8'))

except Exception:
    print(f"Error: {Exception}")

client_socket.close()
