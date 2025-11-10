class Student:
    @staticmethod
    def __init__():
        print("Hello this is static function")
        
    
    #if we write above function without self parameter it throws an error
    #we need to call @staticmethod decorator to change the behaviour of the function
    # def __init__():
    #     print("This will not work without self parameter")
        
s1=Student()
