# # client.py
# # Basic client.py

# import socket

# # Set the address and port
# HOST = '127.0.0.1'
# PORT = 12345

# def download_file(file_name):
#     # Create a socket object
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
#         try:
#             # Connect to the server
#             client_socket.connect((HOST, PORT))
        
#             # Send the file name to the server
#             client_socket.sendall(file_name.encode("utf-8"))

#             # Receive the file content from the server
#             file_content = b""
#             while True:
#                 data_chunk = client_socket.recv(1024)
#                 if not data_chunk:
#                     break
#                 file_content += data_chunk

#             if file_content.strip() == b"File not found":
#                 print(f"File {file_name} not found on the server")
#             else:
#                 # Save the received data to a file
#                 with open("client_file.txt", "wb") as file:
#                     file.write(file_content)
#                     print(f"File {file_name} downloaded successfully")

#         except Exception as e:
#             print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     file_name = "file_name.txt"
#     download_file(file_name)

######################################################################################################################33
# import socket
# from rsa_encryption import RSAEncryption
# from aes_encryption import AESEncryption

# HOST = '127.0.0.1'
# PORT = 12345

# rsa_encryption = RSAEncryption()
# private_key, public_key = rsa_encryption.generate_rsa_key_pair()
# aes_encryption = None

# def download_file(file_name):
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
#         try:
#             client_socket.connect((HOST, PORT))
#             client_socket.settimeout(5)

#             # Send the public RSA key to the server
#             client_socket.sendall(rsa_encryption.save_public_key(public_key))

#             # Receive the encrypted AES key from the server and decrypt it
#             encrypted_aes_key = client_socket.recv(1024)
#             aes_key = rsa_encryption.decrypt(private_key, encrypted_aes_key)
#             aes_encryption = AESEncryption(aes_key=aes_key)

#             client_socket.sendall(file_name.encode("utf-8"))

#             file_content = b""
#             while True:
#                 try:
#                     data_chunk = client_socket.recv(1024)
#                     if not data_chunk:
#                         break
#                     file_content += data_chunk
#                 except socket.timeout:
#                     print("The connection timed out")
#                     break

#             if file_content.strip() == b"File not found":
#                 print(f"File {file_name} not found on the server")
#             else:
#                 try:
#                     decrypted_data = aes_encryption.decrypt_aes(file_content)
#                     print("decrypted_data", decrypted_data)
#                 except Exception as e:
#                     print(f"An error occurred during decryption: {e}")
#                     return
#         finally:
#             client_socket.close()

# if __name__ == "__main__":
#     file_name = "file_name.txt"
#     download_file(file_name)
######################################################################################################################33

# client.py
import socket
from rsa_encryption import RSAEncryption
from aes_encryption import AESEncryption

# Set the address and port
HOST = '127.0.0.1'
PORT = 12345

def download_file(file_name):
    rsa_encryption = RSAEncryption()
    private_key, public_key = rsa_encryption.generate_rsa_key_pair()

    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            # Connect to the server
            client_socket.connect((HOST, PORT))

            # Send the public key to the server
            client_socket.sendall(rsa_encryption.serialize_public_key(public_key))

            # Receive the encrypted AES key from the server and decrypt it
            encrypted_aes_key = client_socket.recv(1024)
            aes_key = rsa_encryption.decrypt_rsa(encrypted_aes_key, private_key)
            aes_encryption = AESEncryption(aes_key)

            # Send the file name to the server
            client_socket.sendall(file_name.encode("utf-8"))

            # Receive the file content from the server
            file_content = b""
            while True:
                data_chunk = client_socket.recv(1024)
                if not data_chunk:
                    break
                file_content += data_chunk

            if file_content.strip() == b"File not found":
                print(f"File {file_name} not found on the server")
            else:
                # Decrypt the received data
                decrypted_file_content = aes_encryption.decrypt_aes(file_content)

                # Save the received data to a file
                with open("client_file.txt", "wb") as file:
                    file.write(decrypted_file_content)
                    print(f"File {file_name} downloaded successfully")

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_name = "file_name.txt"
    download_file(file_name)