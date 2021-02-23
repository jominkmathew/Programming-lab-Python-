class Time:
    __second
    __minute
    __hour
    def __init__(self,s,m,h):
      self.__second=s
      self.__minute=m
      sel.__hour=h
    def __add__(self,obj):
        self.__second+=obj.__second
        self.__minute+=obj.__minute
        self.__hour+=obj.__hour
        if(self.__second>=60):
            extra-minute=int(self.__second/60)
            self.__second=self.__second%60
            
     
 
