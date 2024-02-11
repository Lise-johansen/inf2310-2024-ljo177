'''
 A Server  program that:
    1. Recive a reqest from the client for a file
    2. Decripte the file and send it to the client
        2a. Need to be send as bytes 

  Also:
    1. The client and server uses a RSA ans AES encryption to secure the communication
        Posible plan for the encryption process:

        1a. Encrypt a secret key, K, with the RSA cryptosystem for the AES symmetric cryptosystem.
        1b. Encrypt with AES using key K. 
        1c. Transmit the RSA-encrypted key together with the AES-encrypted document. 

    Summery: 
    1. Protect the confidentiality and integrity of data while in transit over the Internet and defend against the following 3 types of attacks:
        - Eavesdropping
        - Man-in-the-middle attacks
        - Replay attacks
'''
import socket
# import os

# Set the address and port
HOST = '127.0.0.1'
PORT = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(1)
print(f"Server listening on {HOST}:{PORT}")

while True:
    # Accept the connection from the client
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    try:
        # Receive the requested file name from the client 
        file_path = client_socket.recv(1024).decode('utf-8')
        print(file_path)

        # Check if the file exists
        try:
            with open(file_path, "rb") as file:
                file_data = file.read()
                client_socket.sendall(file_data)
                print(f"File {file_path} sent successfully")
        except FileNotFoundError:
            client_socket.sendall(b"File not found")

    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        # Close the connection
        client_socket.close()