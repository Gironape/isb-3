import logging
import argparse
import json
import os
from Key_Generator import generate_symmetric_key, write_symmetric_key, generate_Asymmetric_key
from Encryption import Symmetric_encryption, Asymmetric_encryption
from Decryption import Asymmetric_decryption, Symmetric_decryption
def read_settings(file:str) -> dict:
    # Считывает настройки из файла.
    try:
        with open('file/settings.json') as json_f:
            data = json.load(json_f)
        logging.info('Настройки считаны')
    except OSError as err:
        logging.warning(f'{err} Ошибка при чтении файла')
    return data

parser = argparse.ArgumentParser()
parser.add_argument('-set', '--settings', type=str, help='Использовать собственный файл с настройками (Введите '
                                                             'путь к файлу)')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-gen', '--generation', help='Запускает режим генерации ключей')
group.add_argument('-enc', '--encryption', help='Запускает режим шифрования')
group.add_argument('-dec', '--decryption', help='Запускает режим дешифрования')
args = parser.parse_args()
if args.settings:
    settings = read_settings(args.settings)
else:
    settings = read_settings(os.path.join("file", "settings.json"))
if args.generation:
    symmetric_key = generate_symmetric_key()
    logging.info('Генерация симметричного ключа завершена')
    public_key = generate_Asymmetric_key(settings['secret_key'], settings['public_key'])
    c_symmetric_key = Asymmetric_encryption(public_key, symmetric_key)
    logging.info('Симметричный ключ зашифрован')
    write_symmetric_key(settings['symmetric_key'], c_symmetric_key)
elif args.encryption:
    symmetric_key = Asymmetric_decryption(settings['secret_key'], settings['symmetric_key'])
    logging.info('Симметричный ключ расшифрован')
    Symmetric_encryption(settings['initial_file'], symmetric_key, settings['encrypted_file'])
else:
    symmetric_key = Asymmetric_decryption(settings['secret_key'], settings['symmetric_key'])
    logging.info('Симметричный ключ расшифрован!')
    Symmetric_decryption(settings['encrypted_file'], symmetric_key, settings['decrypted_file'])
