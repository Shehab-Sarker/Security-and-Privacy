
# Rail Fence Brute Force Attack

ciphertext = input("Ciphertext: ").upper()
ciphertext = ciphertext.replace(" ", "")

start, end=map(int,input("Enter Rail range : ").split())

n = len(ciphertext)

# Try different rail values from 2 to 6
for rails in range(start, end):

    plaintext = ""

    cycle = 2 * (rails - 1)

    # Step 1: Calculate character count of each rail
    rail_lengths = []

    for r in range(rails):
        count = 0

        for i in range(n):

            if (i % cycle == r) or (i % cycle == cycle - r):
                count += 1

        rail_lengths.append(count)

    # Step 2: Divide ciphertext into rail strings
    rail_strings = []
    index = 0

    for count in rail_lengths:
        rail_strings.append(ciphertext[index:index + count])
        index += count

    # Step 3: Read characters in zigzag order
    rail_index = [0] * rails

    for i in range(n):

        pos = i % cycle

        r = pos if pos < rails else cycle - pos

        plaintext += rail_strings[r][rail_index[r]]

        rail_index[r] += 1

    print("Rails =", rails, "->", plaintext)
