import logging
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import padding as s_padding
from cryptography.hazmat.primitives import hashes

logger = logging.getLogger()
logger.setLevel('INFO')

def Symmetric_encryption() -> bytes:
    f = open("file/symmetric_key.txt", "rb")
    key = bytes(f.read())
    print("AAAAAAAAAA", key)
    padder = padding.ANSIX923(64).padder()
    text = bytes('кто прочитал тот здохнет', 'UTF-8')
    padded_text = padder.update(text)+padder.finalize()
    print("УГАГА", text)
    print(padded_text)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    c_text = encryptor.update(padded_text) + encryptor.finalize()
    print("КАМОН МЭН", c_text)
    return c_text
def Asymmetric_encryption(public_key, symmetric_key:bytes) -> bytes:
    c_text = public_key.encrypt(symmetric_key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                  algorithm=hashes.SHA256(), label=None))
    return c_text