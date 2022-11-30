import os
from hashlib import sha512
from hashlib import sha256

os.system('cls' if os.name == 'nt' else 'clear')
value = input("Enter the text you want to hash:\n")

os.system('cls' if os.name == 'nt' else 'clear')
algorithm = input('Enter hash algorithm (currently only support SHA256 and SHA512):\n')

os.system('cls' if os.name == 'nt' else 'clear')
if algorithm == 'sha256' or algorithm == 'SHA256':
    hash = sha256(value.encode('utf-8'))
elif algorithm == 'sha512' or algorithm == 'SHA512':
    hash = sha512(value.encode('utf-8'))
else:
    print('I told you that this script currently only support SHA256 and SHA512 you baka!')
    exit()

hashed = hash.hexdigest()

os.system('cls' if os.name == 'nt' else 'clear')
print(f'Your hash: {hashed}\n')
