a=int(input("enter the current year :"))
b=int(input("enter the final year :"))
print("leap years are")
for i in range(a,b+1):
    if i%4==0:
        print(i)
