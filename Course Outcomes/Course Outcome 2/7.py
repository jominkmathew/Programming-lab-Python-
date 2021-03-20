a=input("Enter the string :")
print("After adding 'ing' and 'ly' for string :")
if a[-3:]=="ing":
    print(a[:-3]+"ly")
else:
    print(a+"ing")
