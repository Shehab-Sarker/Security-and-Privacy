# Problem 3: Cipher Menu-Driven Program

while True:
    
    print("\n==== Ceasear Cipher ====")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")
    
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
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
    
        print("Encrypted message :",ciphertext)
        
        
    elif choice == "2":
        # Decrpytion
        
        ciphertext= input("Enter Message : ")
        k =int(input("Enter key: "))

        plaintext=""

        for char in ciphertext:
            if char.isupper():
                decrypted_char=chr((ord(char)-ord("A")-k)%26 + ord("A"))

            elif char.islower():
                decrypted_char=chr((ord(char)-ord("a")-k)%26 + ord("a"))

            else:
                decrypted_char=char

            plaintext+=decrypted_char

        print("Decrypted Message :",plaintext)
        
    
    elif choice=="3":
        print("Program exited")
        break
    
    
    else:
        print("Invalid Choice. Please select 1, 2, or 3.")