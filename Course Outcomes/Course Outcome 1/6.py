l1=[1,2,3,4,5,6,7]
l2=[2,4,5,1,2,3,4,5,8]
a=len(l1)
b=len(l2)
s1=sum(l1)
s2=sum(l2)
print("length of list 1:",a)
print("length of list 2:",b)
print("sum of list 1:",s1)
print("sum of list 2:",s2)
if a==b:
    print("lists are of same length")
else:
    print("lists are of diffrent length")
if s1==s2:
    print("sum of two lists are same")
else:
    print("sums are different")
l3=[x for x in l1 if x in l2]
print("common values in list 1 & list 2",l3)
