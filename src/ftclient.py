import socket
from crypto_utils import Cryptoutils

def download_file(file_name):
    crypto_utils = Cryptoutils()
    private_key, public_key = crypto_utils.generate_rsa_key_pair()

    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            # Connect to the server
            client_socket.connect((HOST, PORT))

            # Send the public key to the server
            client_socket.sendall(crypto_utils.serialize_public_key(public_key))
            print("Public key sent")

            # Receive the encrypted AES key from the server and decrypt it
            encrypted_aes_key = client_socket.recv(1024)
            aes_key = crypto_utils.decrypt_rsa(encrypted_aes_key, private_key)
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
                decrypted_file_content = crypto_utils.decrypt_aes(file_content, private_key)

                # Save the received data to a file
                new_file_name = f"decrypted_{file_name}"
                with open(new_file_name, "wb") as file:
                    file.write(decrypted_file_content)

                print(f"File downloaded and decrypted successfully")

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Get the address and port from the user
    user_input_HOST = input("Enter the HOST address: ")
    user_input_PORT = input("Enter the PORT number: ")

    try:
        # Validate the input for HOST
        if user_input_HOST == '127.0.0.1':
            HOST = '127.0.0.1'
        else:
            raise ValueError(f"{user_input_HOST} is the wrong HOST address")

        # Validate the input for PORT
        if int(user_input_PORT) == 12345:
            PORT = 12345
        else:
            raise ValueError(f"{user_input_PORT} is the wrong PORT number")

    except ValueError as e:
        print(f"Validation error: {e}")
        exit()  # Terminate the program for incorrect input

    file_name = None

    while file_name not in ["message.txt", "Tux.png"]:
        user_input = input("Enter 1 to download the text file or 2 to download the image file: ")
        
        if user_input == "1":
            file_name = "message.txt"
        elif user_input == "2":
            file_name = "Tux.png"
        else:
            print("Invalid input. Please enter 1 or 2.")

    # Now, you have a valid file_name, and you can proceed to download the file.
    download_file(file_name)
    