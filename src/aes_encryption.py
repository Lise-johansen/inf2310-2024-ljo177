# import os
# from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# class AESEncryption:
#     def __init__(self, aes_key):
#         self.aes_key = aes_key
#         self.iv = self.generate_iv()

#     def generate_iv(self):
#         return os.urandom(16)

#     def encrypt_aes(self, plaintext):
#         cipher = Cipher(algorithms.AES(self.aes_key), modes.CFB(self.iv), backend=default_backend())
#         encryptor = cipher.encryptor()
#         ciphertext = encryptor.update(plaintext) + encryptor.finalize()
#         return ciphertext

#     def decrypt_aes(self, ciphertext):
#         cipher = Cipher(algorithms.AES(self.aes_key), modes.CFB(self.iv), backend=default_backend())
#         decryptor = cipher.decryptor()
#         plaintext = decryptor.update(ciphertext) + decryptor.finalize()
#         return plaintext

# aes_encryption.py
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

class AESEncryption:
    def __init__(self, aes_key):
        self.aes_key = aes_key
        self.iv = self.generate_iv()

    def generate_iv(self):
        return os.urandom(16)

    def encrypt_aes(self, plaintext):
        cipher = Cipher(algorithms.AES(self.aes_key), modes.CFB(self.iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(plaintext) + encryptor.finalize()
        return ciphertext

    def decrypt_aes(self, ciphertext):
        cipher = Cipher(algorithms.AES(self.aes_key), modes.CFB(self.iv), backend=default_backend())
        decryptor = cipher.decryptor()
        plaintext = decryptor.update(ciphertext) + decryptor.finalize()
        return plaintext
