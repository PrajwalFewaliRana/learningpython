# class Student:
#     def __init__(self,name):
#         self._name = name
        
# s=Student("Prajwal") 
# s._name ="" #here is the problem we can also update empty string 
# print(s._name)



class Student:
    def __init__(self,name):
        # self._name = name #creating protected variable
        self.__name = name  #creating private variable
        
    #getter => returns private variable of class   
    @property  #converting methods to attributes => always returns
    def name(self):
        return self.__name
    
    #setter
    @name.setter
    def name(self,value):
        if value =="":
            raise ValueError("Empty string cannot be accepted")
        self.__name = value
    
    @name.deleter
    def name(self):
        print('deleleting name..')
        del self.__name
        
s1= Student("Prajwal")
print(s1.name)
# s1.name ="" #throws an error
del s1.name


