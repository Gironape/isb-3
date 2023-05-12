
import argparse
from Key_Generator import generate_symmetric_key, write_symmetric_key, generate_Asymmetric_key
from Encryption import Symmetric_encryption
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-gen', '--generation', help='Запускает режим генерации ключей')
group.add_argument('-enc', '--encryption', help='Запускает режим шифрования')
group.add_argument('-dec', '--decryption', help='Запускает режим дешифрования')

args = parser.parse_args()
if args.generation is not None:
    symmetric_key = generate_symmetric_key()
    print("EBAT", symmetric_key)
    write_symmetric_key(symmetric_key)
    public_key = generate_Asymmetric_key()
elif args.encryption is not None:
    print(Symmetric_encryption())
else:
    pass
