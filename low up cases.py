def string(a):
    uppercase=0
    lowercase=0 
    for b in a:
        if b.isupper():
           uppercase+=1
        elif b.islower():
           lowercase+=1
    print ("upper case : ", uppercase)
    print ("lower case : ", lowercase)
n=input("enter the string : ")
string(n)
