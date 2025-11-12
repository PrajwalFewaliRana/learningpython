# class Person:
#     name = 'anonymous'
#     def changeName(self,name):
#         self.name=name
        
# p1=Person()
# p1.changeName('rambo')
# print(p1.name) #rambo    this doesnot change the class name either create a new name var inside obj
# print(Person.name) #anonymous


class Person:
    name = 'anonymous'
    # def changeName(self,name):
    #     Person.name=name
    #     # or
    #     # self.__class__.name= name
    
    # or we can use classmethod
    
    @classmethod #update the value of class too 
    def changeName(cls,name):
        cls.name = name
        
p1=Person()
p1.changeName('rambo')
print(p1.name) 
print(Person.name) 