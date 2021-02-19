def string(s):
    UPPER_CASE=0
    LOWER_CASE=0 
    for c in s:
        if c.isupper():
           UPPER_CASE+=1
        elif c.islower():
           LOWER_CASE+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", UPPER_CASE)
    print ("No. of Lower case Characters : ", LOWER_CASE)
n=input("enter the string")
string(n)
