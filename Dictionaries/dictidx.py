"""
Dictionary lookup and update.
"""


print("Dictionary Lookup")
print("=================")

cipher = {'p': 'o', 'y': 'h', 't': 'n',
          'h': 't', 'o': 'y', 'n': 'p'} 
#print(cipher)
for key, val in cipher.items():
    print(key,"-",val)
# Use indexing with keys to access values
print("cipher['t']" ,cipher['t'])
print("cipher['n']",cipher['n'])

def encrypt(cipher, word):
    """encrypt word using cipher"""
    encrypted = ""
    for char in word:
        encrypted += cipher[char]
    return encrypted

python = "python"
enc = encrypt(cipher, python)
print("original - ", python, " and encrypted - ", enc)

# It is an error to use a non-existent key
#print(cipher[1])

# Use .get when you are unsure if the key exists
print("cipher.get('t')", cipher.get('t'))
print("cipher.get(1)", cipher.get(1))
print("cipher.get(1, 'z')", cipher.get(1, 'z'))

print("")
print("Dictionary Update")
print("=================")

print(cipher)

# Modify an existing key->value mapping
cipher['p'] = 'q'
print(cipher)

# Create a new key->value mapping
cipher['r'] = 'z'
print(cipher)

enc2 = encrypt(cipher, python)
print(python, enc, enc2)