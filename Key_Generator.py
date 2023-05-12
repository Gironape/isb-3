import os
import logging
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
def generate_symmetric_key() -> bytes:
    key = os.urandom(128)
    return key

def write_symmetric_key(symmetric_key) -> None:
    with open("file/symmetric_key.txt", "wb") as key_w:
        key_w.write(symmetric_key)

def generate_Asymmetric_key() ->bytes:
    keys = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    private_key = keys
    public_key = keys.public_key()

    try:
        with open("file/public_key.pem", 'wb') as public_write:
            public_write.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                     format=serialization.PublicFormat.SubjectPublicKeyInfo))
        logging.info(f' Открытый ключ записан в {public_key}')
    except OSError as err:
        logging.warning(f'{err} Ошибка при записи ключа в {public_key}')
    try:
        with open("file/secret_key.pem", 'wb') as private_write:
            private_write.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                        format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                        encryption_algorithm=serialization.NoEncryption()))
        logging.info(f'Приватный ключ записан в {private_key}')
    except OSError as err:
        logging.warning(f'{err} Ошибка при записи ключа в {private_key}')
    return public_key