from socket import *
import os
import time

serverName = 'localhost'
serverPort = 6789

def handle_request(connectionSocket):
    try:
        request = connectionSocket.recv(1024).decode('utf-8')
        filename = request.split()[1][1:]
        print(f"{filename} accepted")

        if os.path.isfile(filename):
            with open(filename, 'rb') as file:
                response_content = file.read()
        
            response = b"HTTP/1.1 200 OK\r\n\r\n" + response_content
        else:
            response = b"HTTP/1.1 404 Not Found\r\n\r\nFile not found"

        connectionSocket.sendall(response)

    except Exception as e:
        print(f"Error handling request: {e}")
    
    connectionSocket.close()

def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen()
    print(f"Server berjalan di http://{serverName}:{serverPort}")
    
    while True:
        connectionSocket, socketAddress = serverSocket.accept()
        print(f"Koneksi diterima dari {socketAddress}")
        handle_request(connectionSocket)
      #   time.sleep(3)

if __name__ == "__main__":
    main()