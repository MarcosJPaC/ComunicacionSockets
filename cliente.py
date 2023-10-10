import socket

host = 'localhost'  
port = 65534  

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((host, port))

message = "Hola, servidor bonito"
client_socket.send(message.encode())

data = client_socket.recv(1024).decode()
print(f"Servidor dice: {data}")

client_socket.close()
