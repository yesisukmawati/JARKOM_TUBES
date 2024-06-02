from socket import *
import sys
import threading


serverSocket = socket(AF_INET, SOCK_STREAM)
server_ip = "127.0.0.1"
port = 6789
serverSocket.bind((server_ip, port))
serverSocket.listen(3)

print(f'Server listening on {server_ip}:{port}')

def handle_request(connectionSocket, addr):
  try:
    message = connectionSocket.recv(1024).decode()
    print(f"Received request: {message}")
    request_lines = message.split("\r\n")
    request_line = request_lines[0].split()
    filename = message.split(' ')[1][1:]
    print(f"{threading.current_thread().name}: {filename} accepted")
    f = open(filename, 'rb')
    outputdata = f.read()
    f.close()

    header = "HTTP/1.1 200 OK\r\n\r\n"
    connectionSocket.send(header.encode())

    
    connectionSocket.sendall(outputdata)

    connectionSocket.close()
    print(f'File {filename} sent to {addr}')
    
  except IOError:

    request = f'GET /index.html HTTP/1.1\r\nHost: {server_ip}:{port}\r\n\r\n'
    connectionSocket.send(request.encode())
    connectionSocket.close()
    print(f'File not found for {addr}')

print('Ready to serve...')
while True:
    connectionSocket, addr = serverSocket.accept()
    # Membuat thread baru untuk melayani permintaan
    thread = threading.Thread(target=handle_request, args=(connectionSocket, addr))
    thread.start()

serverSocket.close()
sys.exit()
    

