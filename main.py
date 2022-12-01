import os, binascii, hashlib

os.system('cls' if os.name == 'nt' else 'clear')
value = input("Enter the text you want to hash:\n")

os.system('cls' if os.name == 'nt' else 'clear')
algorithm = input('Enter hash algorithm (currently only support SHA256 and SHA512:\n')

os.system('cls' if os.name == 'nt' else 'clear')
if algorithm == 'sha256' or algorithm == 'SHA256':
    hash = hashlib.sha256(value.encode('utf-8'))
elif algorithm == 'sha512' or algorithm == 'SHA512':
    hash = hashlib.sha512(value.encode('utf-8'))
else:
    print(f'\nWTF is {algorithm}???\n')
    exit()

hashed = hash.hexdigest()

os.system('cls' if os.name == 'nt' else 'clear')
print(f'\nYou choosed: {algorithm}\nHash: {hashed}\n')
