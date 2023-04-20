import json
SETTINGS = {
    'initial_file': 'file/initial_file.txt',
    'encrypted_file': 'file/encrypted_file.txt',
    'decrypted_file': 'file/decrypted_file.txt',
    'symmetric_key': 'file/symmetric_key.txt',
    'public_key': 'file/public_key.pem',
    'secret_key': 'file/secret_key.pem',
}
if __name__ == '__main__':
    with open('settings.json', 'w') as fp:
        json.dump(SETTINGS, fp)