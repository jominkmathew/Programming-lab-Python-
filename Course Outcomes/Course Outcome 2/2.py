a=int(input("Enter the number:  "))
b=0
c=1
print("Fibonacci series of",a,"terms:")
print(b)
print(c)
for i in range(2,a):
    d=b+c
    b=c
    c=d
    print(d)
