a = input("Enter your word : ")
b = a[0]
a = a.replace(b,"$")
a = b+a[1:]
print("First character replaced with ‘$’ except first character:",a)
