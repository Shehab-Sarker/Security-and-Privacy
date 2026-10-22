#key Generation from keyboard

keyword=input("keyword : ").upper()

alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

cipher_alphbt=""

for char in keyword:
    if char.isalpha() and char not in cipher_alphbt:
        cipher_alphbt+=char
        
for char in alphabet:
    if char not in cipher_alphbt:
        cipher_alphbt+=char
        
        
print("Cipher Alphabet: ",cipher_alphbt)
print("\nMapping:")
print(alphabet)
print(cipher_alphbt)