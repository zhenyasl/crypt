import ssl
import socket

# Setting up an SSL connection
context = ssl.create_default_context()
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_socket = context.wrap_socket(client_socket, server_hostname='www.google.com')
ssl_socket.connect(('www.google.com', 443))

# Sending a GET request
request = 'GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n'
ssl_socket.sendall(request.encode())

# Getting a response
response = ssl_socket.recv(4096)
print('Server response:\n', response.decode())

# Close the connection
ssl_socket.close()