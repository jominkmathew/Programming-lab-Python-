a={'a':10, 'b':23, 'c':45, 'd':2, 'e':87}
b=sorted(a, key=a.get, reverse=True)
c=sorted(a, key=a.get)
print("Decending Order")
print(b)
print("Ascending Order")
print(c)
