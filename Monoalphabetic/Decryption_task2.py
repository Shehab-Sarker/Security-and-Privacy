ciphertext=input("Chipertext: ").upper()
key=input("Key: ").upper()

alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
plaintext=""

for char in ciphertext:
    if char==" ":
        plaintext+=" "
        
    else:
        pos=key.index(char)
        plaintext+=alphabet[pos]
        
print("Plaintext: ",plaintext)