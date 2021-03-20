list=[]
for i in range(5):
    num=int(input("enter the number :"))
    if (num>100):
        list.append("over")
    else:
        list.append(num)
print(list)
