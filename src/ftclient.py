import socket
from rsa_and_aes_encryption import RSAEncryption

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
            print("Public key sent")

            # Receive the encrypted AES key from the server and decrypt it
            encrypted_aes_key = client_socket.recv(1024)
            aes_key = rsa_encryption.decrypt_rsa(encrypted_aes_key, private_key)
            print("AES key received and decrypted")

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
                decrypted_file_content = rsa_encryption.decrypt_aes(file_content, private_key)

                # Save the received data to a file
                new_file_name = "decrypted_" + file_name
                with open(new_file_name, "wb") as file:
                    file.write(decrypted_file_content)

                    print(f"File downloaded and decrypted successfully")

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    #Do this priteier
    # file_name = "message.txt"
    file_name = "Tux.png"
    download_file(file_name)