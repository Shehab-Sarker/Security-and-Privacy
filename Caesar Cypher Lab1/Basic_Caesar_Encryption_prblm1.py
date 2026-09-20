# Problem-1: Basic Caesar Encryption (Uppercase Only) 
# Write a Python program that takes: 
# 1. A plaintext string consisting only of uppercase English letters (A–Z) 
# 2. An integer shift value k 
# and outputs the encrypted ciphertext using the Caesar Cipher rule: 
# Input Example 
# HELLO 
# 3 
# Output Example 
# KHOOR 
# Assume: 
# • No lowercase letters 
# • No spaces or special characters 


#Caesar Cipher - Basic Encryption
# Uppercase Letter only

plaintext = input("Enter plaintext : ")
k=int(input("Enter Shift values: "))

ciphertext = ""

for char in plaintext:
    encrypted_char = chr((ord(char)-ord("A")+k) % 26 +ord("A"))
    ciphertext+=encrypted_char
    
    
print("Ciphertext:",ciphertext)