plaintext = input("Plaintext: ").upper()
key=input("Key: ").upper()


alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ciphertext=""

for char in plaintext:
    if char == " ":
        ciphertext+=" "
    
    else:
        pos=alphabet.index(char)
        ciphertext+=key[pos]
        

print("Ciphertext: ", ciphertext)