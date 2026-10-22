# Rail Fence Cipher Encryption using Formula

plaintext = input("Plaintext: ").upper()
rails = int(input("Rails: "))

plaintext = plaintext.replace(" ", "")

ciphertext = ""
n = len(plaintext)

for r in range(rails):
    for i in range(n):
        cycle = 2 * (rails - 1)

        if cycle == 0:
            ciphertext += plaintext[i]
        elif (i % cycle == r) or (i % cycle == cycle - r):
            ciphertext += plaintext[i]

print("Ciphertext:", ciphertext)
