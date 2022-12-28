import os, hashlib

os.system('cls' if os.name == 'nt' else 'clear')

algorithm = input('Enter hash algorithm ("?" for available algorithm):\n')
algorithm = algorithm.lower()
os.system('cls' if os.name == 'nt' else 'clear')

supported_algorithm = hashlib.algorithms_available

if algorithm == '?':
    print(f"Available algorithm:\n{hashlib.algorithms_available}")
    exit()
elif algorithm not in supported_algorithm:
    print(f'\nWTF is {algorithm}!?\n')
    exit()

value = input('Enter the text you want to hash:\n')
os.system('cls' if os.name == 'nt' else 'clear')

hash = hashlib.new(f'{algorithm}')
hash.update(value.encode('utf-8'))
hashed = hash.hexdigest()

print(f'\nYou choosed: {algorithm}\nHash: {hashed}\n')
