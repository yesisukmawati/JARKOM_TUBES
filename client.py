from socket import *
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: client.py server_host server_port filename")
        return
    
    serverName = sys.argv[1]
    serverPort = int(sys.argv[2])
    filename = sys.argv[3]

    clientSocket = socket(AF_INET, SOCK_STREAM)

    try:
        clientSocket.connect((serverName, serverPort))

        request = f"GET /{filename} HTTP/1.1\r\nHost: {serverName}:{serverPort}\r\n\r\n"
        clientSocket.sendall(request.encode('utf-8'))

        response = clientSocket.recv(4096)
        print(response.decode('utf-8'))

    except Exception as e:
        print(f"Error: {e}")
    
    clientSocket.close()

if __name__ == "__main__":
    main()