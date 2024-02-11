'''
 A client program that:
    1. Send a reqest to server for a file
    2. Receives the file from the server
    3. Saves the file to the local file system (not needed for this assignment) 

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

# Set the address and port
HOST = '127.0.0.1'
PORT = 12345

def download_file(file_name):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((HOST, PORT))
    
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
            # Save the received data to a file
            with open("client_file.txt", "wb") as file:
                file.write(file_content)
                print(f"File {file_name} downloaded successfully")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    response = input("Do you want to receive a file? (yes/no): ").lower()
    if response == "yes":
        file_name = "file_name.txt"
        download_file(file_name)
    elif response == "no":
        print("No request sent.")
    else:
        print("Invalid response.")
