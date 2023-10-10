import socket



host = 'localhost' 
port = 65534  

# Crear un socket de servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((host, port))

server_socket.listen()

print(f"Servidor escuchando en {host}:{port}")

client_socket, client_address = server_socket.accept()

data = client_socket.recv(1024).decode()
print(f"Cliente dice: {data}")

response = "Hola, Cliente bonito"
client_socket.send(response.encode())

client_socket.close()
server_socket.close()
