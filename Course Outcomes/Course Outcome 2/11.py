sqr=lambda s: s*s
a=int(input("Enter the length of side of a Square:"))
print("Area of Square is :",sqr(a))
rect=lambda a,b: a*b
a=int(input("Enter the length of a Rectangle:"))
b=int(input("Enter breadth of a Rectangle:"))
print("Area of Rectangle is:",rect(a,b))
tri=lambda b,h: 1/2*b*h
b=int(input("Enter the base length of Triangle:"))
h=int(input("Enter the height of Triangle:"))
print("Area of Triangle is :",tri(b,h))
