fw=open("a.txt","r")
str=fw.read()
a=open("e.txt","w")
a.write(str)
a.close()
b=open("e.txt","r")
c=b.read()
print(c)
                   
