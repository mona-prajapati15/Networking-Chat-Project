import socket

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5555))  # connect to server

while True:
    message = input("Client: ")
    client.send(message.encode())
    data = client.recv(1024).decode()
    print(f"Server: {data}")
