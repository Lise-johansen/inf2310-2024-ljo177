import socket
import os
from rsa_and_aes_encryption import RSAEncryption

def start_server():
    # Set the address and port
    HOST = '127.0.0.1'
    PORT = 12345

    # Create a socket object, bind it to the address and port and listen for incoming connections
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Server listening on {HOST}:{PORT}")

    # Create an RSA key pair and an AES key
    rsa_encryption = RSAEncryption()
    private_key, public_key = rsa_encryption.generate_rsa_key_pair()

    while True:
        # Accept the connection from the client
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        try:
            # Receive the public key from the client
            client_public_key = client_socket.recv(4096)
            print("Public key received")

            # Deserialize the public key            
            deserialize_public_key = rsa_encryption.load_public_key(client_public_key)

            # Send the encrypted AES key to the client
            encrypted_aes_key = rsa_encryption.encrypt_rsa(os.urandom(16), deserialize_public_key)
            client_socket.sendall(encrypted_aes_key)
            print("Encrypted AES key sent to client")

            # Receive the requested file name from the client 
            file_path = client_socket.recv(1024).decode('utf-8')

            # Check if the file exists
            try:
                with open(file_path, "rb") as file:
                    file_data = file.read()

                    # Encrypt the file data with the client's public key
                    encrypted_file_data = rsa_encryption.encrypt_aes(file_data, deserialize_public_key)
                    client_socket.sendall(encrypted_file_data)
                    print(f"Encrypted file sent successfully")

            except FileNotFoundError:
                client_socket.sendall(b"File not found")

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            # Close the connection
            client_socket.close()

if __name__ == "__main__":
    start_server()