from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization

# class RSAEncryption:
#     def __init__(self):
#         self.private_key, self.public_key = self.generate_rsa_key_pair()

#     def generate_rsa_key_pair(self):
#         private_key = rsa.generate_private_key(
#             public_exponent=65537,
#             key_size=2048,
#             backend=default_backend()
#         )
#         public_key = private_key.public_key()
#         return private_key, public_key

#     def encrypt_rsa(self, plaintext, public_key):
#         ciphertext = public_key.encrypt(
#             plaintext,
#             padding.OAEP(
#                 mgf=padding.MGF1(algorithm=hashes.SHA256()),
#                 algorithm=hashes.SHA256(),
#                 label=None
#             )
#         )
#         return ciphertext

#     def decrypt_rsa(self, ciphertext, private_key):
#         plaintext = private_key.decrypt(
#             ciphertext,
#             padding.OAEP(
#                 mgf=padding.MGF1(algorithm=hashes.SHA256()),
#                 algorithm=hashes.SHA256(),
#                 label=None
#             )
#         )
#         return plaintext
    
#     # def load_public_key(self, public_key_bytes):
#     #     return rsa.RSAPublicKey.load_pem(public_key_bytes, backend=default_backend())
    
#     def load_public_key(self, public_key_bytes):
#         public_key = serialization.load_pem_public_key(public_key_bytes, backend=default_backend())
#         return public_key
    
#     def save_public_key(filename, public_key):
#         pem = public_key.public_bytes(
#             encoding=serialization.Encoding.PEM,
#             format=serialization.PublicFormat.SubjectPublicKeyInfo
#         )
#         with open(filename, 'wb') as f:
#             f.write(pem)

# class RSAEncryption:
#     def __init__(self):
#         self.private_key, self.public_key = self.generate_rsa_key_pair()

#     def generate_rsa_key_pair(self):
#         private_key = rsa.generate_private_key(
#             public_exponent=65537,
#             key_size=2048,
#             backend=default_backend()
#         )
#         public_key = private_key.public_key()
#         return private_key, public_key

#     def encrypt_rsa(self, plaintext, public_key):
#         ciphertext = public_key.encrypt(
#             plaintext,
#             padding.OAEP(
#                 mgf=padding.MGF1(algorithm=hashes.SHA256()),
#                 algorithm=hashes.SHA256(),
#                 label=None
#             )
#         )
#         return ciphertext

#     def decrypt_rsa(self, ciphertext, private_key):
#         plaintext = private_key.decrypt(
#             ciphertext,
#             padding.OAEP(
#                 mgf=padding.MGF1(algorithm=hashes.SHA256()),
#                 algorithm=hashes.SHA256(),
#                 label=None
#             )
#         )
#         return plaintext

#     def load_public_key(self, public_key_bytes):
#         public_key = serialization.load_pem_public_key(public_key_bytes, backend=default_backend())
#         return public_key

#     def serialize_public_key(self, public_key):
#         pem = public_key.public_bytes(
#             encoding=serialization.Encoding.PEM,
#             format=serialization.PublicFormat.SubjectPublicKeyInfo
#         )
#         return pem

#     def save_public_key(self, filename, public_key):
#         pem = self.serialize_public_key(public_key)
#         with open(filename, 'wb') as f:
#             f.write(pem)

# rsa_encryption.py
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization

class RSAEncryption:
    def __init__(self):
        self.private_key, self.public_key = self.generate_rsa_key_pair()

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

    def load_public_key(self, public_key_bytes):
        public_key = serialization.load_pem_public_key(public_key_bytes, backend=default_backend())
        return public_key

    def serialize_public_key(self, public_key):
        pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        return pem
