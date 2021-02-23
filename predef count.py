str="hello""\n""hai""\n""hi""\n""h"
fw=open("a.txt","w")
fw.write(str)
fw.close()
fr=open("a.txt","r")
str1=fr.readlines()
#print(str)
print(len(str1))
#for i in str1:
 #print(i)
