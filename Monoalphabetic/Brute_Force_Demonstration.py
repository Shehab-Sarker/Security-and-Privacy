from itertools import permutations

alphabet = input("Alphabet: ").upper()
ciphertext=input("Ciphertext : ").upper()

total_keys=0

for perm in permutations(alphabet):
    key="".join(perm)
    plaintext=""
    
    for char in ciphertext:
        if char in key:
            index=key.index(char)
            plaintext+=alphabet[index]
            
        else:
            plaintext+=char
            
    print(f"Key: {key} -> Plaintext: {plaintext}")
    total_keys+=1
    
print(f"Total Key Tried: {total_keys}")