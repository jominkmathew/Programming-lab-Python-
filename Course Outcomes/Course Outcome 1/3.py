a=input("enter the text :")
b=a.split()
count={}
for word in b:
    count[word]=count.get(word,0)+1
print(count)
