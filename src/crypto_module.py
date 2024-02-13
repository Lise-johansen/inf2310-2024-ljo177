# crypto_module.py
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

class Encryption:
    def __init__(self):
        self.private_key, self.public_key = self.generate_rsa_key_pair()
   
    def generate_iv(self):
        return os.urandom(16)

    def generate_rsa_key_pair(self):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        public_key = private_key.public_key()
        return private_key, public_key

    def encrypt_rsa(self, plaintext, public_key):
        ciphertext = public_key.encrypt(
            plaintext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return ciphertext

    def decrypt_rsa(self, ciphertext, private_key):
        plaintext = private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return plaintext


    def encrypt_aes(self, plaintext, aes_key):
        cipher = Cipher(algorithms.AES(aes_key), modes.CFB(self.iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(plaintext) + encryptor.finalize()
        return ciphertext

    def decrypt_aes(self, ciphertext, aes_key):
        cipher = Cipher(algorithms.AES(aes_key), modes.CFB(self.iv), backend=default_backend())
        decryptor = cipher.decryptor()
        plaintext = decryptor.update(ciphertext) + decryptor.finalize()
        return plaintext
    
    # def encrypt_aes(self, plaintext, aes_key, iv):
    #     cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv), backend=default_backend())
    #     encryptor = cipher.encryptor()
    #     ciphertext = encryptor.update(plaintext) + encryptor.finalize()
    #     return ciphertext

    # def decrypt_aes(self, ciphertext, aes_key, iv):
    #     cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv), backend=default_backend())
    #     decryptor = cipher.decryptor()
    #     # plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    #     plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    #     return plaintext