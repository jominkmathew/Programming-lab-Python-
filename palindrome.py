def palindrome(n):
    print(n)
    b=n[::-1]
    print(b)
    if (n==b):
        print("palindrome")
    else:
        print("not palindrome")
a=input("enter the string : ")
palindrome(a)
