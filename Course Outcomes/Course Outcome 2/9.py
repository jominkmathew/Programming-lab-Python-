a=int(input("enter the number :"))
for i in range(a):
    for j in range(i):
        print ('* ', end="")
    print('')
for i in range(a,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')
