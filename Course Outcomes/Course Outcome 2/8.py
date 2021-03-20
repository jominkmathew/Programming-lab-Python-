list=[]
a=int(input("How many words want to enter :"))
for i in range(a):
    print("Enter the ",i+1,"word :")
    list.append(len(input()))
print("The longest word size is :"+str(max(list)))
