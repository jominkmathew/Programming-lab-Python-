newFile = open("files.txt","w")
newFile.write("he\nhai\nhello")
newFile.close()
readFile = open("files.txt","r")
print(readFile.readlines())
lines = readFile.readlines()
readFile.close()
oddFile = open("oddlines.txt","w")
for i in range(0,len(lines),2):
    oddFile.write(lines[i])
oddFile.close()
