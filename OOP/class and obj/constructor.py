#also called __init__ function

count = 0
class Car:
    location="kathmandu" #class attributr for common value store 
    name="anonyms" 
    #default constructor
    def __init__(self):
        pass
    
    #parameterized constructor
    def __init__(self,color,model,name):
        global count
        self.color= color #object attribut for different value store
        self.model = model
        self.name = name
        count+=1
c1 = Car("red","mt","bugadii")
c2 = Car("blue","Av","lamborgini")

print(c1.name,c1.model,c1.color) #since obj.attr(name) have higher precedence than class.attr 
print(c2.name,c2.model,c2.color)
print("constructor called",count,"times")
print(c1.location) #or
# print(Car.location)
