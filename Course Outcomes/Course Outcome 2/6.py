a=str(input("Enter the string: "))
freq={}
for letter in a:
    if letter in freq:
        freq[letter]+=1
    else:
        freq[letter]=1
print("The frequency of characters in",a,":",str(freq))
