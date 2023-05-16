import logging
import argparse
import json
import os

from key_generator import generate_symmetric_key, write_symmetric_key, generate_asymmetric_key
from encryption import symmetric_encryption, asymmetric_encryption
from decryption import asymmetric_decryption, symmetric_decryption


def read_settings(file:str) -> dict:
    """ Считывает настройки из файла.
        :param file: Путь к файлу.
    """
    try:
        with open(file) as json_f:
            data = json.load(json_f)
        logging.info('Настройки считаны')
    except OSError as err:
        logging.warning(f'{err} Ошибка при чтении файла')
    return data

if __name__ == '__main__':
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
        public_key = generate_asymmetric_key(settings['secret_key'], settings['public_key'])
        c_symmetric_key = asymmetric_encryption(public_key, symmetric_key)
        logging.info('Симметричный ключ зашифрован')
        write_symmetric_key(settings['symmetric_key'], c_symmetric_key)
    elif args.encryption:
        symmetric_key = asymmetric_decryption(settings['secret_key'], settings['symmetric_key'])
        logging.info('Симметричный ключ расшифрован')
        symmetric_encryption(settings['initial_file'], symmetric_key, settings['encrypted_file'])
    else:
        symmetric_key = asymmetric_decryption(settings['secret_key'], settings['symmetric_key'])
        logging.info('Симметричный ключ расшифрован!')
        symmetric_decryption(settings['encrypted_file'], symmetric_key, settings['decrypted_file'])
