from hashlib import sha256

value = input("Enter the text you want to hash:\n")
hash = sha256(value.encode('utf-8'))
hashed = hash.hexdigest()
print(hashed)
