# Problem 5: Negative Shift Handling

# Problem 2: Preserve Non-Alphabet Characters
plaintext= input("Enter Plaintext : ")
k =int(input("Enter shift value: "))

ciphertext=""

for char in plaintext:
    if char.isupper():
        encrypted_char=chr((ord(char)-ord("A")+k)%26 + ord("A"))
        
    elif char.islower():
        encrypted_char=chr((ord(char)-ord("a")+k)%26 + ord("a"))
        
    else:
        encrypted_char=char
        
    ciphertext +=encrypted_char
    
print("Chiphertext :",ciphertext)