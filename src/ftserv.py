# # server.py
# # Basic server.py

# import socket
# from rsa_encryption import RSAEncryption
# from aes_encryption import AESEncryption


# def start_server():
#     # Set the address and port
#     HOST = '127.0.0.1'
#     PORT = 12345

#     # Create a socket object
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#     # Bind the socket to the address and port
#     server_socket.bind((HOST, PORT))

#     # Listen for incoming connections
#     server_socket.listen(1)
#     print(f"Server listening on {HOST}:{PORT}")
    
#     while True:
#         # Accept the connection from the client
#         client_socket, client_address = server_socket.accept()
#         print(f"Connection from {client_address}")

#         try:
#             # Receive the requested file name from the client 
#             file_path = client_socket.recv(1024).decode('utf-8')
#             print(file_path)

#             # Check if the file exists
#             try:
#                 with open(file_path, "rb") as file:
#                     file_data = file.read()
#                     client_socket.sendall(file_data)
#                     print(f"File {file_path} sent successfully")
#             except FileNotFoundError:
#                 client_socket.sendall(b"File not found")

#         except Exception as e:
#             print(f"An error occurred: {e}")
            
#         finally:
#             # Close the connection
#             client_socket.close()

# ######################################################################################################################33
# # from crypto_module import Encryption
# import socket
# import os
# from rsa_encryption import RSAEncryption
# from aes_encryption import AESEncryption

# HOST = '127.0.0.1'
# PORT = 12345

# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind((HOST, PORT))
# server_socket.listen(1)
# print(f"Server listening on {HOST}:{PORT}")

# rsa_encryption = RSAEncryption()
# aes_key = os.urandom(32)
# aes_encryption = AESEncryption(aes_key=aes_key)

# while True:
#     client_socket, client_address = server_socket.accept()
#     print(f"Connection from {client_address}")

#     try:
#         # Receive the client's RSA public key
#         client_public_key = rsa_encryption.load_public_key(client_socket.recv(1024))

#         # Encrypt the AES key using the client's RSA public key and send it to the client
#         encrypted_aes_key = rsa_encryption.encrypt_rsa(aes_key, client_public_key)
#         file_name = client_socket.recv(1024).decode('utf-8')
#         print(file_name)

#         try:
#             with open(file_name, "rb") as file:
#                 file_data = file.read()
#                 # encrypted_data = aes_encryption.encrypt_aes(file_data, aes_encryption.aes_key)
#                 encrypted_data = aes_encryption.encrypt_aes(file_data)
#                 client_socket.sendall(encrypted_data)
#                 print(f"File {file_name} sent successfully")

#         except FileNotFoundError:
#             client_socket.sendall(b"File not found")

#     except Exception as e:
#         print(f"An error occurred: {e}")
        
#     finally:
#         client_socket.close()

# ######################################################################################################################33

# server.py
import socket
import os
from rsa_encryption import RSAEncryption
from aes_encryption import AESEncryption

def start_server():
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

    rsa_encryption = RSAEncryption()
    private_key, public_key = rsa_encryption.generate_rsa_key_pair()
    aes_encryption = AESEncryption(os.urandom(16))

    while True:
        # Accept the connection from the client
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        try:
            # Receive the public key from the client
            client_public_key = rsa_encryption.load_public_key(client_socket.recv(1024))

            # Send the encrypted AES key to the client
            encrypted_aes_key = rsa_encryption.encrypt_rsa(aes_encryption.aes_key, client_public_key)
            client_socket.sendall(encrypted_aes_key)

            # Receive the requested file name from the client 
            file_path = client_socket.recv(1024).decode('utf-8')
            print(file_path)

            # Check if the file exists
            try:
                with open(file_path, "rb") as file:
                    file_data = file.read()
                    encrypted_file_data = aes_encryption.encrypt_aes(file_data)
                    client_socket.sendall(encrypted_file_data)
                    print(f"File {file_path} sent successfully")
                    print("here")
            except FileNotFoundError:
                client_socket.sendall(b"File not found")

        except Exception as e:
            print(f"An error occurred: {e}")
            
        finally:
            # Close the connection
            client_socket.close()

if __name__ == "__main__":
    start_server()