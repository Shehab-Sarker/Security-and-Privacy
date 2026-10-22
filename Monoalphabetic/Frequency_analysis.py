# Frequency Analysis

from collections import Counter

ciphertext = input("Ciphertext: ").upper()

english_frequency = "ETAOINSHRDLCUMWFGYPBVKJXQZ"


letter_counts= Counter()

for char in ciphertext:
    if char.isalpha():
        letter_counts[char]+=1
        

sorted_letters = []

for char in letter_counts:
    sorted_letters.append([char, letter_counts[char]])
    
    for i in range(len(sorted_letters)):
        for j in range(i+1, len(sorted_letters)):
            if sorted_letters[j][1]> sorted_letters[i][1]:
                sorted_letters[i], sorted_letters[j]=(
                    sorted_letters[j],sorted_letters[i]
                )

print("\nFrequency Table (Top): ")

for item in sorted_letters:
    print(item[0] + ":", item[1])
    
    
#Create gussed substitution
substitution = {}

for i in range(len(sorted_letters)):
    char = sorted_letters[i][0]
    substitution[char]=english_frequency[i]
    
    
print("\nGuessed Substitution : ")

for item in sorted_letters:
    char = item[0]
    print(char + "->" + substitution[char])
    
    
decoded = ""


for char in ciphertext:
    if char in ciphertext:
        if char in substitution:
            decoded+=substitution[char]
        else:
            decoded+=char
            
print("\nPartial Decode: ")
print(decoded.lower())