import base64

encrypted = 'your encrypted message'
decrypted = ''

key = 'your username'

x = 0
for i, c in enumerate(base64.b64decode(encrypted)):
    decrypted += chr(c ^ ord(key[i % len(key)]))

print(decrypted)