a=input("enter the words :")
b=a.split()
count=0
for i in b:
    if i.startswith("a"):
        count=count+1
print("count of name starts with a:",count)
