class rectangle:
    __length=0
    __bredth=0
    __area=0
    def __init__(self,l,b):
      self.__length=l
      self.__bredth=b
    def area(self):
     self.__area=self.__length*self.__bredth
 
    def __gt__(self,other):
     if(self.__area > other.__area):
      return True
     else: 
      return False
ob1 =rectangle(2,3)
ob1.area()
ob2 =rectangle(4,5)
ob2.area()
if(ob1>ob2):
 print("obl is greater")
else:
 print("ob2 is greater")
