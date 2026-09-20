# Problem 4: Brute-Force Attack
# Caesar Cipher Cryptanalysis

ciphertext = input( "Enter ciphertext: ")

for k in range(26):
    plaintext=""
    for char in ciphertext:
        if char.isupper():
             decrypted_char=chr((ord(char)-ord("A")-k)%26 + ord("A"))
             
        elif char.islower():
             decrypted_char=chr((ord(char)-ord("a")-k)%26 + ord("a"))
             
        else:
             decrypted_char=char
             
        plaintext+=decrypted_char
        
    print(f"Shift {k} : {plaintext}")