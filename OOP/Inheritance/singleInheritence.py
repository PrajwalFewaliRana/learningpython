
class Car:
    color= "white"
    @staticmethod
    def start():
        print("Car started")
        
    @staticmethod
    def stop():
        print("Car STopped")
        
class Toyota(Car):
    def __init__(self,name):
        self.name = name
        
car1 = Toyota("fortunate")
print(car1.name)
print(car1.start())