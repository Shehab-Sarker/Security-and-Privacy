ciphertext = input("Ciphertext : ").upper()
rails = int(input("Rails : "))

ciphertext=ciphertext.replace(" ","")

plaintext=""
n=len(ciphertext)

cycle=2*(rails-1)

rail_lengths=[]

for r in range(rails):
    count=0
    
    for i in range(n):
        if cycle==0:
            count+=1
        elif(i%cycle == r) or (i%cycle==cycle-r):
            count+=1
            
    rail_lengths.append(count)

rail_strings = []
index =0 

for count in rail_lengths:
    rail_strings.append(ciphertext[index: index + count])
    index += count
    
    
rail_index = [0]*rails

for i in range(n):
    if cycle ==0:
        r=0
        
    else:
        pos = i%cycle
        r= pos if pos<rails else cycle- pos
        
        
    plaintext+=rail_strings[r][rail_index[r]]
    rail_index[r] +=1
    
print("Plaintext : ", plaintext)