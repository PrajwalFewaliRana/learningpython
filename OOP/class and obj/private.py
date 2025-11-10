# class Account:
#     def __init__(self,acc,pas):
#         self.account = acc
#         self.password = pas
        
# a1 = Account(12354,"23edsfe")
    
# print(a1.password)

class Account:
    def __init__(self,acc,pas):
        self.account = acc
        self.__password = pas #__ before the variable make its password
    
    def __hello(self): #private method
        print("hellow")
    def reset_pass(self): #but can acesses inside the class and pass it
        return self.__password  
    def welcome(self):
        self.__hello()
a1 = Account(12354,"23edsfe")
    
# print(a1.__password) #cannot print password outside the class
print(a1.reset_pass())
print(a1.welcome())